

products = [
    {
        "id": 101,
        "name": "Laptop",
        "price": 50000
    },
    {
        "id": 102,
        "name": "Phone",
        "price": 60000
    }
]

def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None
def create_product(new_product):
    for product in products:
        if product["id"] == new_product["id"]:
            return None

    products.append(new_product)
    return new_product