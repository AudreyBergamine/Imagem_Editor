import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

def subtrair_imagens(memory: ImageMemory):
    """ Subtrai duas imagens pixel a pixel e retorna a imagem resultante. """
    
    # Abrir as duas imagens
    img2 = selecionar_imagem()

    # Subtrair as duas imagens
    img_subtraida = cv2.subtract(ImageMemory, img2)
    
    
    return img_subtraida