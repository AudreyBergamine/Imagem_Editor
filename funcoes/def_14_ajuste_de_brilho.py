import cv2

def ajuste_de_brilho(imagem, k):
    """ Ajusta o brilho de uma imagem adicionando um valor k a cada pixel."""
    
    # Obter as dimensões da imagem
    linhas, colunas = imagem.shape[:2]

    # Criar uma cópia da imagem para edição
    imagem = imagem.copy()

    # Ajustar o brilho
    for x in range(linhas):
        for y in range(colunas):
            for c in range(imagem.shape[2]):  # Para cada canal de cor
                imagem[x, y, c] = min(max(imagem[x, y, c] + k, 0), 255)

    return imagem
