import cv2
from .def_0_abrir_imagem import abrir_imagem

# Função para dividir duas imagens pixel a pixel
def dividir_imagens(imagem1, imagem2):
# Abrir as duas imagens
    imagem1 = abrir_imagem(imagem1)
    imagem2 = abrir_imagem(imagem2)
    # Certifique-se de que as imagens têm o mesmo tamanho
    if imagem1.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para divisão.")
    
    # Evitar divisão por zero adicionando um pequeno valor ao denominador
    imagem2 = imagem2.astype(float) + 1e-10
    
    # Realizar a divisão pixel a pixel
    imagem_resultante = cv2.divide(imagem1.astype(float), imagem2)
    
    # Converter de volta para o tipo original
    imagem_resultante = cv2.convertScaleAbs(imagem_resultante)
    
    return imagem_resultante