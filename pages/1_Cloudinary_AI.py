import streamlit as st
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import io
import zipfile


def init_cloudinary():
    """Inicializa Cloudinary con credenciales desde secrets"""
    if 'cloudinary_initialized' not in st.session_state:
        try:
            cloudinary.config(url=st.secrets['CLOUDINARY_URL'])
            st.session_state.cloudinary_initialized = True
            cleanup_cloudinary()
        except Exception as e:
            st.error("Error: No se encontraron las credenciales de Cloudinary en secrets.toml")
            st.session_state.cloudinary_initialized = False


def check_file_size(file, max_size_mb=10):
    file.seek(0, 2)
    file_size = file.tell() / (1024 * 1024)
    file.seek(0)
    return file_size <= max_size_mb


def cleanup_cloudinary():
    """Limpia todos los recursos de Cloudinary"""
    if not st.session_state.get('cloudinary_initialized', False):
        return

    try:
        result = cloudinary.api.resources()
        if 'resources' in result and result['resources']:
            public_ids = [resource['public_id'] for resource in result['resources']]
            if public_ids:
                cloudinary.api.delete_resources(public_ids)
    except Exception as e:
        st.error(f"Error al limpiar recursos: {e}")


def process_image(image, width, height):
    """
    Procesa la imagen usando Cloudinary. Se asegura de reiniciar el puntero del archivo.
    Retorna una tupla (imagen_procesada_bytes, extension_del_archivo).
    """
    if not st.session_state.get('cloudinary_initialized', False):
        st.error("Cloudinary no está inicializado correctamente")
        return None, None

    try:
        # Reiniciar el puntero para garantizar la lectura completa
        image.seek(0)
        if not check_file_size(image, 10):
            st.error(f"La imagen excede el límite de 10MB")
            return None, None

        image_content = image.read()

        response = cloudinary.uploader.upload(
            image_content,
            transformation=[{
                "width": width,
                "height": height,
                "crop": "pad",
                "background": "gen_fill",
                "quality": 100,
                "dpr": 3,
                "flags": "preserve_transparency"
            }]
        )

        processed_url = response['secure_url']
        processed_image = requests.get(processed_url).content
        file_format = response.get('format', 'jpg')  # Se obtiene el formato real procesado
        return processed_image, file_format
    except Exception as e:
        st.error(f"Error procesando imagen: {e}")
        return None, None


def main():
    init_cloudinary()

    st.title("🤖 Cloudinary AI Background Generator")

    with st.expander("📌 ¿Cómo usar esta herramienta?", expanded=True):
        st.markdown("""
        **Transforma tus imágenes automáticamente con IA:**                    

        Esta herramienta utiliza la IA de Cloudinary para:
        - 🔄 Redimensionar imágenes manteniendo la relación de aspecto
        - 🎨 Generar fondos coherentes con la imagen usando IA
        - 📥 Descargar múltiples imágenes procesadas en un ZIP

        **Formatos soportados:**
        ✅ PNG, JPG, JPEG, WEBP

        **Pasos para usar:**
        1. ⚙️ Define las dimensiones deseadas (ancho y alto)
        2. 📤 Sube tus imágenes (hasta 10MB c/u)
        3. 🚀 Haz clic en "Procesar Imágenes"
        4. ⏬ Descarga los resultados finales

        **Características clave:**
        - Mantiene transparencia en PNGs
        - Soporte para formatos modernos (WEBP)
        - Calidad ultra HD (DPR 3)
        - Procesamiento por lotes
        - Fondo generado por IA se adapta al contexto

        **Notas importantes:**
        - Las imágenes subidas se borrarán automáticamente después del procesamiento
        - Para mejores resultados con IA, usa imágenes con sujetos bien definidos
        - El tiempo de procesamiento varía según el tamaño y cantidad de imágenes
        """)

    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("Ancho (px)", value=1000, min_value=100, max_value=3000)
    with col2:
        height = st.number_input("Alto (px)", value=460, min_value=100, max_value=3000)

    uploaded_files = st.file_uploader(
        "Sube tus imágenes (máx. 10MB por archivo)",
        type=['png', 'jpg', 'jpeg', 'webp'],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.header("Imágenes Originales")
        cols = st.columns(3)
        # Guardar el contenido original para evitar que se consuma el stream
        original_images = []
        for idx, file in enumerate(uploaded_files):
            file_bytes = file.getvalue()
            original_images.append((file.name, file_bytes))
            with cols[idx % 3]:
                st.image(file_bytes)

        if st.button("Procesar Imágenes"):
            if not st.session_state.get('cloudinary_initialized', False):
                st.error("Por favor, asegúrate de que Cloudinary esté correctamente configurado")
                return

            processed_images = []
            progress_bar = st.progress(0)

            for idx, (name, img_bytes) in enumerate(original_images):
                # Crear un nuevo objeto BytesIO para cada imagen
                img_io = io.BytesIO(img_bytes)
                with st.spinner(f'Procesando imagen {idx + 1}/{len(original_images)}...'):
                    processed, file_format = process_image(img_io, width, height)
                    if processed:
                        processed_images.append((processed, file_format))
                    progress_bar.progress((idx + 1) / len(original_images))

            if processed_images:
                st.header("Imágenes Procesadas")
                cols = st.columns(3)
                for idx, (img_bytes, file_format) in enumerate(processed_images):
                    with cols[idx % 3]:
                        st.image(img_bytes)

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for idx, (img_bytes, file_format) in enumerate(processed_images):
                        zip_file.writestr(f'imagen_procesada_{idx}.{file_format}', img_bytes)

                st.download_button(
                    label="Descargar todas las imágenes",
                    data=zip_buffer.getvalue(),
                    file_name="imagenes_procesadas.zip",
                    mime="application/zip"
                )


if __name__ == "__main__":
    main()
