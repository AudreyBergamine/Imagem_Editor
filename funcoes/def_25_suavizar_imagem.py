import cv2
from service.image_memory import ImageMemory

def suavizar_imagem(memory: ImageMemory):
    """
    Aplica suavização a uma imagem.
    """

    # Aplicar suavização na imagem usando o filtro GaussianBlur
    imagem_suavizada = cv2.GaussianBlur(ImageMemory, (13, 13), 3)
    return imagem_suavizada