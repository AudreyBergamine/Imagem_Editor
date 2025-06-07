import cv2
from service.image_memory import ImageMemory

#  Realça objetos brilhantes em fundos escuros
#  e objetos escuros em fundos claros.
#  O operador Top Hat é útil para destacar objetos que são mais brilhantes do que o fundo.
def top_hat(memory: ImageMemory, kernel_size=(25, 25)):
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica o operador morfológico Top Hat
    imagem_processada = cv2.morphologyEx(ImageMemory, cv2.MORPH_TOPHAT, elemento_estruturante)
    
    # Ajusta o contraste
    imagem_tratada = cv2.add(imagem_processada, imagem_processada)
    
    return imagem_processada, imagem_tratada