import cv2

def converter_modelos_cor(imagem):
    """
    Converte uma imagem para diferentes modelos de cor.
    """

    # Converte a imagem para diferentes modelos de cor
    imagemNC = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagemCrCb = cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    imagemLab = cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)
    imagemHSV = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Exibe as imagens convertidas
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem em Escala de Cinza (NC)', imagemNC)
    cv2.imshow('Imagem em YCrCb', imagemCrCb)
    cv2.imshow('Imagem em LAB', imagemLab)
    cv2.imshow('Imagem em HSV', imagemHSV)


    return {
        "NC": imagemNC,
        "YCrCb": imagemCrCb,
        "LAB": imagemLab,
        "HSV": imagemHSV
    }
