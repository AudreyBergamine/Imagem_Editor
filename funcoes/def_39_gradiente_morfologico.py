import cv2

def gradiente_morfologico(imagem):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    
    # Aplica o gradiente morfológico
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_GRADIENT, elemento_estruturante)
    
    return imagem_processada
