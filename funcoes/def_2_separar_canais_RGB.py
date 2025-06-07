import cv2

from service.image_memory import ImageMemory


def separar_canais_rgb(memory: ImageMemory):
    """ Separa os canais de cores RGB de uma imagem e exibe cada canal individualmente. """

    # Separa os canais de cores
    azul, verde, vermelho = cv2.split(memory.getLastEdit())

    # Exibe os canais separados
    cv2.imshow("Canal R", vermelho)
    cv2.imshow("Canal G", verde)
    cv2.imshow("Canal B", azul)

    # Salva os canais separados
    cv2.imwrite("Canal_R.jpeg", vermelho)
    cv2.imwrite("Canal_G.jpeg", verde)
    cv2.imwrite("Canal_B.jpeg", azul)

    return azul, verde, vermelho
