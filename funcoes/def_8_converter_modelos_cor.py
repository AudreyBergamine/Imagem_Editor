import cv2
from service.image_memory import ImageMemory

def converter_modelos_cor(memory: ImageMemory):
    """
    Converte uma imagem para diferentes modelos de cor.
    """

    # Converte a imagem para diferentes modelos de cor
    imagemNC = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2GRAY)
    imagemCrCb = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2YCrCb)
    imagemLab = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2LAB)
    imagemHSV = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2HSV)

    # Adiciona a imagem em escala de cinza à memória (como exemplo)
    # O usuário pode escolher qual conversão usar
    memory.addEdit(imagemNC)

    # Retorna um dicionário com todas as conversões
    return {
        "NC": imagemNC,
        "YCrCb": imagemCrCb,
        "LAB": imagemLab,
        "HSV": imagemHSV
    }
