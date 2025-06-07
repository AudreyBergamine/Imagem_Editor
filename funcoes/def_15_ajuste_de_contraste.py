import cv2
from service.image_memory import ImageMemory

def ajuste_de_contraste(memory: ImageMemory, k):
    """
    Ajusta o contraste de uma imagem multiplicando cada pixel por um fator k.
    """
    
    # Obter a imagem da memória
    imagem = memory.getLastEdit()

    # Obter as dimensões da imagem
    linhas, colunas = imagem.shape[:2]

    # Criar uma cópia da imagem para edição
    imagem = imagem.copy()

    # Ajustar o contraste
    for x in range(linhas):
        for y in range(colunas):
            for c in range(imagem.shape[2]):  # Para cada canal de cor
                valor_original = imagem[x, y, c]
                valor_editado = valor_original + (valor_original * k / 100)
                imagem[x, y, c] = max(0, min(255, int(valor_editado)))  # Garantir valores válidos

    memory.addEdit(imagem)
