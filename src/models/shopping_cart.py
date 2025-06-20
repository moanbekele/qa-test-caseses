class InvalidQuantityError(Exception):
    """Exception raised when quantity is invalid"""
    pass

class ProductNotFoundError(Exception):
    """Exception raised when product is not found in cart"""
    pass

class ShoppingCart:
    def __init__(self):
        self.items = {}  # key: product id, value: dict with product and quantity

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero")
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id, quantity):
        if product_id not in self.items:
            raise ProductNotFoundError("Product not found in cart")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero")
        if quantity > self.items[product_id]['quantity']:
            raise InvalidQuantityError("Cannot remove more than existing quantity")
        self.items[product_id]['quantity'] -= quantity
        if self.items[product_id]['quantity'] == 0:
            del self.items[product_id]

    def remove_all_items(self, product_id):
        if product_id not in self.items:
            raise ProductNotFoundError("Product not found in cart")
        del self.items[product_id]

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self.items:
            raise ProductNotFoundError("Product not found in cart")
        if new_quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero")
        self.items[product_id]['quantity'] = new_quantity

    def get_total_price(self):
        total = 0.0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return round(total, 2)

    def get_item_count(self):
        return sum(item['quantity'] for item in self.items.values())

    def clear_cart(self):
        self.items.clear()

    def get_cart_contents(self):
        return [{
            'product_id': item['product'].id,
            'name': item['product'].name,
            'price': item['product'].price,
            'quantity': item['quantity']
        } for item in self.items.values()]

    def __repr__(self):
        return f"ShoppingCart(items={self.items})"
