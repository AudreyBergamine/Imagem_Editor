import cv2
from .def_0_abrir_imagem import selecionar_imagem, abrir_imagem

# Operadores Morfológicos - Dilatação
# A dilatação é uma operação morfológica que adiciona pixels à borda de um objeto na imagem.
def dilatacao(imagem, kernel_size=(5, 5), iterations=2):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica o operador morfológico de dilatação
    imagem_dilatada = cv2.dilate(imagem, elemento_estruturante, iterations=iterations)
    
    return imagem_dilatada