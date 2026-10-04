from localapp.Recovered_Backend_20261004_085226.backend09_26_2026.repositories import product_repository



def get_products():
    return product_repository.find_all()

def find_product(product_id):
    return product_repository.find_by_id(product_id)

def create_product(product):
    return product_repository.save(product)

def update_product(product_id, product):
    return product_repository.update(product_id, product)

def patch_product(product_id, updated_data):
    return product_repository.patch(product_id, updated_data)

def delete_product(product_id):
    return product_repository.delete(product_id)

