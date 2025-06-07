import tkinter as tk
from tkinter import ttk
from service.image_memory import ImageMemory
from view.menu.components.image_comparator import ImageComparator
from view.menu.components.menu_principal.side_menu import Side_menu
from view.menu.components.menu_principal.tools_bar import ToolsBar


class MenuPrincipal(tk.Frame):
    def __init__(self, master, app, mudar_tela):
        super().__init__(master)
        self.mudar_tela = mudar_tela
        self.app = app

        self.background_color = "#555"
        self.border_color = "#333"

        self.configure(background=self.background_color, highlightbackground=self.border_color, highlightthickness=0)

        self.create_widgets()
        
    def create_widgets(self):
        
        side_menu = Side_menu(self)
        side_menu.pack(side="left", fill="y")
        
        toolsBar = ToolsBar(self, [])
        toolsBar.pack() 
        
        image_comparator = ImageComparator(master=self,app= self.app)
        image_comparator.pack(fill="both", expand=True)
    
        def voltar_edicao():
            memory: ImageMemory = self.app.memory
            memory.resetLastEdition()
            self.app.trocar_tela('menu_principal')
        
        buttonReet = tk.Button(toolsBar, text="Voltar edição", command=voltar_edicao)
        buttonReet.pack(fill="none", expand=False)
        
        
    def __str__(self):
        return "Menu Principal"