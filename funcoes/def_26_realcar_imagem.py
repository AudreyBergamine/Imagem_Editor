import cv2
import numpy as np
from service.image_memory import ImageMemory

def realcar_imagem(memory: ImageMemory):
    """ Realça as cores de uma imagem aumentando a saturação. """
    
    imagem = memory.getLastEdit()

    # Converter a imagem de BGR para HSV
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Aumentar a saturação
    h, s, v = cv2.split(imagem_hsv)
    s = np.clip(s.astype(np.int16) + 50, 0, 255).astype(np.uint8)  # Aumenta a saturação em 50
    imagem_hsv_realcada = cv2.merge([h, s, v])

    # Converter de volta para BGR
    imagem_realcada = cv2.cvtColor(imagem_hsv_realcada, cv2.COLOR_HSV2BGR)

    memory.addEdit(imagem_realcada)
