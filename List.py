

class List:
    x = []
    def __init__(self, size, typeOfList):
        self.size = size
        self.type = typeOfList

    def createList(self):
        return self.x
    
    def append(self, list_nmae, item):
        ls = self.x
        return ls.append(item)
        
