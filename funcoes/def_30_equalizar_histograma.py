import cv2
from service.image_memory import ImageMemory

def equalizar_histograma(memory: ImageMemory):
    """ Aplica a equalização de histograma a uma imagem em escala de cinza. """
    
    imagem = memory.getLastEdit()
    
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar a equalização de histograma
    imagem_equalizada = cv2.equalizeHist(imagem_cinza)
    
    return imagem_equalizada
  