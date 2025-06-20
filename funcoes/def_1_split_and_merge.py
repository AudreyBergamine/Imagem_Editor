import cv2

from service.image_memory import ImageMemory

def split_and_merge(memory: ImageMemory):
    """
    Realiza a separação e junção de canais de uma imagem.
    Permite realizar alterações nos canais antes de juntá-los novamente.
    """
    # Converte para o espaço de cores HSV
    imagem_hsv = cv2.cvtColor(memory.getLastEdit(), cv2.COLOR_BGR2HSV)

    # Realiza separação de canais HSV
    matiz, saturacao, valor = cv2.split(imagem_hsv)

    # Aqui você pode realizar alterações nos canais individualmente
    # Exemplo: inverter o canal de matiz
    matiz = cv2.bitwise_not(matiz)

    # Realiza junção dos canais HSV
    imagem_hsv_modificada = cv2.merge((matiz, saturacao, valor))
    # cv2.imshow("Imagem junção canais HSV", imagem_hsv_modificada)

    # Converte de volta para o espaço de cores BGR
    imagem_resultado = cv2.cvtColor(imagem_hsv_modificada, cv2.COLOR_HSV2BGR)
    # cv2.imshow("Imagem HSV para RGB", imagem_resultado)
    
    memory.addEdit(imagem_resultado)
