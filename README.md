
# Shopping Cart Application

Simple shopping cart application with Flask API and unit tests.

## Files

- `shopping_cart.py` - Core logic
- `run_tests.py` - All tests
- `app.py` - Flask API

## Product Methods

```
Product(id, name, price)    # Create product
```

## Shopping Cart Methods

```
ShoppingCart()              # Create empty cart
add_item(product, quantity) # Add item to cart
remove_item(product_id, quantity)  # Remove specific quantity
remove_all_items(product_id)       # Remove all of item
update_quantity(product_id, new_quantity)  # Update item quantity
get_total_price()          # Get cart total
get_item_count()           # Get total items
clear_cart()               # Empty cart
get_cart_contents()        # Get all cart items
```

## Service Functions

```
validate_quantity(quantity)           # Check valid quantity
validate_price(price)                 # Check valid price
calculate_item_subtotal(product, qty) # Calculate item total
format_price(price)                   # Format price to 2 decimal places
```

## API Endpoints

- `POST /api/cart/add` - Add item
- `GET /api/cart` - Get cart contents  
- `GET /api/cart/total` - Get total price

## Running Tests

```
python run_tests.py
```

## Running Application

```
python app.py
```

Server runs on `http://localhost:5000`
```