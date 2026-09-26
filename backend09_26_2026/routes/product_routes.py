from flask import Blueprint, jsonify, request

from services import product_service



product_bp = Blueprint("product", __name__)







@product_bp.route("/product/<int:product_id>")
def get_product(product_id):

    product = product_service.find_product(product_id)

    if product is None:
        return jsonify({
            "message": "Product not found"
        }), 404

    return jsonify(product), 200


@product_bp.route("/new_product", methods=["POST"])
def create_product_route():
    new_product = request.get_json()
    
    

    if not new_product:
        return jsonify({"message": "JSON data required"}), 400

    if "id" not in new_product:
        return jsonify({"message": "id is required"}), 400

    if "name" not in new_product:
        return jsonify({"message": "name is required"}), 400

    if "price" not in new_product:
        return jsonify({"message": "price is required"}), 400

    created_product = product_service.create_product(new_product)
    return jsonify(created_product), 201


# @product_bp.route("/product/<int:product_id>", methods=["PUT"])
# def update_product(product_id):
#     updated_data = request.get_json()

#     for product in products:
#         if product["id"] == product_id:
#             product["name"] = updated_data["name"]
#             product["price"] = updated_data["price"]

#             return jsonify(product), 200

#     return jsonify({"message": "Product not found"}), 404


# @product_bp.route("/product/<int:product_id>", methods=["DELETE"])
# def delete_product(product_id):
#     for product in products:
#         if product["id"] == product_id:
#             products.remove(product)

#             return jsonify({"message": "Product deleted"}), 200

#     return jsonify({"message": "Product not found"}), 404