import tkinter as tk
from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame

class Side_menu(RoundedFrame):
    def __init__(self, master):
        super().__init__(master, 
                        bg_color=Configuration.side_background_color,
                        border_color="black",
                        corner_radius=20,
                        width=Configuration.side_menu_width,
                        height=Configuration.side_menu_height,
                        highlightthickness=0)
        
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        # Frame interno para conter os widgets
        self.inner_frame = tk.Frame(self, bg=Configuration.side_background_color, width=Configuration.side_menu_width - 20, height=Configuration.side_menu_height - 20)
        self.inner_frame.pack_propagate(False)  # Impede que o frame redimensione automaticamente
        self.create_window(Configuration.side_menu_width // 2, Configuration.side_menu_height // 2, window=self.inner_frame, anchor="center")
        
        # Criando os botões do menu lateral
        self.opcao1 = IconButton(self.inner_frame, 
                    image_path="view/static/images/engrenagem.png", 
                    text="Opção 1", 
                    command=self.show_menu_principal, 
                    background_color="#555", 
                    text_color="white")
        self.opcao1.pack(side="top")
        
        # Criando os botões do menu lateral
        self.opcao2 = IconButton(self.inner_frame, 
                    image_path="view/static/images/engrenagem.png", 
                    text="Escalas de cinza", 
                    command=self.show_menu_principal, 
                    background_color="#555", 
                    text_color="white")
        self.opcao2.pack(side="top")
        
    def show_menu_principal(self):
        pass
    
    def show_editor(self):
        pass