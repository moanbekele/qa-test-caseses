import unittest
from shopping_cart import (
    Product, ShoppingCart, validate_quantity, validate_price, 
    calculate_item_subtotal, format_price
)

class TestProduct(unittest.TestCase):

    def test_01_product_creation_with_valid_data(self):
        product_id = 1
        product_name = "Laptop"
        product_price = 999.99

        product = Product(product_id, product_name, product_price)

        self.assertEqual(product.id, product_id)
        self.assertEqual(product.name, product_name)
        self.assertEqual(product.price, product_price)

    def test_02_product_creation_with_zero_price(self):
        product_id = 2
        product_name = "Free Sample"
        product_price = 0.00

        product = Product(product_id, product_name, product_price)

        self.assertEqual(product.price, 0.00)

    def test_03_product_creation_with_negative_price_raises_exception(self):
        product_id = 3
        product_name = "Invalid Product"
        invalid_price = -10.00

        with self.assertRaises(ValueError):
            Product(product_id, product_name, invalid_price)

class TestShoppingCart(unittest.TestCase):

    def test_04_cart_initialization_creates_empty_cart(self):
        cart = ShoppingCart()

        self.assertEqual(len(cart.items), 0)
        self.assertEqual(cart.get_total_price(), 0.00)

    def test_05_add_single_item_to_empty_cart(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        quantity = 1

        cart.add_item(product, quantity)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[1]['quantity'], 1)
        self.assertEqual(cart.items[1]['product'], product)

    def test_06_add_multiple_quantities_of_same_item(self):
        cart = ShoppingCart()
        product = Product(1, "Mouse", 25.50)
        initial_quantity = 2
        additional_quantity = 3

        cart.add_item(product, initial_quantity)
        cart.add_item(product, additional_quantity)

        self.assertEqual(cart.items[1]['quantity'], 5)

    def test_07_add_different_products_to_cart(self):
        cart = ShoppingCart()
        product1 = Product(1, "Laptop", 999.99)
        product2 = Product(2, "Mouse", 25.50)

        cart.add_item(product1, 1)
        cart.add_item(product2, 2)

        self.assertEqual(len(cart.items), 2)
        self.assertEqual(cart.items[1]['quantity'], 1)
        self.assertEqual(cart.items[2]['quantity'], 2)

    def test_08_add_invalid_quantity_raises_exception(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        invalid_quantity = -1

        with self.assertRaises(ValueError):
            cart.add_item(product, invalid_quantity)

    def test_09_remove_partial_quantity_from_cart(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        cart.add_item(product, 5)

        cart.remove_item(1, 2)

        self.assertEqual(cart.items[1]['quantity'], 3)

    def test_10_remove_all_quantity_removes_item_completely(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        cart.add_item(product, 3)

        cart.remove_item(1, 3)

        self.assertNotIn(1, cart.items)
        self.assertEqual(len(cart.items), 0)

    def test_11_remove_nonexistent_item_raises_exception(self):
        cart = ShoppingCart()

        with self.assertRaises(KeyError):
            cart.remove_item(999, 1)

    def test_12_remove_more_than_available_raises_exception(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        cart.add_item(product, 2)

        with self.assertRaises(ValueError):
            cart.remove_item(1, 5)

    def test_13_update_item_quantity_changes_amount(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        cart.add_item(product, 2)
        new_quantity = 5

        cart.update_quantity(1, new_quantity)

        self.assertEqual(cart.items[1]['quantity'], new_quantity)

    def test_14_clear_cart_removes_all_items(self):
        cart = ShoppingCart()
        product1 = Product(1, "Laptop", 999.99)
        product2 = Product(2, "Mouse", 25.50)
        cart.add_item(product1, 2)
        cart.add_item(product2, 1)

        cart.clear_cart()

        self.assertEqual(len(cart.items), 0)

    def test_15_calculate_total_for_empty_cart(self):
        cart = ShoppingCart()

        total = cart.get_total_price()

        self.assertEqual(total, 0.00)

    def test_16_calculate_total_for_single_item(self):
        cart = ShoppingCart()
        product = Product(1, "Laptop", 999.99)
        cart.add_item(product, 2)

        total = cart.get_total_price()

        self.assertEqual(total, 1999.98)

    def test_17_calculate_total_for_multiple_items(self):
        cart = ShoppingCart()
        product1 = Product(1, "Laptop", 999.99)
        product2 = Product(2, "Mouse", 25.50)
        cart.add_item(product1, 1)
        cart.add_item(product2, 2)

        total = cart.get_total_price()

        self.assertEqual(total, 1050.99)

class TestServiceFunctions(unittest.TestCase):

    def test_18_validate_positive_quantity_returns_true(self):
        valid_quantity = 5

        result = validate_quantity(valid_quantity)

        self.assertTrue(result)

    def test_19_validate_zero_quantity_raises_exception(self):
        invalid_quantity = 0

        with self.assertRaises(ValueError):
            validate_quantity(invalid_quantity)

    def test_20_calculate_item_subtotal_correct_amount(self):
        product = Product(1, "Test Product", 50.00)
        quantity = 3

        subtotal = calculate_item_subtotal(product, quantity)

        self.assertEqual(subtotal, 150.00)

if __name__ == '__main__':
    unittest.main(verbosity=2)
