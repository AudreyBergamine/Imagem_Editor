import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

def adicionar_imagens(memory: ImageMemory):
    
    # Abrir as duas imagens
    img2 = selecionar_imagem()

    # Verificar se as imagens foram carregadas corretamente
    if ImageMemory is None or img2 is None:
        raise ValueError("Uma ou ambas as imagens não foram carregadas corretamente.")

    # Realizar a adição das imagens
    img_resultado = cv2.add(ImageMemory, img2)

    # Retornar a imagem resultante
    return img_resultado
