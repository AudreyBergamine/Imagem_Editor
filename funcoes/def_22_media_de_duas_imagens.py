import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

# Função para dividir duas imagens pixel a pixel

# Função para calcular a média de duas imagens
def media_de_duas_imagens(memory: ImageMemory):
    """ Calcula a média de duas imagens pixel a pixel e retorna a imagem resultante. """
    
    imagem = memory.getLastEdit()
    
    # Abrir as duas imagens
    imagem2 = selecionar_imagem()
    # Certifique-se de que as imagens têm o mesmo tamanho
    if imagem.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para média.")
    # Calcular a média pixel a pixel
    imagem_resultante = cv2.addWeighted(imagem, 0.5, imagem2, 0.5, 0)
    return imagem_resultante