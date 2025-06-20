from flask import Flask
from src.routes.cart_routes import cart_routes
from src.routes.product_routes import product_routes

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(cart_routes)
    app.register_blueprint(product_routes)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
