from configuration.configuration import Configuration


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
    
    def getBackImage(self, image):
        index = self.images.index(image) - 1
        
        if index < 0:
            return image
        
        return self.images[index]
    
    def getBackIndex(self, index):
        index -= 1
        
        if index < 0:
            return 0
        
        return index
    
    
    def getNext(self, image):
        index = self.images.index(image) + 1
        
        if index >= len(self.images):
            return self.getLast()
        
        return self.images[index]
    
    def getNextIndex(self, index):
        index += 1
        
        if index >= len(self.images):
            return self.getLastIndex()
        
        return index