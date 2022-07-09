import repository.orderrepository as db_order
import repository.productsrepository as db_products


def find_order(id):
    order = db_order.find_order_id(id)
    products = db_products.find_products_by_order(id)
    order.products = products
    return order


def save(order):
    if not db_order.save(order):
        return False
    for product in order.products:
        db_products.save(product)
    return True


def delete(id):
    db_products.delete(id)
    return db_order.delete(id)


def update(order):

    db_products.delete(order.id)
    for product in order.products:
        db_products.save(product)
    return db_order.update(order)
