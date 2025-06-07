import cv2
from service.image_memory import ImageMemory

def espaco_de_cor_LAB(memory: ImageMemory):
    """
    Converte a imagem de BGR para o espaço de cor LAB.
    
    Parâmetros:
    imagem (numpy.ndarray): Imagem em formato BGR.
    
    Retorna:
    numpy.ndarray: Imagem convertida para o espaço de cor LAB.
    """
    imagem_LAB = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2Lab)

    memory.addEdit(imagem_LAB)
    
    return imagem_LAB