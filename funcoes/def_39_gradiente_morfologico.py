import cv2
from service.image_memory import ImageMemory

def gradiente_morfologico(memory: ImageMemory):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    
    # Aplica o gradiente morfológico
    imagem_processada = cv2.morphologyEx(ImageMemory, cv2.MORPH_GRADIENT, elemento_estruturante)
    
    return imagem_processada
