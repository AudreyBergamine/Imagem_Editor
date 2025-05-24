import cv2

def convert_RGB_to_HSV(imagem):
    
    # Converter a imagem de RGB para HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    return imagem_hsv