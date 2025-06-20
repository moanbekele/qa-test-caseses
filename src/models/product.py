class InvalidPriceError(Exception):
    """Exception raised when product price is invalid"""
    pass

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.validate_price()

    def validate_price(self):
        if self.price < 0:
            raise InvalidPriceError("Price cannot be negative")

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"
