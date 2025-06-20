import cv2
from service.image_memory import ImageMemory

def binarizar_imagem(memory: ImageMemory, limiar):
    """
    Binariza uma imagem em tons de cinza usando um limiar.
    """
    
    imagem = memory.getLastEdit()

    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Aplicar a binarização
    _, imagem_binarizada = cv2.threshold(imagem_cinza, limiar, 255, cv2.THRESH_BINARY)

    memory.addEdit(imagem_binarizada)
