import cv2
import numpy as np
from service.image_memory import ImageMemory

# Quantização ou agrupamento do histograma
def quantizar_histograma(memory: ImageMemory, quantidade_de_cores):
    """
    Quantiza o histograma de uma imagem, reduzindo o número de cores."""
    
    imagem = memory.getLastEdit()
    
    # Obter os valores dos canais R, G e B
    R = imagem[:, :, 0]
    G = imagem[:, :, 1]
    B = imagem[:, :, 2]

    # Aplicar a quantização
    R = np.floor(R / 256 * quantidade_de_cores) * (256 / quantidade_de_cores)
    G = np.floor(G / 256 * quantidade_de_cores) * (256 / quantidade_de_cores)
    B = np.floor(B / 256 * quantidade_de_cores) * (256 / quantidade_de_cores)
    
    # Recriar a imagem quantizada
    imagem_quantizada = np.stack([R, G, B], axis=2).astype(np.uint8)
    
    memory.addEdit(imagem_quantizada)
