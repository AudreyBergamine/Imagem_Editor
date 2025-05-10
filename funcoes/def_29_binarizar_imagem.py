import cv2

def binarizar_imagem(imagem, limiar):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Aplicar a binarização
    _, imagem_binarizada = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)
    return imagem_binarizada
    
  