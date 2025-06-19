import cv2
import numpy as np
from service.image_memory import ImageMemory


def multiplicar_imagens(memory: ImageMemory, mascara=None):
    """
    Multiplica uma imagem por uma máscara binária.
    Se nenhuma máscara for fornecida, cria uma máscara padrão.
    """
    
    imagem = memory.getLastEdit()

    # Se nenhuma máscara for fornecida, criar uma máscara padrão
    if mascara is None:
        # Criar uma máscara circular no centro da imagem
        altura, largura = imagem.shape[:2]
        mascara = np.zeros((altura, largura), dtype=np.uint8)
        centro_y, centro_x = altura // 2, largura // 2
        raio = min(altura, largura) // 4
        cv2.circle(mascara, (centro_x, centro_y), raio, (255, 255, 255), -1)
        mascara = cv2.cvtColor(mascara, cv2.COLOR_GRAY2BGR)

    # Garantir que a máscara seja binária (0 e 1)
    mascara_binaria = (mascara > 0).astype("uint8")
    
    # Multiplicar a imagem pela máscara
    imagem_resultante = cv2.multiply(imagem, mascara_binaria)

    memory.addEdit(imagem_resultante)