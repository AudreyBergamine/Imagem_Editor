import tkinter as tk
from tkinter import ttk

class Editor(tk.Frame):
    def __init__(self, master, mudar_tela):
        super().__init__(master)
        self.mudar_tela = mudar_tela
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Editor de Imagem", font=("Arial", 18))
        label.pack(pady=20)

        btn_voltar = ttk.Button(self, text="Voltar ao Menu", command=lambda: self.mudar_tela("menu_principal"))
        btn_voltar.pack(pady=10)