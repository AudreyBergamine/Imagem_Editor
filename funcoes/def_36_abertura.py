import cv2

# Operadores Morfológicos - Abertura
# A abertura é uma operação morfológica que remove pequenos objetos da imagem.
def abertura(imagem):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    
    # Aplica o operador morfológico de abertura
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)
    
    return imagem_processada