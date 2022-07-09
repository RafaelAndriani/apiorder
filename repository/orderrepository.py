import psycopg2
from model.order import Order

conn = psycopg2.connect(
    database="postgres", user='postgres', password='admin', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()


def convert_order_list(data):
    order_list = []
    for d in data:
        order_list.append(Order(d[0], d[1], d[2]))
    return order_list


def find_order_id(id):
    sql = f"select id, cnpj, value from \"order\" where id={id};"
    cursor.execute(sql)
    data = cursor.fetchall()
    count = cursor.rowcount
    if count != 0:
        return convert_order_list(data)[0]
    return None


def find_all():
    sql = f"select id, cnpj, value from order;"
    cursor.execute(sql)
    data = cursor.fetchall()
    count = cursor.rowcount
    if count != 0:
        return data
    return None


def save(order):
    sql = f"INSERT INTO public.\"order\"(id, cnpj, value)VALUES({order.id}, {order.cnpj}, {order.value});"
    try:
        cursor.execute(sql)
        conn.commit()
        count = cursor.rowcount
        return count != 0
    except psycopg2.Error as e:
        print(e)
        conn.rollback()
        return False


def delete(id):
    sql = f"DELETE FROM public.\"order\" WHERE id ={id};"
    cursor.execute(sql)
    conn.commit()
    count = cursor.rowcount
    return count != 0


def update(order):
    sql = f'UPDATE public.\"order\" SET cnpj={order.cnpj}, value={order.value} WHERE id={order.id};'
    try:
        cursor.execute(sql)
        conn.commit()
        count = cursor.rowcount
        return count != 0
    except psycopg2.Error as e:
        print(e)
        conn.rollback()




































