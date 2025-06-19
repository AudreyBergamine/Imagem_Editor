import cv2
from service.image_memory import ImageMemory

def ajuste_de_contraste(memory: ImageMemory, k=30):
    """
    Ajusta o contraste de uma imagem multiplicando cada pixel por um fator k.
    k é o percentual de ajuste (ex: 30 aumenta 30%, -30 diminui 30%).
    """
    
    # Obter a imagem da memória
    imagem = memory.getLastEdit()

    # Obter as dimensões da imagem
    linhas, colunas = imagem.shape[:2]

    # Criar uma cópia da imagem para edição
    imagem = imagem.copy()

    fator = 1 + (k / 100)
    for x in range(linhas):
        for y in range(colunas):
            for c in range(imagem.shape[2]):  # Para cada canal de cor
                valor_original = imagem[x, y, c]
                valor_editado = valor_original * fator
                imagem[x, y, c] = max(0, min(255, int(valor_editado)))  # Garantir valores válidos

    memory.addEdit(imagem)
