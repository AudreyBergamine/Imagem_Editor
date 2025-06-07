import cv2
from service.image_memory import ImageMemory



def calcular_histograma_colorido(memory: ImageMemory):
    """ Calcula o histograma de uma imagem colorida e retorna os vetores de histograma para os canais R, G e B. """
    
    # Inicializar os vetores HR, HG e HB com zeros
    HR = [0] * 256
    HG = [0] * 256
    HB = [0] * 256

    # Obter as dimensões da imagem
    quantidade_de_linhas, quantidade_de_colunas, _ = ImageMemory.shape

    # Percorrer cada pixel da ImageMemory
    for x in range(quantidade_de_linhas):
        for y in range(quantidade_de_colunas):
            
            # Obter os valores dos canais R, G e B
            B, G, R = ImageMemory[x, y]

            # Atualizar os vetores de histograma
            HR[R] += 1
            HG[G] += 1
            HB[B] += 1

    return HR, HG, HB
  