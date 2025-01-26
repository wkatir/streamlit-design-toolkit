import streamlit as st


def main():
    st.set_page_config(
        page_title="AI Design Hub",
        page_icon="🎨",
        layout="wide"
    )

    st.title("AI Design Hub")
    st.subheader("Automatización Inteligente de Diseño Publicitario")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("### 🌟 Cloudinary AI")
        st.markdown("""
       - Expansión inteligente de imágenes
       - Generación de contenido con IA
       """)
        st.button("Expandir lienzo", key="canvas")

    with col2:
        st.markdown("### 🔮 Meta Segment AI")
        st.markdown("""
       - Segmentación precisa con SAM
       - Edición por objetos
       """)
        st.button("Segmentar", key="sam")

    with col3:
        st.markdown("### ☁️ Cloud Preview")
        st.markdown("""
       - Previews optimizados
       - Transformación en la nube
       """)
        st.button("Generar preview", key="preview")

    with col4:
        st.markdown("### 🚀 Próximamente")
        st.markdown("""
       - Herramientas avanzadas
       - Innovación constante
       """)
        st.button("Más información", key="coming_soon", disabled=True)

    st.markdown("---")
    st.markdown("Desarrollado por Wilmer Salazar")


if __name__ == "__main__":
    main()