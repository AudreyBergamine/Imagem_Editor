import cv2

from service.image_memory import ImageMemory

def convert_HSV_to_RGB(memory: ImageMemory):

    # Converter de HSV para RGB
    imagem_rgb = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_HSV2BGR)
    
    return imagem_rgb