```markdown
# AI Design Hub 🎨

A suite of AI-powered design tools for automating and optimizing creative workflows.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## Key Features ✨

### 🌟 AI Background Generator
- Intelligent image expansion with AI
- Context-aware background generation
- Batch processing with ZIP download
- PNG/JPG/WEBP support
- Transparency preservation

### ✂️ Smart Crop Tool
- Face detection cropping
- Multiple gravity modes (auto, face, north, etc)
- Batch processing
- Precision resizing

### 📁 Image Optimizer
- Smart compression algorithms
- Guaranteed size reduction
- PNG transparency support
- Detailed compression metrics

## Installation ⚙️

1. Clone repository:
```bash
git clone https://github.com/wkatir/ai-design-hub.git
cd ai-design-hub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Cloudinary credentials (for AI features):
```bash
# Create .env file
echo "CLOUDINARY_URL='your_cloudinary_url'" > .env
```

## Usage 🚀

### Launch Main Dashboard
```bash
streamlit run main.py
```

### Direct Access to Tools
```bash
# Background Generator
streamlit run pages/1_🌌_Background_Generator.py

# Smart Crop Tool
streamlit run pages/2_✂️_Smart_Crop.py

# Image Optimizer
streamlit run pages/3_📁_Image_Compression.py
```

## Requirements 📋

- Python 3.8+
- [Cloudinary](https://cloudinary.com) account (for AI features)
- Streamlit ≥1.28.0
- Core dependencies: `Pillow`, `python-dotenv`, `cloudinary`, `requests`

## File Structure 📂
```
ai-design-hub/
├── main.py
├── pages/
│   ├── 1_🌌_Background_Generator.py
│   ├── 2_✂️_Smart_Crop.py
│   └── 3_📁_Image_Compression.py
├── requirements.txt
└── .env.example
```

## Support & Contribution 🤝

**Report Issues:**  
[GitHub Issues](https://github.com/yourusername/ai-design-hub/issues)

**Feature Requests:**  
[Suggest Features](mailto:features@example.com)

**Contribution Guide:**
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License 📄
Distributed under MIT License. See [LICENSE](LICENSE) for more information.

---