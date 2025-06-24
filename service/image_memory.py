from components.image_queue import ImageQueue

class ImageMemory:
    def __init__(self):
        # Pilha de edições (undo)
        self.undo_stack = []  # imagens já editadas
        # Pilha de refazer (redo)
        self.redo_stack = []  # imagens desfeitas

        self.image_selected = None
        self.imagem_original = None

    def addEdit(self, image):
        if self.image_selected is not None:
            self.undo_stack.append(self.image_selected)
        else:
            # Primeira imagem, define como original
            self.imagem_original = image.copy()
        self.image_selected = image
        self.redo_stack.clear()  # Nova edição limpa o redo

    def moveBack(self):
        if self.undo_stack:
            self.redo_stack.append(self.image_selected)
            self.image_selected = self.undo_stack.pop()
        # Se não houver mais nada para desfazer, permanece na original

    def moveNext(self):
        if self.redo_stack:
            self.undo_stack.append(self.image_selected)
            self.image_selected = self.redo_stack.pop()
        # Se não houver mais nada para refazer, permanece na última

    def restoreOriginal(self):
        if self.imagem_original is not None:
            self.undo_stack.clear()
            self.redo_stack.clear()
            self.image_selected = self.imagem_original.copy()

    def addImage(self, image):
        # Compatibilidade: adiciona imagem como nova edição
        self.addEdit(image)

    def setOriginalImage(self, image):
        self.imagem_original = image.copy()
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.image_selected = self.imagem_original.copy()

    # Métodos auxiliares para compatibilidade
    def getLastEdit(self):
        return self.image_selected
    def getLastIndex(self):
        return len(self.undo_stack)
    def getBackImage(self, _):
        if self.undo_stack:
            return self.undo_stack[-1]
        return self.image_selected
    def getBackIndex(self, _):
        return len(self.undo_stack) - 1 if self.undo_stack else 0
    def getNextImage(self, _):
        if self.redo_stack:
            return self.redo_stack[-1]
        return self.image_selected
    def getNextIndex(self, _):
        return len(self.undo_stack) + 1 if self.redo_stack else len(self.undo_stack)
    def update(self):
        pass  # Não faz nada, compatibilidade
    def restoreImage(self, index):
        # Não implementado neste modelo
        pass
    def resetLastEdition(self):
        self.moveBack()
