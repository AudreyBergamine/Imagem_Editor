import tkinter as tk
from view.menu.pages.MenuPrincipal import MenuPrincipal
from view.menu.pages.Editor import Editor
from view.menu.components.menuBar import MenuBar
from service.image_memory import ImageMemory
from view.menu.components.main_container import main_container
from configuration.configuration import Configuration

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.memory = ImageMemory()
        self.imagem_original = None
        self.current_screen = None
        
        # Detectar tamanho da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        self.title("Imagem Editor")
        
        # Configurar para preencher 100% da tela
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.state('zoomed')  # Maximizar a janela no Windows
        
        self.container = main_container(self, self.trocar_tela)
        self.container.pack(fill="both", expand=True)
        
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)
                
        self.frame = {}
        
        # Inicializar com menu principal
        self.trocar_tela("menu_principal")
    
    def update(self):
        """Destrói todos os widgets filhos do container"""
        for widget in self.container.winfo_children():
            widget.destroy()
    
    def trocar_tela(self, nome_tela):
        """Troca para a tela especificada de forma otimizada"""
        try:
            # Só destrói e recria se for uma tela diferente
            if self.current_screen != nome_tela:
                self.update()
                self.current_screen = nome_tela
                
                if nome_tela == "menu_principal":
                    nova_tela = MenuPrincipal(self.container, self, self.trocar_tela)
                elif nome_tela == "editor":
                    nova_tela = Editor(self.container, self.trocar_tela)
                else:
                    print(f"Tela desconhecida: {nome_tela}")
                    return
                
                nova_tela.pack(fill="both", expand=True)
                
        except Exception as e:
            print(f"Erro ao trocar tela: {str(e)}")
            print(f"Tipo do erro: {type(e).__name__}")

    def __str__(self):
        return "App"

if __name__ == "__main__":
    app = App()
    app.mainloop() 