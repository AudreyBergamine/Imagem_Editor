import cv2

def realcar_imagem(imagem):
    
    # Converter a imagem de RGB para HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    # Definir os limites inferior e superior para o filtro de cor
    limite_inferior = (0, 0, 0)
    limite_superior = (255, 255, 255)
    
    # Aplicar o filtro de cor
    mascara = cv2.inRange(imagem_hsv, limite_inferior, limite_superior)
    
    # Aplicar a máscara na imagem original
    imagem_realcada = cv2.bitwise_and(imagem, imagem, mask=mascara)
    
    return imagem_realcada
