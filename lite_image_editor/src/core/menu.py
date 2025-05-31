from __future__ import annotations
import menu_select as ms
from abc import ABC, abstractmethod
from typing import List, Union

class Menu(ABC):
    def __init__(self, menu: ms.Menu_select, nome: str, descricao: str):
        self.menu = menu
        self.nome = nome
        self.descricao = descricao
    
    def abrir_menu(self, opcoes: List[Union[Menu, Option]]):
        index = self.menu.options(descrição=self.descricao, opções=opcoes)
        selecionado = opcoes[index]
        
        try:
            selecionado.executar()
        except NotImplementedError:
            print(f"O menu/opção '{selecionado}' não está implementado.")
    
    @abstractmethod
    def executar(self):
        pass
    
    def __str__(self):
        return self.nome

class Option(ABC):
    def __init__(self,nome: str, menu: Menu = None):
        self.nome = nome
        self.menu = menu
    
    @abstractmethod
    def executar(self):
        pass
    
    def __str__(self):
        return self.nome
