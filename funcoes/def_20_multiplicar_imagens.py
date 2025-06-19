import cv2
from service.image_memory import ImageMemory
from tkinter import messagebox


def multiplicar_imagens(memory: ImageMemory):
    """
    Multiplica pixel a pixel as duas últimas imagens adicionadas na fila.
    A imagem B deve ser adicionada por último (usando 'Adicionar Imagem').
    """
    if len(memory.fila.images) < 2:
        messagebox.showinfo("Atenção", "É necessário adicionar pelo menos mais 1 imagem para multiplicar.")
        return

    imagem_A = memory.fila.images[-2]
    imagem_B = memory.fila.images[-1]

    # Verifica se as imagens têm o mesmo shape
    if imagem_A.shape != imagem_B.shape:
        messagebox.showinfo("Erro", "As imagens devem ter o mesmo tamanho e número de canais para multiplicar.")
        return

    imagem_resultante = cv2.multiply(imagem_A, imagem_B)
    memory.addEdit(imagem_resultante)