from .Configuration import Configuration


class ImageQueue:
    def __init__(self):    
        self.images = []
        self.limit_memory = Configuration.limit_image_memory 
    
    def add(self, image):
        self.images.append(image)
        
        if len(self.images) > self.limit_memory:
            self.images.pop(0)
    
    def back(self):
        self.images.pop()
    
    def restore(self, index):
        while len(self.images) > index+1:
            self.images.pop()    
            
    def getLast(self):
        return self.images[-1]
    
    def getLastIndex(self):
        return len(self.images)-1
    
    def getBackImage(self, index_selected):
        if (len(self.images) -1 < index_selected):
            return self.images[index_selected]
        else:
            return self.images[index_selected]
    
    def getBackIndex(self, index):
        index -= 1
        
        if index < 0:
            return 0
        
        return index
    
    
    def getNext(self, index_selected):
        if (len(self.images) -1 > index_selected):
            return self.images[index_selected + 1]
        else:
            return self.images[index_selected]
    
    def getNextIndex(self, index):
        index += 1
        
        if index >= len(self.images):
            return self.getLastIndex()
        
        return index