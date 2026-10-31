"""
Program 8: Store and manage product details using CRUD operations.

Products are stored in a dictionary keyed by product code.
"""

products = {}  # {code: {"name", "price", "quantity"}}


def add_product(code, name, price, quantity):
    """Create: add a product (price and quantity must not be negative)."""
    if code in products:
        print(f"Product {code} already exists.")
    elif price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
    else:
        products[code] = {"name": name, "price": price, "quantity": quantity}
        print(f"Product {code} ({name}) added.")


def view_products():
    """Read: list all products with the stock value of each."""
    if not products:
        print("No products in stock.")
        return
    print(f"{'Code':<8}{'Name':<14}{'Price':<10}{'Qty':<6}{'Stock Value':<12}")
    print("-" * 50)
    for code, p in products.items():
        value = p["price"] * p["quantity"]
        print(f"{code:<8}{p['name']:<14}{p['price']:<10}{p['quantity']:<6}{value:<12}")


def update_product(code, price=None, quantity=None):
    """Update: change price and/or quantity."""
    if code not in products:
        print(f"Product {code} not found.")
        return
    if price is not None:
        products[code]["price"] = price
    if quantity is not None:
        products[code]["quantity"] = quantity
    print(f"Product {code} updated.")


def delete_product(code):
    """Delete: remove a product."""
    if code in products:
        del products[code]
        print(f"Product {code} deleted.")
    else:
        print(f"Product {code} not found.")


try:
    print("--- ADD ---")
    add_product("P101", "Keyboard", 750.0, 20)
    add_product("P102", "Mouse", 350.0, 35)
    add_product("P103", "Monitor", 8999.0, 8)
    add_product("P101", "Duplicate", 1.0, 1)
    add_product("P104", "Cable", -5.0, 10)

    print("\n--- VIEW ---")
    view_products()

    print("\n--- UPDATE ---")
    update_product("P102", price=399.0, quantity=30)
    update_product("P999", price=1.0)

    print("\n--- DELETE ---")
    delete_product("P103")
    delete_product("P103")

    print("\n--- FINAL STOCK ---")
    view_products()
except Exception as e:
    print("Error:", e)


# ============================================================
# SAMPLE INPUT / OUTPUT
# ============================================================
# Output:
# --- ADD ---
# Product P101 (Keyboard) added.
# Product P102 (Mouse) added.
# Product P103 (Monitor) added.
# Product P101 already exists.
# Price and quantity cannot be negative.
#
# --- VIEW ---
# Code    Name          Price     Qty   Stock Value
# --------------------------------------------------
# P101    Keyboard      750.0     20    15000.0
# P102    Mouse         350.0     35    12250.0
# P103    Monitor       8999.0    8     71992.0
#
# --- UPDATE ---
# Product P102 updated.
# Product P999 not found.
#
# --- DELETE ---
# Product P103 deleted.
# Product P103 not found.
#
# --- FINAL STOCK ---
# Code    Name          Price     Qty   Stock Value
# --------------------------------------------------
# P101    Keyboard      750.0     20    15000.0
# P102    Mouse         399.0     30    11970.0
