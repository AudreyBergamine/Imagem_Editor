import cv2
from service.image_memory import ImageMemory

def negativo_da_imagem(memory: ImageMemory):
    """
    Aplica a transformação negativa a uma imagem.
    """
    
    imagem = memory.getLastEdit()

    # Obtém as dimensões da imagem
    linhas, colunas = imagem.shape[:2]

    # Aplica a transformação negativa
    for x in range(linhas):
        for y in range(colunas):
            imagem[x, y] = 255 - imagem[x, y]

    return imagem

