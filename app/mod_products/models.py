class Product:
    def __init__(self, name, productFamily="default"):
        self.name = name
        self.productFamily = productFamily

class ProductFamily:
    def __init__(self, name, members = set()):
        self.name = name
        self.members = members
