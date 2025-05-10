import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def redimensionar_imagem(imagem, escala):
    
    # Obtém as dimensões originais da imagem
    largura = int(imagem.shape[1] * escala)
    altura = int(imagem.shape[0] * escala)
    dimensoes = (largura, altura)

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

    return imagem_redimensionada
   
