import os
import sys
from tkinter import Image, Tk, filedialog

import cv2
from src.core.image_memory import ImageMemory
from src.core.menu import Option

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Carregar_Imagem(Option):
    def __init__(self, menu, memory: ImageMemory):
        super().__init__("Carregar Imagem", menu)
        self.memory = memory
    
    def executar(self):
        imagem = self.selecionar_imagem()
        self.memory.addImage(imagem)
        
        print(self.memory.fila)
    
    def listar_imagens(self, diretorio=os.listdir(f'{__file__}/../../../../../')):
        """Lista os arquivos de imagem no diretório especificado (padrão: diretório atual)."""
        extensoes_imagem = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
        return [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f)) and os.path.splitext(f)[1].lower() in extensoes_imagem]

    def selecionar_imagem(self):
        
        print(self.listar_imagens())
        
        options = self.listar_imagens() + ["Voltar"]
        
        print("Opções")
        print(options)
        exit(1)
        select = self.menu.options(opções=options)

        if options[select] == "Voltar":
            return None
        
        imagem = cv2.imread(options[select])
        return imagem


