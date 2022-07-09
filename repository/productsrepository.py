import psycopg2
from model.order_product import OrderProduct

conn = psycopg2.connect(
    database="postgres", user='postgres', password='admin', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()


def convert_order_product_list(data):
    order_product_list = []
    for d in data:
        order_product_list.append(OrderProduct(name=d[0], id_order=d[1], id_product=d[2], quantity=d[3], price=d[4]))
    return order_product_list


def find_products_by_order(id):
    sql = f"""
select product.name, order_product.id_order, order_product.id_product, order_product.quantity, product.price
from order_product
inner join product
on order_product.id_product  = product.id
where id_order = {id};
"""
    cursor.execute(sql)
    data = cursor.fetchall()
    count = cursor.rowcount
    if count == 0:
        return None
    return convert_order_product_list(data)


def save(o_product):
    sql = f"INSERT INTO public.order_product(id_order, id_product, quantity) values({o_product.id_order}, {o_product.id_product}, {o_product.quantity}); "
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    return count != 0


def delete(id):
    sql = f"DELETE FROM public.order_product WHERE id_order ={id};"
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    return count != 0
