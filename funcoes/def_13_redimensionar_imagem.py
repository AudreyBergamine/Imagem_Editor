import cv2

def redimensionar_imagem(imagem, escala):
    """ Redimensiona a imagem de acordo com a escala fornecida."""
    
    # Obtém as dimensões originais da imagem
    largura = int(imagem.shape[1] * escala)
    altura = int(imagem.shape[0] * escala)
    dimensoes = (largura, altura)

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

    return imagem_redimensionada
   
