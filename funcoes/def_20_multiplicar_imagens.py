import cv2
from service.image_memory import ImageMemory


def multiplicar_imagens(memory: ImageMemory, mascara):
    """
    Multiplica uma imagem por uma máscara binária.
    """

    # Garantir que a máscara seja binária (0 e 1)
    mascara_binaria = (mascara > 0).astype("uint8")
    
    # Multiplicar a imagem pela máscara
    imagem_resultante = cv2.multiply(ImageMemory, mascara_binaria)
    
    return imagem_resultante