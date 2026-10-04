from flask import Blueprint, jsonify, request

from localapp.Recovered_Backend_20261004_085226.backend09_26_2026.services import product_service
from localapp.Recovered_Backend_20261004_085226.backend09_26_2026.utils import response_utils



product_bp = Blueprint("product", __name__)





@product_bp.route("/products",methods=['GET'])
def get_products():
    products = product_service.get_products()
    return jsonify(products), 200

@product_bp.route("/product/<int:product_id>")
def get_product(product_id):

    product = product_service.find_product(product_id)

    if product is None:
        return response_utils.error_response("Product not found", 404)

    return jsonify(product), 200


@product_bp.route("/products", methods=["POST"])
def create_product():
    new_product = request.get_json()

    if not new_product:
        return jsonify({"message": "JSON data required"}), 400

    if "name" not in new_product or "price" not in new_product:
        return jsonify({"message": "name and price are required"}), 400

    created_product = product_service.create_product(new_product)

    return jsonify(created_product), 201



@product_bp.route("/product/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"message": "JSON data required"}), 400

    if "name" not in updated_data or "price" not in updated_data:
        return jsonify({"message": "name and price are required"}), 400

    product = product_service.update_product(product_id, updated_data)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product), 200


@product_bp.route("/products/<int:product_id>", methods=["PATCH"])
def patch_product(product_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"message": "JSON data required"}), 400

    product = product_service.patch_product(product_id, updated_data)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product), 200

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = product_service.delete_product(product_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify({
        "message": "Product deleted successfully",
        "product": product
    }), 200