import cv2
from def_0_abrir_imagem import selecionar_imagem, abrir_imagem


def separar_canais_rgb(imagem):

    # Separa os canais de cores
    azul, verde, vermelho = cv2.split(imagem)

    # Exibe os canais separados
    cv2.imshow("Canal R", vermelho)
    cv2.imshow("Canal G", verde)
    cv2.imshow("Canal B", azul)

    # Salva os canais separados
    cv2.imwrite("Canal_R.jpeg", vermelho)
    cv2.imwrite("Canal_G.jpeg", verde)
    cv2.imwrite("Canal_B.jpeg", azul)

    return azul, verde, vermelho
