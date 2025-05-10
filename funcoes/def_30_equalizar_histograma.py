import cv2

def equalizar_histograma(imagem):
    
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Aplicar a equalização de histograma
    imagem_equalizada = cv2.equalizeHist(imagem_cinza)
    
    return imagem_equalizada
  