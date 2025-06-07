import cv2

from service.image_memory import ImageMemory

def convert_RGB_to_HSV(memory: ImageMemory):
    """ Converte uma imagem de RGB para HSV. """
    
    # Converter a imagem de RGB para HSV
    imagem_hsv = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2HSV)
    
    memory.addEdit(imagem_hsv)