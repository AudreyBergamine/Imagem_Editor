import cv2

def convert_HSV_to_RGB(imagem):

    # Converter de HSV para RGB
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)
    
    return imagem_rgb