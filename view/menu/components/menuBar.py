import tkinter as tk
from tkinter import messagebox
from funcoes.def_0_abrir_imagem import abrir_imagem, selecionar_imagem

class MenuBar(tk.Menu):     
    def __init__(self, parent):
        super().__init__(parent)

        self.app = parent

        # Menu "Arquivo"
        menu_arquivo = tk.Menu(self, tearoff=0)
        menu_arquivo.add_command(label="Novo", command=self.novo_arquivo)
        menu_arquivo.add_command(label="Carregar Imagem", command=self.abrir_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=parent.quit)

        # Menu "Opções"
        menu_opcoes = tk.Menu(self, tearoff=0)
        menu_opcoes.add_command(label="Configurações", command=self.configuracoes)

        # Menu "Ajuda"
        menu_ajuda = tk.Menu(self, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.sobre)

        # Adicionando os menus na barra de menu
        self.add_cascade(label="Arquivo", menu=menu_arquivo)
        self.add_cascade(label="Opções", menu=menu_opcoes)
        self.add_cascade(label="Ajuda", menu=menu_ajuda)

    def novo_arquivo(self):
        messagebox.showinfo("Novo", "Criando um novo arquivo...")

    def abrir_arquivo(self):
        imagem = selecionar_imagem()
        if imagem is not None:
            self.app.imagem_original = imagem
            self.app.memory.addImage(self.app.imagem_original)
            self.app.trocar_tela('menu_principal')
        else:
            messagebox.showinfo("Abrir", "Erro")

    def configuracoes(self):
        messagebox.showinfo("Configurações", "Abrindo configurações...")

    def sobre(self):
        messagebox.showinfo("Sobre", "Imagem Editor v1.0\nDesenvolvido por Você!")
