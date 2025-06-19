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
                
        self.title("Imagem Editor")
        # Ajusta a janela para ocupar 100% da tela
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        self.geometry(f"{largura_tela}x{altura_tela}+0+0")
        
        self.container = main_container(self, self.trocar_tela)
        self.container.pack(fill="both", expand=True)
        
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)
                
        self.frame = {}
        
        # self.trocar_tela("menu_principal")
    
    def update(self):

        for widget in self.container.winfo_children():
            widget.destroy()        
    
    def trocar_tela(self, nome_tela):
        self.update()
                    
        if nome_tela == "menu_principal":
            nova_tela = MenuPrincipal(self.container, self, self.trocar_tela)
            
        elif nome_tela == "Editor":
            nova_tela = Editor(self.container, self.trocar_tela)
        
        nova_tela.pack(fill="both", expand=True)

    def __str__(self):
        return "App"

if __name__ == "__main__":
    app = App()
    import tkinter.messagebox as messagebox
    app.after(100, lambda: messagebox.showinfo("Bem-vindo!", "Selecione uma imagem para começar!\nVá em Arquivo -> Carregar imagem"))
    app.mainloop() 