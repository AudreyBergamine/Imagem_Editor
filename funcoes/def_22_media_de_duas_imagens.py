import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

# Função para dividir duas imagens pixel a pixel

# Função para calcular a média de duas imagens
def media_de_duas_imagens(memory: ImageMemory):
    """ Calcula a média de duas imagens pixel a pixel e retorna a imagem resultante. """
    
    imagem = memory.getLastEdit()
    
    # Abrir a segunda imagem
    imagem2 = selecionar_imagem()
    # Verifica se as imagens foram carregadas corretamente
    if imagem is None or imagem2 is None:
        raise ValueError("Não foi possível carregar uma ou ambas as imagens.")
    # Certifique-se de que as imagens têm o mesmo tamanho
    if imagem.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para média.")
    # Calcular a média pixel a pixel de forma segura
    import numpy as np
    imagem_resultante = ((imagem.astype('float32') + imagem2.astype('float32')) / 2).astype(imagem.dtype)
    memory.addEdit(imagem_resultante)