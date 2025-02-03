import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Design Hub",
        page_icon="🎨",
        layout="wide"
    )

    st.title("AI Design Hub")
    st.subheader("Automatización Inteligente de Diseño")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🌟 Generador de Fondos AI")
        st.markdown("""
        - Expansión de imágenes con IA
        - Mantenimiento de transparencia
        - Descarga múltiple en ZIP
        """)

    with col2:
        st.markdown("### ✂️ Smart Crop AI")
        st.markdown("""
        - Recorte inteligente con IA
        - Detección de rostros
        - Multiples modos de recorte
        """)

    with col3:
        st.markdown("### 📁 Optimizador de Imágenes")
        st.markdown("""
        - Compresión inteligente
        - Reducción de tamaño garantizada
        - Procesamiento por lotes
        """)

    st.markdown("---")
    st.markdown("Desarrollado por Wilmer Salazar")

if __name__ == "__main__":
    main()