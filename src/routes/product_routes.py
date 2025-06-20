from flask import Blueprint, request, jsonify
from src.models.product import Product
from src.services.product_service import ProductService

product_routes = Blueprint('product_routes', __name__)

product_service = ProductService()
products = {}

@product_routes.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': [vars(p) for p in products.values()]}), 200

@product_routes.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(vars(product)), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

@product_routes.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product_id = data.get('id')
    name = data.get('name')
    price = data.get('price')

    try:
        product_service.validate_price(price)
        product = Product(product_id, name, price)
        products[product_id] = product
        return jsonify({'message': 'Product created', 'product': vars(product)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
