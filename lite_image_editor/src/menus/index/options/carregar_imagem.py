import os
from tkinter import Image, Tk, filedialog
from src.core.image_memory import ImageMemory
from src.core.menu import Option

class Carregar_Imagem(Option):
    def __init__(self, menu, memory: ImageMemory):
        super().__init__("Carregar Imagem", menu)
        self.memory = memory
    
    def executar(self):
        imagem = self.selecionar_imagem()
        self.memory.addImage(imagem)
        
        print(self.memory.fila)
    
    def selecionar_imagem(self):
        # Cria uma janela Tkinter oculta
        root = Tk()
        root.withdraw()

        # Abre a janela de seleção de arquivos
        file_path = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("Todos os arquivos", "*.*")
            ]
        )

        # Fecha a janela root
        root.destroy()

        if not file_path or not os.path.exists(file_path):
            return None

        try:
            imagem = Image.open(file_path)
            return imagem
        except Exception as e:
            print(f"Erro ao abrir a imagem: {e}")
            return None
