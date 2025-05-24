import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def convert_RGB_to_HSV(imagem):
    
    # Converter a imagem de RGB para HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    return imagem_hsv