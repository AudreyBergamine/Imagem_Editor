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

    def addEdit(self, image):
        self.image_backEdited = self.getLastEdit()
        self.index_backEdited = self.getLastIndex()
        
        self.fila.add(image)
        self.image_selected = self.getLastEdit()
        self.index_lastEdited = self.getLastIndex()
        
        self.image_nextEdited = self.image_selected
        self.index_nextEdited = self.index_selected
    
    def moveNext(self):
        if self.index_nextEdited == self.index_selected:
            return
        
        self.image_backEdited = self.image_selected
        self.index_backEdited = self.index_selected
        
        self.image_selected = self.image_nextEdited
        self.index_selected = self.index_nextEdited
        
        self.image_nextEdited = self.getBackImage(self.image_nextEdited)
        self.index_nextEdited = self.getBackIndex(self.index_nextEdited)
    
    def moveBack(self):
        if self.index_lastEdited == self.index_selected:
            return
        
        self.image_nextEdited = self.image_selected
        self.index_nextEdited = self.index_selected
        
        self.image_selected = self.image_backEdited
        self.index_selected = self.index_backEdited
        
        self.image_backEdited = self.getLastEdit()
        self.index_backEdited = self.getLastIndex()
    
    def getBackImage(self, image):
        return self.fila.getBack(image)
    
    def getBackIndex(self, index):
        return self.fila.getBackIndex(index)
        
    def getNextImage(self, image):
        return self.fila.getNext(image)
    
    def getNextIndex(self, index):
        return self.fila.getNextIndex(index)
    
    def getLastIndex(self):
        return self.fila.getLastIndex()
    
    def getLastEdit(self):
        return self.fila.getLast()
          
    def update(self):
        self.image_selected = self.getLastEdit()
        self.index_selected = self.getLastIndex()
        
        self.image_backEdited = self.getBackImage(self.image_selected)
        self.index_backEdited = self.getBackIndex(self.index_selected)
        
        self.image_nextEdited = self.getNextImage(self.image_selected)
        self.index_nextEdited = self.getNextIndex(self.index_selected)
    
    def restoreImage(self, index):
        self.fila.restore(index)
        self.update()
    
    def addImage(self, image):
        self.fila.add(image)
        self.update()
        
    def resetLastEdition(self):
        self.fila.back()
        self.update()
