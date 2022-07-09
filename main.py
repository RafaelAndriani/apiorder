from flask import Flask, request, Response
import json
from service import orderservice
from model.order import Order
from model.order_product import OrderProduct

app = Flask(__name__)


@app.get("/order/<id>")
def orders(id):
    return Response(json.dumps(orderservice.find_order(id), default=lambda o: o.__dict__), status=200, mimetype="application/json")


@app.post("/order")
def save():
    data_json = request.json
    order = Order(data_json["id"], data_json["cnpj"], data_json["value"])
    products = []
    for product in data_json["products"]:
        products.append(OrderProduct(id_order=product["id_order"], id_product=product["id_product"], quantity=product["quantity"]))
    order.products = products
    save_confirmation = orderservice.save(order)
    if not save_confirmation:
        return Response("Fail", status=400, mimetype="application/json")
    return Response("Created", status=201, mimetype="application/json")


@app.delete("/order/<id>")
def delete(id):
    check = "success" if orderservice.delete(id) else "fail"
    return Response("deleted " + check, status=200, mimetype="application/json")


@app.put("/order/<id>")
def update(id):
    data_json = request.json
    order = Order(id, data_json["cnpj"], data_json["value"])
    products = []
    for product in data_json["products"]:
        products.append(OrderProduct(id, product["id_product"], product["quantity"], product["price"]))
    order.products = products
    if not orderservice.update(order):
        return Response("not updated", status=400, mimetype="application/json")
    return Response("updated", status=200, mimetype="application/json")









if __name__ == "__main__":
    app.run(debug=True)
