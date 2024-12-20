from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
supplier_bp = Blueprint('supplier', __name__)

mongo = PyMongo()
db = mongo.db

@supplier_bp.route('/add', methods=['POST'])
def add_supplier():
    data = request.json
    new_supplier = {
        "supplier_name": data['supplier_name'],
        "contact": data['contact'],
        "address": data['address'],
        "created_at": "timestamp"
    }
    result = mongo.db.suppliers.insert_one(new_supplier)
    return jsonify({"message": "Supplier added successfully", "supplier_id": str(result.inserted_id)}), 201

@supplier_bp.route('/list', methods=['GET'])
def list_suppliers():
    # Fetch suppliers from database
    return {"suppliers": []}
