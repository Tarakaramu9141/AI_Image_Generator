# Pro AI Image Studio

Welcome to **Pro AI Image Studio**, a web-based application that lets you create stunning AI-generated artwork with ease! Powered by Stable Diffusion, this app allows you to generate high-quality images up to 720p resolution, apply artistic styles, and download your creations—all through a simple, user-friendly interface hosted on Streamlit Community Cloud.

## Features
- **AI Image Generation**: Create detailed images from text prompts using the Stable Diffusion 1.5 model.
- **Style Transfer**: Apply artistic effects like Oil Painting, Cyberpunk, and Watercolor to your images.
- **Upscaling**: Enhance images to 720p resolution for sharper visuals.
- **Customizable Settings**: Adjust creativity (guidance scale) and generation steps for personalized results.
- **Downloadable Output**: Save your artwork as PNG files.

## Model Details
This app uses the **`runwayml/stable-diffusion-v1-5`** model, a lightweight yet powerful version of Stable Diffusion. Key highlights:
- **Quality**: Produces sharper, more accurate images compared to earlier base models, with excellent prompt adherence.
- **Efficiency**: Optimized to run on CPU within Streamlit Cloud’s free tier (~1 GB RAM), making it accessible without GPU requirements.
- **Size**: Approximately 1 GB, balancing quality and resource usage for cloud deployment.

## Deployment
The app is hosted on [Streamlit Community Cloud](https://streamlit.io/cloud), allowing anyone to access it via a simple URL [(e.g., `https://tarakaramu9141-ai-image-generator.streamlit.app](https://aiimagegenerator-troxy.streamlit.app/). No local setup is required—just click the link and start creating!

## Project Structure
ai-image-generator/
├── app/
│   ├── main.py              # Main Streamlit app
│   ├── components/
│   │   ├── style_transfer.py  # Art style application
│   │   └── upscaler.py       # Image upscaling to 720p
│   ├── models/
│   │   └── generative_model.py  # Stable Diffusion model logic
│   ├── utils/
│   │   ├── animations.py    # Loading animation handler
│   │   └── logger.py        # Logging setup
│   ├── assets/
│   │   ├── styles.css       # Custom CSS
│   │   └── loading_animation.json  # Lottie animation
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .gitignore              # Git ignore rules


## Prerequisites
- Python 3.9 or higher
- Git
- A GitHub account (for deployment)

## Local Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-image-generator.git
cd ai-image-generator```

## 2.Create a Virtual Environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the APP
streamlit run app/main.py
Open your browser to http://localhost:8501.
Enter a prompt (e.g., "A majestic lion in the savannah at sunset") and click "Generate Masterpiece".

## Notes 
The first run downloads the stabilityai/stable-diffusion-2-1-base model (~1.2 GB) to your Hugging Face cache (~/.cache/huggingface/hub).
Generation takes 10-60 seconds on a CPU, depending on hardware and steps.

## Alternatives for Better Image Generation
The current setup uses a lightweight model for speed and low storage. For higher quality or faster generation, consider these alternatives

### 1. Local GPU setup
Why: Use float16 and larger models (e.g., SDXL) for better quality and speed.
How:
Install CUDA and cuDNN (see NVIDIA CUDA Toolkit).
Install GPU-enabled PyTorch:

pip install torch --extra-index-url https://download.pytorch.org/whl/cu118
Update generative_model.py to use torch.float16 on "cuda".
Model Suggestion: runwayml/stable-diffusion-v1-5 (~1 GB) or stabilityai/stable-diffusion-xl-base-1.0 (~5 GB).
Pros: Faster (5-20s), higher quality (up to 1024x1024 natively).
Cons: Requires a GPU, not cloud-friendly.

### 2. Use a Distilled Model
Why: Smaller, faster models with decent quality.
Model Suggestion: segmind/SSD-1B (~2 GB, optimized for speed).
How: Replace "stabilityai/stable-diffusion-2-1-base" in generative_model.py with "segmind/SSD-1B".
Pros: Faster than SD 2.1, still lightweight.
Cons: Slightly lower quality than full SDXL.

### 3. Advanced Upscaling

Why: Improve quality beyond bicubic interpolation.
Tool: Use Real-ESRGAN or SwinIR.
How: Integrate a pre-trained upscaler (e.g., xinntao/Real-ESRGAN):
Add to requirements.txt: realesrgan.
Update upscaler.py to use Real-ESRGAN instead of PyTorch’s F.interpolate.
Pros: Sharper, more detailed 720p+ images.
Cons: Increases memory usage, slower on CPU.

### Troubleshooting
"Out of Memory" on Cloud: Reduce steps or disable upscaling in main.py.
Dependency Errors: Check logs in Streamlit Cloud and adjust requirements.txt.
Slow Generation: Test with fewer steps (e.g., 10) locally first.

## License
 MIT License - feel free to use, modify, and distribute

 ## Contact 
 For issues or suggestions, open a github issue or reach out to [tarakram9141@gmail.com].
