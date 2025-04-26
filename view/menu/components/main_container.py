import tkinter as tk

class main_container(tk.Frame):
    
    def __init__(self, parent, mudar_tela):
        super().__init__(parent)
        self.mudar_tela = mudar_tela
        
        