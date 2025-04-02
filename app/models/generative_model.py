import torch
import os
from diffusers import StableDiffusionPipeline
from utils.logger import setup_logger

# Disable CUDA entirely
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Prevents any CUDA initialization

logger = setup_logger()

class HDImageGenerator:
    def __init__(self):
        self.device = "cpu"  # Explicitly force CPU for Streamlit Cloud
        logger.info(f"Initialized device as: {self.device}")
        logger.info(f"CUDA available: {torch.cuda.is_available()}")
        self.models = {
            "StableDiffusion15": "runwayml/stable-diffusion-v1-5",
        }
        self.pipes = {}
    
    def load_pipeline(self, model_key):
        if model_key not in self.models:
            raise ValueError(f"Unknown model key: {model_key}")
            
        if model_key not in self.pipes:
            logger.info(f"Loading {model_key} pipeline on device: {self.device}")
            pipe = StableDiffusionPipeline.from_pretrained(
                self.models[model_key],
                torch_dtype=torch.float32,  # Force float32 for CPU
                use_safetensors=True,
                low_cpu_mem_usage=True
            )
            pipe = pipe.to("cpu")  # Explicitly move to CPU
            logger.info("Pipeline moved to CPU")
            pipe.enable_attention_slicing()  # Reduce memory usage (CPU-safe)
            self.pipes[model_key] = pipe
        
        return self.pipes[model_key]
    
    def generate_hd_image(self, prompt, model_key="StableDiffusion15", steps=20, guidance_scale=7.5):
        try:
            logger.info(f"Generating image with prompt: {prompt}, steps: {steps}, guidance: {guidance_scale}")
            pipe = self.load_pipeline(model_key)
            logger.info(f"Pipeline device: {pipe.device}")
            image = pipe(
                prompt,
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                height=512,
                width=512
            ).images[0]
            logger.info("Image generation completed successfully")
            return image
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise

# Global instance
image_generator = HDImageGenerator()
generate_hd_image = image_generator.generate_hd_image
