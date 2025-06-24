from components.image_queue import ImageQueue

class ImageMemory:
    def __init__(self):
        self.fila = ImageQueue()
        
        self.image_backEdited = None
        self.index_backEdited = 0
        
        self.image_selected = None
        self.index_selected = 0
        
        self.image_nextEdited = None
        self.index_nextEdited = 0
        
        # Nova propriedade para armazenar a imagem original
        self.imagem_original = None

    def addEdit(self, image):
        if self.index_selected != self.getLastIndex():
            self.fila.restore(self.index_selected)
        self.image_backEdited = self.getLastEdit()
        self.index_backEdited = self.getLastIndex()
        self.fila.add(image)
        self.image_selected = self.getLastEdit()
        self.index_lastEdited = self.getLastIndex()
        self.image_nextEdited = self.image_selected
        self.index_nextEdited = self.index_selected
        self.update()
    
    def moveNext(self):
        if self.index_selected < len(self.fila.images) - 1:
            self.image_backEdited = self.image_selected
            self.index_backEdited = self.index_selected

            self.index_selected += 1
            self.image_selected = self.fila.images[self.index_selected]

            if self.index_selected < len(self.fila.images) - 1:
                self.index_nextEdited = self.index_selected + 1
                self.image_nextEdited = self.fila.images[self.index_nextEdited]
            else:
                self.index_nextEdited = self.index_selected
                self.image_nextEdited = None
        # Se já está na última edição, não faz nada
    
    def moveBack(self):
        back_index = self.getBackIndex(self.index_selected)
        if back_index == self.index_selected:
            return  # Já está na primeira edição, não volta

        # Restaurar a fila para o estado anterior
        self.fila.restore(back_index)

        self.image_nextEdited = self.image_selected
        self.index_nextEdited = self.index_selected

        self.index_selected = back_index
        self.image_selected = self.fila.images[self.index_selected]  # Corrigido

        self.index_backEdited = self.getBackIndex(self.index_selected)
        if self.index_backEdited >= 0:
            self.image_backEdited = self.fila.images[self.index_backEdited]
        else:
            self.image_backEdited = None
    
    def getBackImage(self, index_selected):
        return self.fila.getBackImage(index_selected)
    
    def getBackIndex(self, index):
        return self.fila.getBackIndex(index)
        
    def getNextImage(self, index_selected):
        return self.fila.getNext(index_selected)
    
    def getNextIndex(self, index):
        return self.fila.getNextIndex(index)
    
    def getLastIndex(self):
        return self.fila.getLastIndex()
    
    def getLastEdit(self):
        return self.fila.getLast()
          
    def update(self):
        self.image_selected = self.getLastEdit()
        self.index_selected = self.getLastIndex()
        
        self.image_backEdited = self.getBackImage(self.index_selected)
        self.index_backEdited = self.getBackIndex(self.index_selected)
        
        self.image_nextEdited = self.getNextImage(self.index_selected)
        self.index_nextEdited = self.getNextIndex(self.index_selected)
    
    def restoreImage(self, index):
        self.fila.restore(index)
        self.update()
    
    def addImage(self, image):
        # Se não há imagem original definida, define esta como original
        if self.imagem_original is None:
            self.imagem_original = image.copy()
        
        self.fila.add(image)
        self.update()
        
    def resetLastEdition(self):
        self.fila.back()
        self.update()
    
    def setOriginalImage(self, image):
        """Define uma nova imagem como original e limpa o histórico"""
        self.imagem_original = image.copy()
        # Limpa a fila e adiciona a nova imagem original
        self.fila.images = [self.imagem_original]
        self.update()
    
    def restoreOriginal(self):
        """Restaura para a imagem original"""
        if self.imagem_original is not None:
            # Limpa a fila e adiciona apenas a imagem original
            self.fila.images = [self.imagem_original]
            self.update()
