import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem


def multiplicar_imagens(imagem, mascara):

    # Garantir que a máscara seja binária (0 e 1)
    mascara_binaria = (mascara > 0).astype("uint8")
    
    # Multiplicar a imagem pela máscara
    imagem_resultante = cv2.multiply(imagem, mascara_binaria)
    
    return imagem_resultante