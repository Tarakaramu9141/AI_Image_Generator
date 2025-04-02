from PIL import Image
import cv2
import numpy as np

def apply_style(image, style_name):
    img_array = np.array(image)
    
    if style_name == "Oil Painting":
        return _oil_paint_effect(img_array)
    elif style_name == "Cyberpunk":
        return _cyberpunk_effect(img_array)
    elif style_name == "Watercolor":
        return _watercolor_effect(img_array)
    return image

def _oil_paint_effect(img, size=7, dynRatio=1):
    res = cv2.xphoto.oilPainting(img, size, dynRatio)
    return Image.fromarray(res)

def _cyberpunk_effect(img):
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    limg = cv2.merge([clahe.apply(l), a, b])
    res = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)
    hsv = cv2.cvtColor(res, cv2.COLOR_RGB2HSV)
    hsv[:,:,1] = hsv[:,:,1]*1.5
    res = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    return Image.fromarray(res)

def _watercolor_effect(img):
    res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    return Image.fromarray(res)
