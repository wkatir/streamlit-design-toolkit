import streamlit as st

st.set_page_config(page_title="Herramientas Recomendadas", page_icon="🛠️")

st.title("🛠️ Desktop Tools")
st.markdown("Aplicaciones prácticas para optimizar tu productividad")

# --- Ordyn Organizador ---
st.subheader("Ordyn - Automatic Organizer")
st.markdown("""
**Función principal:**  
Clasificación automática de archivos por tipo

**Formatos soportados:**

- **Documentos y texto:**  
  DOC, DOCX, PDF, TXT, RTF, ODT, MD, EPUB, MOBI, XML, WPD (+20 formatos de procesamiento de texto y eBooks)

- **Datos y hojas de cálculo:**  
  XLS, XLSX, CSV, ODS, DB, SQLITE, MDB (+15 formatos de Excel, bases de datos y análisis de datos)

- **Presentaciones y diagramas:**  
  PPT, PPTX, KEY, ODP, PPSX (+12 formatos de presentaciones y plantillas)

- **Multimedia y diseño:**  
  - _Imágenes:_ JPG, PNG, WEBP, SVG, RAW, TIFF, ICO (30+ formatos incluyendo cámaras profesionales)
  - _Video/audio:_ MP4, AVI, MKV, MP3, WAV, FLAC (+25 codecs y formatos multimedia)
  - _Diseño gráfico:_ PSD, AI, INDD, XD, DWG, BLEND (+18 formatos de Adobe, AutoCAD y 3D)

- **Archivos técnicos y desarrollo:**  
  - _Programación:_ PY, JS, HTML, CPP, JAVA, JSON (+15 lenguajes y formatos de código)
  - _Sistemas:_ EXE, MSI, DLL, SYS, BAT, CMD (+20 ejecutables y scripts para Windows)

- **Compresión y paquetes:**  
  ZIP, RAR, 7Z, TAR, ISO, DEB, APK (+12 formatos de archivos comprimidos y paquetes de software)
  
**Requisitos:**
- Windows 10/11
- 20 MB espacio libre
- Versión 2.1 (2024)
""")

# Enlace de descarga directo
st.markdown("[Descargar Ordyn desde Google Drive (15 MB)](https://drive.google.com/file/d/1Bc0cwmaUcX-9QyVmCVdSC3hYFsSVM_D-/view?usp=drive_link)")

# Nota final
st.markdown("---")
st.caption("Todas las herramientas son portables y de uso libre")