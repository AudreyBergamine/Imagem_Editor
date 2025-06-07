import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import selecionar_imagem, abrir_imagem

# Operadores Morfológicos - Dilatação
# A dilatação é uma operação morfológica que adiciona pixels à borda de um objeto na imagem.
def dilatacao(memory: ImageMemory, kernel_size=(5, 5), iterations=2):
    """ Aplica a dilatação a uma imagem usando um elemento estruturante definido. """
    
    imagem = memory.getLastEdit()
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica o operador morfológico de dilatação
    imagem_dilatada = cv2.dilate(imagem, elemento_estruturante, iterations=iterations)

    memory.addEdit(imagem_dilatada)