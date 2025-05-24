import cv2

#  Eliminação de ruídos
# Função para eliminar ruídos em uma imagem usando morfologia matemática
# Esta função aplica uma operação de abertura para remover pequenos ruídos na imagem
def eliminacao_ruidos(imagem):
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    
    # Aplica a operação de abertura para eliminar ruídos
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)
    
    return imagem_processada