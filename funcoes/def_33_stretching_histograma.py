import cv2
import numpy as np

def stretching_histograma(imagem):
    
    # Obter os valores mínimo e máximo dos pixels da imagem
    min_val = imagem.min()
    max_val = imagem.max()
    
    # Aplicar o stretching
    imagem_stretched = (imagem - min_val) * 255 / (max_val - min_val)
    
    return imagem_stretched.astype(np.uint8)