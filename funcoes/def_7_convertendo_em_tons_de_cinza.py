import cv2

# Função para converter uma imagem colorida em tons de cinza
def convertendo_em_tons_de_cinza(imagem):
    
    # Converter a imagem para tons de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return imagem_cinza
