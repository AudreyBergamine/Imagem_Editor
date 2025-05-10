import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem

def suavizar_imagem(imagem):
    # Aplicar suavização na imagem usando o filtro GaussianBlur
    imagem_suavizada = cv2.GaussianBlur(imagem, (13, 13), 3)
    return imagem_suavizada