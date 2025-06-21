import cv2
import numpy as np
from service.image_memory import ImageMemory

def ajuste_de_brilho(memory: ImageMemory, k=30):
    """ Ajusta o brilho de uma imagem adicionando um valor k a cada pixel."""

    imagem = memory.getLastEdit()

    # Obter as dimensões da imagem
    linhas, colunas = imagem.shape[:2]

    # Criar uma cópia da imagem para edição
    imagem = imagem.copy()

    # Ajustar o brilho
    for x in range(linhas):
        for y in range(colunas):
            for c in range(imagem.shape[2]):  # Para cada canal de cor
                # Converter para int16 para evitar overflow, fazer a operação e converter de volta para uint8
                valor_atual = int(imagem[x, y, c])
                novo_valor = min(max(valor_atual + k, 0), 255)
                imagem[x, y, c] = np.uint8(novo_valor)

    memory.addEdit(imagem)
