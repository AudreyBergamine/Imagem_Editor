import cv2
from service.image_memory import ImageMemory
from tkinter import messagebox
import numpy as np

def dividir_imagens(memory: ImageMemory):
    """
    Divide pixel a pixel a última imagem adicionada na fila por ela mesma.
    O resultado é normalizado para o intervalo [0, 255].
    """
    if len(memory.fila.images) < 1:
        messagebox.showinfo("Atenção", "É necessário adicionar pelo menos 1 imagem para dividir por ela mesma.")
        return

    imagem = memory.fila.images[-1]

    # Evitar divisão por zero
    imagem_float = imagem.astype(np.float32)
    imagem_float[imagem_float == 0] = 1e-10

    resultado_float = imagem.astype(np.float32) / imagem_float
    dst = np.empty_like(resultado_float)
    resultado_norm = cv2.normalize(resultado_float, dst, 0, 255, cv2.NORM_MINMAX)
    imagem_resultante = resultado_norm.astype(np.uint8)

    memory.addEdit(imagem_resultante)
    return imagem_resultante