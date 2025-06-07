import cv2
import numpy as np
from service.image_memory import ImageMemory

def stretching_histograma(memory: ImageMemory):
    
    # Obter os valores mínimo e máximo dos pixels da imagem
    min_val = ImageMemory.min()
    max_val = ImageMemory.max()
    
    # Aplicar o stretching
    imagem_stretched = (ImageMemory - min_val) * 255 / (max_val - min_val)
    
    return imagem_stretched.astype(np.uint8)