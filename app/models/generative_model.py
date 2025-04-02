import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from utils.logger import setup_logger

logger = setup_logger()

class HDImageGenerator:
    def __init__(self):
        self.device = "cpu"  # Streamlit Cloud has no GPU
        self.models = {
            "StableDiffusion": "runwayml/stable-diffusion-v1-5"  # ~1 GB model
        }
        self.pipes = {}
    
    def load_pipeline(self, model_key):
        if model_key not in self.models:
            raise ValueError(f"Unknown model key: {model_key}")
            
        if model_key not in self.pipes:
            logger.info(f"Loading {model_key} pipeline...")
            
            pipe = StableDiffusionPipeline.from_pretrained(
                self.models[model_key],
                torch_dtype=torch.float32,  # CPU only, no float16
                use_safetensors=True,
                low_cpu_mem_usage=True  # Optimize for low memory
            ).to(self.device)
            
            # Use a fast scheduler to reduce steps and memory
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
            self.pipes[model_key] = pipe
        
        return self.pipes[model_key]
    
    def generate_hd_image(self, prompt, model_key="StableDiffusion", steps=20, guidance_scale=7.5):
        try:
            pipe = self.load_pipeline(model_key)
            image = pipe(
                prompt,
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                height=256,  # Smaller size for speed and memory
                width=256
            ).images[0]
            return image
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise

# Global instance
image_generator = HDImageGenerator()
generate_hd_image = image_generator.generate_hd_image