import cv2

def suavizar_imagem(imagem):
    # Aplicar suavização na imagem usando o filtro GaussianBlur
    imagem_suavizada = cv2.GaussianBlur(imagem, (13, 13), 3)
    return imagem_suavizada