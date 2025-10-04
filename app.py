from flask import Flask, request, jsonify

app = Flask(__name__)
products = [{"id":1,"name":"Laptop","price":1000},{"id":2,"name":"Phone","price":500}]
cart = []

@app.route('/products')
def list_products():
    return jsonify(products)

@app.route('/cart', methods=['POST'])
def add_cart():
    pid = request.json['id']
    prod = next((p for p in products if p['id']==pid), None)
    if not prod: return {"error":"Not found"}, 404
    cart.append(prod)
    return {"cart": cart}

@app.route('/checkout')
def checkout():
    total = sum(p['price'] for p in cart)
    return {"total": total}
