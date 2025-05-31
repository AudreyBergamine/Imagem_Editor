from src.core.menu import Menu, Option


class Sair(Option):
    def __init__(self, menu: Menu = None):
        super().__init__("Sair", menu)
    
    def executar(self):
        print("Obrigado por usar nosso sitema")
        exit(1)
        return super().executar()