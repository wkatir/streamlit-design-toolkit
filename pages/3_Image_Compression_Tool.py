import streamlit as st
from PIL import Image
import io
import zipfile
from datetime import datetime
from pathlib import Path


def optimize_image(image_file):
    """Optimiza la imagen automáticamente manteniendo la máxima calidad visual"""
    try:
        img = Image.open(image_file)
        output_buffer = io.BytesIO()

        # Configuración simple por formato
        if img.format == 'PNG':
            # Para PNG, mantener transparencia si existe
            if img.mode in ('RGBA', 'LA'):
                img_to_save = img
                save_params = {
                    'format': 'PNG',
                    'optimize': True
                }
            else:
                img_to_save = img.convert('RGB')
                save_params = {
                    'format': 'JPEG',
                    'quality': 85,
                    'optimize': True
                }
        else:
            # Para otros formatos, convertir a JPEG
            img_to_save = img.convert('RGB')
            save_params = {
                'format': 'JPEG',
                'quality': 85,
                'optimize': True
            }

        # Guardar imagen optimizada
        img_to_save.save(output_buffer, **save_params)
        output_buffer.seek(0)

        # Validar reducción de tamaño
        optimized_size = len(output_buffer.getvalue())
        if optimized_size >= image_file.size:
            return None, None

        return output_buffer.getvalue(), save_params['format']

    except Exception as e:
        st.error(f"Error optimizando imagen: {str(e)}")
        return None, None


def process_filename(original_name, optimized_format):
    """Genera nombre de archivo optimizado usando pathlib y el formato optimizado"""
    path = Path(original_name)
    new_suffix = f".{optimized_format.lower()}" if optimized_format else '.jpg'
    return f"{path.stem}_optimizado{new_suffix}"


def main():
    st.title("📁 Image Compression Tool")

    with st.expander("📌 Instrucciones de uso", expanded=True):
        st.markdown("""
        **Optimización automática de imágenes con máxima calidad visual**

        **Características:**
        - 🔍 Compresión inteligente automática
        - 🖼️ Mantiene transparencia en PNG
        - 📉 Reducción de tamaño garantizada
        - 🚀 Procesamiento por lotes
        - 📥 Descarga múltiple en ZIP
        """)

    uploaded_files = st.file_uploader(
        "Sube tus imágenes (máx. 50MB por archivo)",
        type=['png', 'jpg', 'jpeg'],
        accept_multiple_files=True
    )

    if uploaded_files and st.button("🚀 Optimizar Imágenes"):
        processed_images = []
        total_reduction = 0
        progress_bar = st.progress(0)
        total_files = len(uploaded_files)

        st.info("Optimizando imágenes...")

        for idx, file in enumerate(uploaded_files):
            try:
                if file.size > 50 * 1024 * 1024:
                    st.error(f"Archivo {file.name} excede 50MB")
                    continue

                original_size = file.size
                optimized_data, format_used = optimize_image(file)

                if optimized_data and format_used:
                    new_size = len(optimized_data)
                    reduction = original_size - new_size
                    total_reduction += reduction

                    new_name = process_filename(file.name, format_used)
                    processed_images.append((new_name, optimized_data, original_size, new_size))

                    st.write(f"✅ {file.name} optimizado ({reduction / 1024:.1f} KB ahorrados)")
                else:
                    st.write(f"⚠️ {file.name} no se optimizó porque no se logró reducir el tamaño.")

                progress_bar.progress((idx + 1) / total_files)

            except Exception as e:
                st.error(f"Error procesando {file.name}: {str(e)}")

        st.success(f"¡Optimización completada! (Ahorro total: {total_reduction / 1024:.1f} KB)")

        if processed_images:
            # Mostrar resultados
            st.subheader("Resultados de Optimización")
            cols = st.columns(3)
            with cols[0]:
                st.metric("Archivos procesados", len(processed_images))
            with cols[1]:
                st.metric("Espacio ahorrado", f"{total_reduction / 1024:.1f} KB")
            with cols[2]:
                avg_reduction = (total_reduction / len(processed_images)) / 1024
                st.metric("Reducción promedio", f"{avg_reduction:.1f} KB")

            # Generar ZIP
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for name, data, _, _ in processed_images:
                    zip_file.writestr(name, data)

            # Botón de descarga
            st.download_button(
                label="📥 Descargar Todas las Imágenes",
                data=zip_buffer.getvalue(),
                file_name=f"imagenes_optimizadas_{datetime.now().strftime('%Y%m%d_%H%M')}.zip",
                mime="application/zip"
            )


if __name__ == "__main__":
    main()
