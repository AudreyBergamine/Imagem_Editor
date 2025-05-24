import cv2

def espaco_de_cor_LAB(imagem):
    """
    Converte a imagem de BGR para o espaço de cor LAB.
    
    Parâmetros:
    imagem (numpy.ndarray): Imagem em formato BGR.
    
    Retorna:
    numpy.ndarray: Imagem convertida para o espaço de cor LAB.
    """
    imagem_LAB = cv2.cvtColor(imagem, cv2.COLOR_BGR2Lab)
    
    return imagem_LAB