import cv2

def filtro_media(imagem, kernel_size=(3, 3)):

    imagem_filtrada = cv2.blur(imagem, kernel_size)
    return imagem_filtrada

  