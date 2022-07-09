class OrderProduct(object):
    def __init__(self, id_order, id_product, name="", quantity=0, price=0):
        self.name = name
        self.id_order = id_order
        self.id_product = id_product
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str(self.__dict__)
    """
    when you try to print an object class, python calls str and when you call a list of objects python calls repr
    """
    __repr__ = __str__
