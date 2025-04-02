import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import cv2
import json
import time
from models.generative_model import generate_hd_image
from components.style_transfer import apply_style
from components.upscaler import upscale_image
from utils.animations import load_lottie
from utils.logger import setup_logger

# Setup
logger = setup_logger()
st.set_page_config(page_title="Pro AI Image Studio", layout="wide", page_icon="🎨")

# Load assets
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
loading_anim = load_lottie("assets/loading_animation.json")

def main():
    st.title("🎨 Pro AI Image Studio")
    st.markdown("Create stunning 720p artwork with AI magic ✨ (Hosted on Streamlit Cloud)")
    
    with st.sidebar:
        st.header("🛠️ Settings")
        model_choice = st.selectbox(
            "Model",
            ["Stable Diffusion 1.5 (Enhanced Quality)"],
            index=0
        )
        model_map = {
            "Stable Diffusion 1.5 (Enhanced Quality)": "StableDiffusion15"
        }
        selected_model_key = model_map[model_choice]
        
        col1, col2 = st.columns(2)
        with col1:
            steps = st.slider("Steps", 10, 30, 20, help="More steps = better quality but slower")
        with col2:
            cfg = st.slider("Creativity", 1.0, 10.0, 7.5, help="Higher = more creative")
        
        enhance = st.toggle("Upscale to 720p", True)
        style = st.selectbox("Art Style", ["None", "Oil Painting", "Cyberpunk", "Watercolor"])
    
    prompt = st.text_area("📝 Describe your image:", "A majestic lion in the savannah at sunset")
    
    if st.button("✨ Generate Masterpiece", type="primary"):
        with st.spinner("Generating... (May take 1-2 minutes on cloud)"):
            placeholder = st.empty()
            with placeholder:
                st_lottie(loading_anim, height=200, key="loading")
            
            try:
                start_time = time.time()
                
                # Generate base image (512x512)
                base_image = generate_hd_image(
                    prompt=prompt,
                    model_key=selected_model_key,
                    steps=steps,
                    guidance_scale=cfg
                )
                
                # Apply enhancements
                if enhance:
                    base_image = upscale_image(base_image, target_height=720)
                if style != "None":
                    base_image = apply_style(base_image, style)
                
                # Display
                placeholder.empty()
                st.image(base_image, caption=prompt, use_column_width=True)
                
                # Performance metrics
                gen_time = time.time() - start_time
                st.success(f"Generated in {gen_time:.1f}s | Resolution: {base_image.size}")
                
                # Download
                img_bytes = base_image.tobytes()
                st.download_button(
                    "💾 Download Image",
                    data=img_bytes,
                    file_name="ai_artwork.png",
                    mime="image/png"
                )
                
            except Exception as e:
                placeholder.empty()
                st.error(f"Generation failed: {str(e)}")
                logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
