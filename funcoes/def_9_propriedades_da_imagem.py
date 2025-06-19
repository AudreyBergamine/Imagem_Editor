import cv2
from service.image_memory import ImageMemory
import tkinter as tk
from tkinter import messagebox

def propriedades_da_imagem(memory: ImageMemory):
    """
    Obtém e exibe as propriedades de uma imagem.
    """
    imagem = memory.getLastEdit()
    propriedades = {
        "Altura": imagem.shape[0],
        "Largura": imagem.shape[1],
        "Canais": imagem.shape[2]
    }
    texto = "\n".join([f"{k}: {v}" for k, v in propriedades.items()])
    # Sempre cria um root oculto para garantir o messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Propriedades da Imagem", texto)
    root.destroy()
    return propriedades

def mostrar_propriedades_da_imagem(memory, master=None):
    props = propriedades_da_imagem(memory)
    texto = f"Altura: {props['Altura']} px\nLargura: {props['Largura']} px\nCanais: {props['Canais']}"
    messagebox.showinfo("Propriedades da Imagem", texto, parent=master)


