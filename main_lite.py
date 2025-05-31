import menu_select as ms

menu = ms.Menu_select("Teste")

class teste:
    def __init__(self):
        self.nome = "Testar"
    
    def execute(self):
        
        print("Testando...")

    def __str__(self):
        return self.nome    

list = [teste]
list[menu.options(opções=list)].execute()