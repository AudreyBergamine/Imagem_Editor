import cv2
from service.image_memory import ImageMemory

def inverter_cores(memory: ImageMemory):
    """
    Inverte as cores de uma imagem.
    """

    # Obtém o valor máximo de intensidade (255 para imagens em escala de cinza ou RGB)
    max_intensidade = 255

    # Inverte as cores da imagem
    ImageMemory = max_intensidade - ImageMemory

    return ImageMemory