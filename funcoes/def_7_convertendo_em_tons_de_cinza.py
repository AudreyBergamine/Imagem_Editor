import cv2

from service.image_memory import ImageMemory

# Função para converter uma imagem colorida em tons de cinza
def convertendo_em_tons_de_cinza(memory: ImageMemory):
    
    # Converter a imagem para tons de cinza
    imagem_cinza = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2GRAY)
    memory.addImage(imagem_cinza)
