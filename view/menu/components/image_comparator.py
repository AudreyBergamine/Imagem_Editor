import tkinter as tk
from PIL import Image, ImageTk

class ImageComparator(tk.Frame):
    def __init__(self, parent, img_before=None, img_after=None):
        super().__init__(parent)
        
        self.img_before = img_before  
        self.img_after = img_after
        
        self.configure(bg="red")

        # Criando os rótulos para exibir as imagens
        self.label_before = tk.Label(self, text="Imagem Anterior", compound="top")
        self.label_after = tk.Label(self, text="Imagem Atual", compound="top")

        self.label_before.pack(side="left", expand=True, padx=10, pady=10)
        self.label_after.pack(side="right", expand=True, padx=10, pady=10)

        # Atualiza as imagens se forem passadas
        if self.img_before:
            self.update_image_before(self.img_before)
        if self.img_after:
            self.update_image_after(self.img_after)

    def update_image_before(self, image):
        """Atualiza a imagem anterior"""
        image = image.resize((300, 300))  # Ajusta o tamanho
        self.img_before_tk = ImageTk.PhotoImage(image)
        self.label_before.config(image=self.img_before_tk)

    def update_image_after(self, image):
        """Atualiza a imagem atual"""
        image = image.resize((300, 300))  # Ajusta o tamanho
        self.img_after_tk = ImageTk.PhotoImage(image)
        self.label_after.config(image=self.img_after_tk)
