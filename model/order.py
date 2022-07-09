class Order(object):
    def __init__(self, id, cnpj, value):
        self.id = id
        self.cnpj = cnpj
        self.value = value
        self.products = []

    def __str__(self):
        return str(self.__dict__)
