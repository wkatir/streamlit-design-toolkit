```markdown
# AI Design Hub

A suite of AI-powered design tools for automating and optimizing creative workflows.

## Key Features

### AI Background Generator
- Intelligent image expansion with AI
- Context-aware background generation
- Batch processing with ZIP download
- PNG/JPG/WEBP support
- Transparency preservation

### Smart Crop Tool
- Face detection cropping
- Multiple gravity modes (auto, face, north, etc)
- Batch processing
- Precision resizing

### Image Optimizer
- Smart compression algorithms
- Guaranteed size reduction
- PNG transparency support
- Detailed compression metrics

## Installation

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
echo "CLOUDINARY_URL='your_cloudinary_url'" > .env
```

## Usage

### Main Dashboard
```bash
streamlit run main.py
```

### Individual Tools
```bash
# Background Generator
streamlit run pages/1_Background_Generator.py

# Smart Crop Tool
streamlit run pages/2_Smart_Crop.py

# Image Optimizer
streamlit run pages/3_Image_Compression.py
```

## Requirements
- Python 3.8+
- Cloudinary account
- Streamlit ≥1.28.0
- Pillow, python-dotenv, cloudinary, requests

## File Structure
```
ai-design-hub/
├── main.py
├── pages/
│   ├── 1_Background_Generator.py
│   ├── 2_Smart_Crop.py
│   └── 3_Image_Compression.py
├── requirements.txt
└── .env.example
```

## Support & Contribution
- Issues: GitHub Issues tracker
- PRs: Follow standard GitHub workflow

## License
MIT License

