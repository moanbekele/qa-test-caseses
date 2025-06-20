class Product:
    def __init__(self, id, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id, quantity):
        if product_id not in self.items:
            raise KeyError("Product not found in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if quantity > self.items[product_id]['quantity']:
            raise ValueError("Cannot remove more than existing quantity")
        self.items[product_id]['quantity'] -= quantity
        if self.items[product_id]['quantity'] == 0:
            del self.items[product_id]

    def remove_all_items(self, product_id):
        if product_id not in self.items:
            raise KeyError("Product not found in cart")
        del self.items[product_id]

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self.items:
            raise KeyError("Product not found in cart")
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
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

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return True

def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative")
    return True

def calculate_item_subtotal(product, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    return round(product.price * quantity, 2)

def format_price(price):
    return round(price, 2)
