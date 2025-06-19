import cv2
from service.image_memory import ImageMemory

def espaco_de_cores_YCrCb(memory: ImageMemory):
    """ Converte uma imagem para o espaço de cores YCrCb e extrai seus canais. """

    # Converter a imagem para o espaço de cores YCrCb
    imagemYCrCb = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2YCrCb)
    
    # Extrair os canais Y, Cr e Cb
    canal_Y, canal_Cr, canal_Cb = cv2.split(imagemYCrCb)
    
    memory.addEdit(imagemYCrCb)
    return imagemYCrCb, canal_Y, canal_Cr, canal_Cb