import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def calcular_histograma(imagem):
    
    # Obter as dimensões da imagem
    linhas, colunas = imagem.shape[:2]
    
    # Inicializar o vetor do histograma com zeros (256 níveis de intensidade)
    vetor_histograma = [0] * 256
    
    # Calcular o histograma
    for x in range(linhas):
        for y in range(colunas):
            intensidade = imagem[x, y]
            vetor_histograma[intensidade] += 1
    
    return vetor_histograma
  