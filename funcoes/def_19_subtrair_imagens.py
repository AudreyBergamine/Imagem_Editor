import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def subtrair_imagens(imagem1, imagem2):
    
    # Abrir as duas imagens
    img1 = abrir_imagem(imagem1)
    img2 = abrir_imagem(imagem2)

    # Subtrair as duas imagens
    img_subtraida = cv2.subtract(img1, img2)
    
    
    return img_subtraida