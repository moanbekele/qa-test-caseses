from flask import Flask, request, jsonify
from shopping_cart import Product, ShoppingCart

app = Flask(__name__)
cart = ShoppingCart()

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    try:
        product = Product(data['product_id'], data['name'], data['price'])
        cart.add_item(product, data['quantity'])
        return jsonify({
            'message': 'Item added to cart',
            'cart': cart.get_cart_contents(),
            'total': cart.get_total_price()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart', methods=['GET'])
def get_cart():
    return jsonify({
        'cart': cart.get_cart_contents(),
        'total_items': cart.get_item_count(),
        'total_price': cart.get_total_price()
    }), 200

@app.route('/api/cart/total', methods=['GET'])
def get_cart_total():
    return jsonify({
        'total_price': cart.get_total_price(),
        'item_count': cart.get_item_count()
    }), 200

@app.route('/api/cart/update', methods=['PUT'])
def update_cart_item():
    data = request.get_json()
    try:
        cart.update_quantity(data['product_id'], data['quantity'])
        return jsonify({
            'message': 'Cart updated',
            'cart': cart.get_cart_contents(),
            'total': cart.get_total_price()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
def remove_cart_item(product_id):
    try:
        cart.remove_all_items(product_id)
        return jsonify({
            'message': 'Item removed from cart',
            'cart': cart.get_cart_contents(),
            'total': cart.get_total_price()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/remove', methods=['DELETE'])
def remove_partial_item():
    data = request.get_json()
    try:
        cart.remove_item(data['product_id'], data['quantity'])
        return jsonify({
            'message': 'Items removed from cart',
            'cart': cart.get_cart_contents(),
            'total': cart.get_total_price()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/clear', methods=['DELETE'])
def clear_cart():
    cart.clear_cart()
    return jsonify({
        'message': 'Cart cleared',
        'cart': [],
        'total': 0.00
    }), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Shopping cart API is running'
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
