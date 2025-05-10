import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem



def calcular_histograma_colorido(imagem):
    
    # Inicializar os vetores HR, HG e HB com zeros
    HR = [0] * 256
    HG = [0] * 256
    HB = [0] * 256

    # Obter as dimensões da imagem
    quantidade_de_linhas, quantidade_de_colunas, _ = imagem.shape

    # Percorrer cada pixel da imagem
    for x in range(quantidade_de_linhas):
        for y in range(quantidade_de_colunas):
            
            # Obter os valores dos canais R, G e B
            B, G, R = imagem[x, y]

            # Atualizar os vetores de histograma
            HR[R] += 1
            HG[G] += 1
            HB[B] += 1

    return HR, HG, HB
  