import cv2
from service.image_memory import ImageMemory

# Operadores Morfológicos - Erosão
# A erosão é uma operação morfológica que remove pixels de borda de um objeto na imagem.
def erosao(memory: ImageMemory, kernel_size=(5, 5), iterations=1):
    """ Aplica a erosão a uma imagem usando um elemento estruturante definido. """
    
    imagem = memory.getLastEdit()
    
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    
    # Aplica a erosão na imagem
    imagem_processada = cv2.erode(imagem, elemento_estruturante, iterations=iterations)

    memory.addEdit(imagem_processada)