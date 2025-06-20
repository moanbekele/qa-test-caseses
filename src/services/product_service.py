class InvalidPriceError(Exception):
    """Exception raised when product price is invalid"""
    pass

class ProductService:
    def validate_price(self, price):
        if price < 0:
            raise InvalidPriceError("Price cannot be negative")
        return True

    def format_price(self, price):
        return round(price, 2)
