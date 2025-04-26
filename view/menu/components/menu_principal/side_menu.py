import tkinter as tk
from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame

class Side_menu(RoundedFrame):
    def __init__(self, master):
        super().__init__(master, 
                        bg_color="#555",
                        border_color="black",
                        corner_radius=20,
                        width=Configuration.side_menu_width,
                        height=Configuration.side_menu_height,
                        highlightthickness=0)
        
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        # Frame interno para conter os widgets
        self.inner_frame = tk.Frame(self, bg="#555")
        self.create_window(250, 100, window=self.inner_frame, anchor="center")
        
        # Criando os botões do menu lateral
        self.opcao1 = IconButton(self.inner_frame, 
                                image_path="view/static/images/engrenagem.png", 
                                text="Opção 1", 
                                command=self.show_menu_principal, 
                                background_color="#555")
        self.opcao1.pack(padx=5, pady=5)
        
    def show_menu_principal(self):
        pass
    
    def show_editor(self):
        pass