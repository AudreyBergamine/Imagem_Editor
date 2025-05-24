import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def adicionar_imagens(imagem1, imagem2):
    
    # Abrir as duas imagens
    img1 = abrir_imagem(imagem1)
    img2 = abrir_imagem(imagem2)

    # Verificar se as imagens foram carregadas corretamente
    if img1 is None or img2 is None:
        raise ValueError("Uma ou ambas as imagens não foram carregadas corretamente.")

    # Realizar a adição das imagens
    img_resultado = cv2.add(img1, img2)

    # Retornar a imagem resultante
    return img_resultado
