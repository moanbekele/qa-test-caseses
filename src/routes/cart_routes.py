from flask import Blueprint, request, jsonify
from src.models.shopping_cart import ShoppingCart
from src.models.product import Product
from src.services.cart_service import CartService

cart_routes = Blueprint('cart_routes', __name__)

cart = ShoppingCart()
cart_service = CartService()

@cart_routes.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    name = data.get('name', 'Unknown')
    price = data.get('price', 0.0)

    try:
        cart_service.validate_quantity(quantity)
        product = Product(product_id, name, price)
        cart.add_item(product, quantity)
        return jsonify({'message': 'Item added to cart', 'cart': cart.get_cart_contents()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cart_routes.route('/api/cart/update', methods=['PUT'])
def update_cart_item():
    data = request.get_json()
    product_id = data.get('product_id')
    new_quantity = data.get('quantity')

    try:
        cart_service.validate_quantity(new_quantity)
        cart.update_quantity(product_id, new_quantity)
        return jsonify({'message': 'Cart updated', 'cart': cart.get_cart_contents()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cart_routes.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
def remove_cart_item(product_id):
    try:
        cart.remove_all_items(product_id)
        return jsonify({'message': 'Item removed from cart', 'cart': cart.get_cart_contents()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@cart_routes.route('/api/cart/clear', methods=['DELETE'])
def clear_cart():
    cart.clear_cart()
    return jsonify({'message': 'Cart cleared'}), 200

@cart_routes.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify({'cart': cart.get_cart_contents()}), 200

@cart_routes.route('/api/cart/total', methods=['GET'])
def get_cart_total():
    total = cart.get_total_price()
    return jsonify({'total_price': total}), 200
