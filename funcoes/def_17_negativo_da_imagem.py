import cv2
from service.image_memory import ImageMemory

def negativo_da_imagem(memory: ImageMemory):
    # Obtém as dimensões da imagem
    linhas, colunas = ImageMemory.shape[:2]
        
    # Aplica a transformação negativa
    for x in range(linhas):
        for y in range(colunas):
            ImageMemory[x, y] = 255 - ImageMemory[x, y]
    
    return ImageMemory



    
