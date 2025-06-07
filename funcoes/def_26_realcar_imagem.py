import cv2
from service.image_memory import ImageMemory

def realcar_imagem(memory: ImageMemory):
    """ Realça as cores de uma imagem. """

    # Converter a imagem de RGB para HSV
    imagem_hsv = cv2.cvtColor(ImageMemory, cv2.COLOR_BGR2HSV)
    
    # Definir os limites inferior e superior para o filtro de cor
    limite_inferior = (0, 0, 0)
    limite_superior = (255, 255, 255)
    
    # Aplicar o filtro de cor
    mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior)
    
    # Aplicar a máscara na imagem original
    imagem_realcada = cv2.bitwise_and(ImageMemory, ImageMemory, mask=mascara)
    
    return imagem_realcada
