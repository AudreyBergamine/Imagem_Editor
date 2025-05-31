import menu_select as ms

from src.menus.index.options.carregar_imagem import Carregar_Imagem
from src.menus.index.options.sair import Sair
from src.core.image_memory import ImageMemory
from src.core.menu import Menu

class Menu_index(Menu):
    
    def __init__(self, menu: ms.Menu_select, memory: ImageMemory):
        super().__init__(menu, "Menu principal", "Bem vindo ao programa")
        self.memory = memory
    
    def executar(self):
        
        opcoes = [
            Carregar_Imagem(self.menu, self.memory), 
            Sair(menu=self.menu)
        ]
        
        self.abrir_menu(opcoes=opcoes)
        
    