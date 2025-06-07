import cv2
import numpy as np
from service.image_memory import ImageMemory


def separar_canais_rgb(memory: ImageMemory):
    azul, verde, vermelho = cv2.split(memory.getLastEdit())
    return vermelho, verde, azul


def separar_canal_R(memory: ImageMemory):
    vermelho, _, _ = separar_canais_rgb(memory)
    zeros = np.zeros_like(vermelho)
    imagem_r = cv2.merge([zeros, zeros, vermelho])  # B, G, R
    memory.addEdit(imagem_r)


def separar_canal_G(memory: ImageMemory):
    _, verde, _ = separar_canais_rgb(memory)
    zeros = np.zeros_like(verde)
    imagem_g = cv2.merge([zeros, verde, zeros])
    memory.addEdit(imagem_g)


def separar_canal_B(memory: ImageMemory):
    _, _, azul = separar_canais_rgb(memory)
    zeros = np.zeros_like(azul)
    imagem_b = cv2.merge([azul, zeros, zeros])
    memory.addEdit(imagem_b)
