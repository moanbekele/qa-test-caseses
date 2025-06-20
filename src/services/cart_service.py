class InvalidQuantityError(Exception):
    """Exception raised when quantity is invalid"""
    pass

class CartService:
    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than zero")
        return True

    def calculate_item_subtotal(self, product, quantity):
        self.validate_quantity(quantity)
        return round(product.price * quantity, 2)
