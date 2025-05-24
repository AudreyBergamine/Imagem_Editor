import cv2

def abertura_fechamento_tons_cinza(imagem):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    
    # Aplica a operação de abertura
    imagem_abertura = cv2.morphologyEx(imagem, cv2.MORPH_OPEN, elemento_estruturante)
    
    # Aplica a operação de fechamento
    imagem_fechamento = cv2.morphologyEx(imagem_abertura, cv2.MORPH_CLOSE, elemento_estruturante)
    
    return imagem_fechamento
