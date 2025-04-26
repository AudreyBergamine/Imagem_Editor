import tkinter as tk
from configuration.configuration import Configuration


class IconButton(tk.Button):
    def __init__(self, master, image_path, text="", command=None, background_color="black", text_color="white"):
        self.image_path = image_path
        self.command = command
        self.background_color = background_color
        self.text_color = text_color

        self.size = Configuration.icon_size
        
        # Carregar a imagem
        self.image = tk.PhotoImage(file=image_path)
        # Redimensionar a imagem para o tamanho de um ícone pequeno
        self.image = self.image.zoom(1, 1)  # Reset zoom
        self.image = self.image.subsample(max(self.image.width() // self.size, 1), max(self.image.height() // self.size, 1))  # Ajuste para 32x32 pixels
        
        super().__init__(master, image=self.image, command=self.command, borderwidth=0, text=text, compound="top")
        
        self.config(compound="left", padx=5, pady=5, relief="flat", bg=self.background_color, foreground=self.text_color, font=("Arial", 10))