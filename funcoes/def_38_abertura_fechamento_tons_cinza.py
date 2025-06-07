import cv2
from service.image_memory import ImageMemory

def abertura_fechamento_tons_cinza(memory: ImageMemory):
    """
    Aplica operações de abertura e fechamento em uma imagem em tons de cinza."""
    
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    
    # Aplica a operação de abertura
    imagem_abertura = cv2.morphologyEx(ImageMemory, cv2.MORPH_OPEN, elemento_estruturante)
    
    # Aplica a operação de fechamento
    imagem_fechamento = cv2.morphologyEx(imagem_abertura, cv2.MORPH_CLOSE, elemento_estruturante)
    
    return imagem_fechamento
