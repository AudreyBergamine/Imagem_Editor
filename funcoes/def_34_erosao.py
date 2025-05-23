import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

# Operadores Morfológicos - Erosão
# A erosão é uma operação morfológica que remove pixels de borda de um objeto na imagem.
def erosao(imagem, kernel_size=(5, 5), iterations=1):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica a erosão na imagem
    imagem_processada = cv2.erode(imagem, elemento_estruturante, iterations=iterations)
    
    return imagem_processada