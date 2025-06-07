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

    # Exibe as imagens convertidas
    cv2.imshow('Imagem Original', memory.getLastEdit())
    cv2.imshow('Imagem em Escala de Cinza (NC)', imagemNC)
    cv2.imshow('Imagem em YCrCb', imagemCrCb)
    cv2.imshow('Imagem em LAB', imagemLab)
    cv2.imshow('Imagem em HSV', imagemHSV)


    return {
        "NC": imagemNC,
        "YCrCb": imagemCrCb,
        "LAB": imagemLab,
        "HSV": imagemHSV
    }
