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


def process_image(image, width, height, gravity_option):
    if not st.session_state.get('cloudinary_initialized', False):
        st.error("Cloudinary no está inicializado correctamente")
        return None

    try:
        if not check_file_size(image, 10):
            st.error(f"La imagen {image.name} excede el límite de 10MB")
            return None

        image_content = image.read()

        response = cloudinary.uploader.upload(
            image_content,
            transformation=[{
                "width": width,
                "height": height,
                "crop": "fill",
                "gravity": gravity_option,
                "quality": 100,
                "dpr": 1,
            }]
        )

        processed_url = response['secure_url']
        processed_image = requests.get(processed_url).content

        # Eliminar la imagen de Cloudinary después de procesarla
        cloudinary.api.delete_resources([response['public_id']])

        return processed_image
    except Exception as e:
        st.error(f"Error procesando imagen: {e}")
        return None


def main():
    # Inicializar Cloudinary al principio
    init_cloudinary()

    st.title("✂️ Cloudinary Smart Crop")

    # Configuración de dimensiones y gravedad
    col1, col2, col3 = st.columns(3)
    with col1:
        width = st.number_input("Ancho (px)", value=1000, min_value=100, max_value=3000)
    with col2:
        height = st.number_input("Alto (px)", value=460, min_value=100, max_value=3000)
    with col3:
        gravity_option = st.selectbox(
            "Gravedad",
            ["auto", "center", "face", "faces", "north", "south", "east", "west"],
            help="Determina qué parte de la imagen mantener al recortar"
        )

    uploaded_files = st.file_uploader(
        "Sube tus imágenes (máx. 10MB por archivo)",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.header("Imágenes Originales")
        cols = st.columns(3)
        for idx, file in enumerate(uploaded_files):
            with cols[idx % 3]:
                st.image(file)

        if st.button("Procesar Imágenes"):
            if not st.session_state.get('cloudinary_initialized', False):
                st.error("Por favor, asegúrate de que Cloudinary esté correctamente configurado")
                return

            processed_images = []
            progress_bar = st.progress(0)

            for idx, file in enumerate(uploaded_files):
                with st.spinner(f'Procesando imagen {idx + 1}/{len(uploaded_files)}...'):
                    processed = process_image(file, width, height, gravity_option)
                    if processed:
                        processed_images.append(processed)
                    progress_bar.progress((idx + 1) / len(uploaded_files))

            if processed_images:
                st.header("Imágenes Procesadas")
                cols = st.columns(3)
                for idx, img_bytes in enumerate(processed_images):
                    with cols[idx % 3]:
                        st.image(img_bytes)

                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                    for idx, img_bytes in enumerate(processed_images):
                        zip_file.writestr(f'imagen_procesada_{idx}.jpg', img_bytes)

                st.download_button(
                    label="Descargar todas las imágenes",
                    data=zip_buffer.getvalue(),
                    file_name="imagenes_procesadas.zip",
                    mime="application/zip"
                )


if __name__ == "__main__":
    main()