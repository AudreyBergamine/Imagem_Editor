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
        
        # Botão Edição Anterior com degradê
        degrad_button_width = 180
        degrad_button_height = 38
        canvas_btn = tk.Canvas(toolsBar, width=degrad_button_width, height=degrad_button_height, highlightthickness=0, bd=0, relief="flat")
        # Desenhar degradê laranja/amarelo
        for i in range(degrad_button_height):
            r = int(255)
            g = int(180 + (220-180)*i/degrad_button_height)  # de 180 a 220
            b = int(40 + (100-40)*i/degrad_button_height)    # de 40 a 100
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas_btn.create_line(0, i, degrad_button_width, i, fill=color)
        # Borda arredondada (simples)
        canvas_btn.create_rectangle(2, 2, degrad_button_width-2, degrad_button_height-2, outline="#e67e22", width=2)
        # Texto
        canvas_btn.create_text(degrad_button_width//2, degrad_button_height//2, text="⟵ Edição Anterior", fill="white", font=("Arial", 11, "bold"))
        # Clique
        def on_click(event):
            voltar_edicao()
        canvas_btn.bind("<Button-1>", on_click)
        canvas_btn.config(cursor="hand2")
        canvas_btn.pack(side="left", anchor="w", padx=(10, 5), pady=8)

        def edicao_posterior():
            memory: ImageMemory = self.app.memory
            memory.moveNext()
            self.app.trocar_tela('menu_principal')

        # Botão Edição Posterior com degradê verde
        degrad_button_width_next = 180
        degrad_button_height_next = 38
        canvas_btn_next = tk.Canvas(toolsBar, width=degrad_button_width_next, height=degrad_button_height_next, highlightthickness=0, bd=0, relief="flat")
        # Degradê verde (inspirado na imagem fornecida)
        for i in range(degrad_button_height_next):
            r = int(80 - (80-0)*i/degrad_button_height_next)   # de 80 a 0
            g = int(255 - (255-200)*i/degrad_button_height_next) # de 255 a 200
            b = int(80 - (80-0)*i/degrad_button_height_next)   # de 80 a 0
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas_btn_next.create_line(0, i, degrad_button_width_next, i, fill=color)
        # Borda arredondada (simples)
        canvas_btn_next.create_rectangle(2, 2, degrad_button_width_next-2, degrad_button_height_next-2, outline="#1e9c2c", width=2)
        # Texto
        canvas_btn_next.create_text(degrad_button_width_next//2, degrad_button_height_next//2, text="Edição Posterior ⟶", fill="white", font=("Arial", 11, "bold"))
        # Clique
        def on_click_next(event):
            edicao_posterior()
        canvas_btn_next.bind("<Button-1>", on_click_next)
        canvas_btn_next.config(cursor="hand2")
        canvas_btn_next.pack(side="left", anchor="w", padx=(5, 10), pady=8)
        
    def __str__(self):
        return "Menu Principal"