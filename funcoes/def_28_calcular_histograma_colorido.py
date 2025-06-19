import cv2
from service.image_memory import ImageMemory
import numpy as np
import matplotlib.pyplot as plt



def calcular_histograma_colorido(memory: ImageMemory):
    """ Calcula o histograma de uma imagem colorida e retorna os vetores de histograma para os canais R, G e B. """
    imagem = memory.getLastEdit()

    # Verifica se a imagem é colorida
    if len(imagem.shape) != 3 or imagem.shape[2] != 3:
        raise ValueError("A imagem fornecida não é colorida (esperado 3 canais).")

    # Calcula o histograma para cada canal (B, G, R)
    HB = cv2.calcHist([imagem], [0], None, [256], [0, 256]).flatten()
    HG = cv2.calcHist([imagem], [1], None, [256], [0, 256]).flatten()
    HR = cv2.calcHist([imagem], [2], None, [256], [0, 256]).flatten()

    # Converte para inteiros
    HR = HR.astype(int).tolist()
    HG = HG.astype(int).tolist()
    HB = HB.astype(int).tolist()

    return HR, HG, HB
  