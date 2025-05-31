import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


import menu_select as ms

from src.core.image_memory import ImageMemory
from src.menus.index.index import Menu_index

class main:
    def __init__(self):
        self.cabeçalho = "Sistema de análise e edição de imagem com IA"
        self.menu = ms.Menu_select(self.cabeçalho)
        self.image_memory = ImageMemory()

        
        Menu_index(self.menu, self.image_memory).executar()
        
main()