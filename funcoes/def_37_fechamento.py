import cv2

# Operadores Morfológicos - Fechamento
# O fechamento é uma operação morfológica que preenche pequenos buracos em objetos na imagem.
def fechamento(imagem, kernel_size=(5, 5), iterations=1):
    # Define o elemento estruturante
    elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)

    # Aplica o operador morfológico de fechamento
    imagem_processada = cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, elemento_estruturante)

    return imagem_processada