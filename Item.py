class Item:

    def __init__(self,id,name,cost,type,img = None):
        self.id = id
        self.name = name
        self.cost = cost
        self.type = type
        self.img = img if img is not None else ""


