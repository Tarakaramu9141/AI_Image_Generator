from PIL import Image
import torch
import numpy as np
from torch.nn import functional as F

class SimpleUpscaler:
    def __init__(self):
        self.device = "cpu"  # Streamlit Cloud has no GPU
    
    def upscale(self, image, target_height=720):
        """Upscale to 720p while preserving aspect ratio"""
        img_tensor = torch.from_numpy(np.array(image)).float().permute(2, 0, 1)
        img_tensor = img_tensor.unsqueeze(0).to(self.device)
        
        orig_height, orig_width = image.size[1], image.size[0]
        scale_factor = target_height / orig_height
        target_width = int(orig_width * scale_factor)
        
        upscaled = F.interpolate(
            img_tensor,
            size=(target_height, target_width),
            mode='bicubic',
            align_corners=False
        )
        
        upscaled = upscaled.squeeze(0).permute(1, 2, 0).cpu().numpy()
        upscaled = np.clip(upscaled, 0, 255).astype(np.uint8)
        return Image.fromarray(upscaled)

def upscale_image(image, target_height=720):
    return SimpleUpscaler().upscale(image, target_height)
