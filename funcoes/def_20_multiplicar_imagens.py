import cv2
from service.image_memory import ImageMemory
from tkinter import messagebox


def multiplicar_imagens(memory: ImageMemory):
    """
    Multiplica pixel a pixel as duas últimas imagens da fila e adiciona o resultado na memória.
    """
    if len(memory.fila.images) < 2:
        messagebox.showinfo("Atenção", "É necessário adicionar pelo menos mais 1 imagen para multiplicar.")
        return
    imagem_A = memory.fila.images[-2]
    imagem_B = memory.fila.images[-1]
    imagem_resultante = cv2.multiply(imagem_A, imagem_B)
    memory.addEdit(imagem_resultante)