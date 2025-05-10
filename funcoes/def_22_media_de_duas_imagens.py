import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

# Função para dividir duas imagens pixel a pixel

# Função para calcular a média de duas imagens
def media_de_duas_imagens(imagem1, imagem2):
    # Abrir as duas imagens
    imagem1 = abrir_imagem(imagem1)
    imagem2 = abrir_imagem(imagem2)
    # Certifique-se de que as imagens têm o mesmo tamanho
    if imagem1.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para média.")
    # Calcular a média pixel a pixel
    imagem_resultante = cv2.addWeighted(imagem1, 0.5, imagem2, 0.5, 0)
    return imagem_resultante