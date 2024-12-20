from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo

inventory_bp = Blueprint('inventory', __name__)

mongo=PyMongo()
db = mongo.db

@inventory_bp.route('/add', methods=['POST'])
def add_item():
    data = request.json
    new_item = {
        "item_name": data['item_name'],
        "category": data['category'],
        "supplier_id": data['supplier_id'],  # Reference to supplier
        "quantity": data['quantity'],
        "price_per_item": data['price_per_item'],
        "created_at": "timestamp"
    }
    result = mongo.db.stocks.insert_one(new_item)
    return jsonify({"message": "Item added successfully", "item_id": str(result.inserted_id)}), 201

@inventory_bp.route('/list', methods=['GET'])
def list_items():
    # Fetch items from database
    return {"items": []}
