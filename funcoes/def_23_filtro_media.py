import cv2
from service.image_memory import ImageMemory

def filtro_media(memory: ImageMemory, kernel_size=(3, 3)):
    """ Aplica um filtro de média a uma imagem. """
    
    imagem = memory.getLastEdit()

    imagem_filtrada = cv2.blur(imagem, kernel_size)

    memory.addEdit(imagem_filtrada)
