import cv2
from service.image_memory import ImageMemory
from tkinter import messagebox


def multiplicar_imagens(memory: ImageMemory):
    """
    Multiplica pixel a pixel a última imagem adicionada na fila por ela mesma.
    """
    if len(memory.fila.images) < 1:
        messagebox.showinfo("Atenção", "É necessário adicionar pelo menos 1 imagem para multiplicar por ela mesma.")
        return

    imagem = memory.fila.images[-1]

    imagem_resultante = cv2.multiply(imagem, imagem)
    memory.addEdit(imagem_resultante)
    return imagem_resultante