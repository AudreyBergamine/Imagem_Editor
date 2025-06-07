import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem

# Função para dividir duas imagens pixel a pixel
def dividir_imagens(memory: ImageMemory):
    """ Divide duas imagens pixel a pixel e retorna a imagem resultante. """
    
    imagem = memory.getLastEdit()
    
# Abrir as duas imagens
    imagem2 = selecionar_imagem()
    # Certifique-se de que as imagens têm o mesmo tamanho
    if imagem.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para divisão.")
    
    # Evitar divisão por zero adicionando um pequeno valor ao denominador
    imagem2 = imagem2.astype(float) + 1e-10
    
    # Realizar a divisão pixel a pixel
    imagem_resultante = cv2.divide(imagem.astype(float), imagem2)

    # Converter de volta para o tipo original
    imagem_resultante = cv2.convertScaleAbs(imagem_resultante)

    memory.addEdit(imagem_resultante)