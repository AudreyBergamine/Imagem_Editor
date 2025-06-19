import cv2
from service.image_memory import ImageMemory
from .def_0_abrir_imagem import abrir_imagem, selecionar_imagem
from tkinter import messagebox

def subtrair_imagens(memory: ImageMemory):
    """ Remove a última imagem adicionada (função Voltar), se houver. Caso contrário, mostra mensagem de orientação. """
    if len(memory.fila.images) > 1:
        memory.resetLastEdition()
    else:
        messagebox.showinfo("Atenção", "Para remover uma imagem, você precisa clicar em 'Adicionar Imagem' e selecionar uma imagem antes.")