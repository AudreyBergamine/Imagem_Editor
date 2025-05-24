import cv2

def inverter_cores(imagem):
    
    # Obtém o valor máximo de intensidade (255 para imagens em escala de cinza ou RGB)
    max_intensidade = 255

    # Inverte as cores da imagem
    imagem = max_intensidade - imagem

    return imagem