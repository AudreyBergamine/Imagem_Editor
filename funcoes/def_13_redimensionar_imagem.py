import cv2
from service.image_memory import ImageMemory

def redimensionar_imagem(memory: ImageMemory, escala):
    """ Redimensiona a imagem de acordo com a escala fornecida."""

    imagem = memory.getLastEdit()

    # Obtém as dimensões originais da imagem
    largura = int(imagem.shape[1] * escala)
    altura = int(imagem.shape[0] * escala)
    dimensoes = (largura, altura)

    # Redimensiona a imagem
    imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
    memory.addEdit(imagem_redimensionada)
    
    return imagem_redimensionada
   
