import tkinter as tk
from view.menu.components.IconButton import IconButton
from configuration.configuration import Configuration
from view.menu.components.RoundedFrame import RoundedFrame

class ToolsBar(RoundedFrame):
    def __init__ (self, master, widgets):
        super().__init__(master, 
                bg_color=Configuration.tools_bar_background_color,
                border_color="black",
                corner_radius=20,
                width=master.winfo_screenwidth(),
                height=150,
                highlightthickness=0)
        
        self.master = master
        self.widgets = widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Frame interno para conter os widgets
        self.inner_frame = tk.Frame(self, bg=Configuration.side_background_color, width=Configuration.side_menu_width - 20, height=Configuration.side_menu_height - 20)
        # self.inner_frame.pack( expand=True, padx=10, pady=10)
        self.load_widgets()
    
    def load_widgets(self):
        # Adiciona os widgets na barra de ferramentas
        for widget in self.widgets:
            widget.pack(in_=self.inner_frame, side=tk.LEFT, padx=5, pady=5)
    
    def clear_widgets(self):
        # Remove todos os widgets do frame interno
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
    
    def update_widgets(self, new_widgets):
        # Atualiza os widgets na barra de ferramentas
        self.clear_widgets()
        self.widgets = new_widgets
        self.load_widgets()
        
    def setWidgets(self, widgets):
        self.widgets = widgets
        
    def show_menu_principal(self):
        pass
    
    def show_editor(self):
        pass