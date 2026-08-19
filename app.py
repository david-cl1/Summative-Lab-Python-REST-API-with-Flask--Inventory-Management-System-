from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

barcode = "0056195003005" #3274080005003 for nutella 0056195003005=> chipotle
api_url = f"https://world.openfoodfacts.net/api/v3/product/{barcode}.json?fields=product_name"

#temporary python list as a storage
inventory = [
    {
        "id": 1,
        "product_name": "nutella"
    },
    {
        "id": 2,
        "product_name": "chipotle"
    }
]

# Helper function to fetch from external API
def fetch_external_product(identifier):
    if identifier.isdigit():
        url = f"https://world.openfoodfacts.net/api/v3/product/{identifier}.json"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            if data.get("status") == 1:
                prod = data.get("product", {})
                return {"product_name": prod.get("product_name", "Unknown")}
    else:
        url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={identifier}&search_simple=1&action=process&json=1"
        res = requests.get(url)
        if res.status_code == 200:
            products = res.json().get("products", [])
            if products:
                return {"product_name": products[0].get("product_name", "Unknown")}
    return None


@app.route('/')
def home():
    return "Welcome to the food inventory"


@app.route('/inventory', methods=["GET"]) #show all items in the inventory
def show_inventory():
    return jsonify(inventory), 200


@app.route('/inventory/<int:id>', methods=["GET"]) #shows specific item in the inventory
def get_item(id):
    for item in inventory:
        if item["id"] == id:
            return jsonify(item), 200
    return jsonify({"message": "item not found"}), 404


@app.route('/inventory', methods=["POST"]) #adds new item to the inventory
def add_item():
    data = request.get_json() or {}
    new_product_name = data.get("product_name")
    
    if not new_product_name:
        return jsonify({"message": "product_name is required"}), 400

    new_id = len(inventory) + 1
    new_item = {
        "id": new_id,
        "product_name": f"{new_product_name}"
    }
    inventory.append(new_item)
    return jsonify(new_item), 201


@app.route('/inventory/<int:id>', methods=["PATCH"]) #updates an items info in the inventory
def update_item(id):
    data = request.get_json() or {}
    for item in inventory:
        if item["id"] == id:
            item["product_name"] = data.get("product_name", item["product_name"])
            return jsonify(item), 200
    return jsonify({"message": "item not found"}), 404


@app.route('/inventory/<int:id>', methods=["DELETE"]) #deletes an item from the inventory
def remove_item(id):
    for item in inventory:
        if item["id"] == id:
            inventory.remove(item)
            return jsonify({"message": "item deleted successfully"}), 200
    return jsonify({"message": "item not found"}), 404


@app.route('/inventory/external/<path:query>', methods=["POST"]) #fetches external product and adds to inventory
def add_external_item(query):
    ext_data = fetch_external_product(query)
    if not ext_data:
        return jsonify({"message": "item not found on external api"}), 404

    new_id = len(inventory) + 1
    new_item = {
        "id": new_id,
        "product_name": ext_data["product_name"]
    }
    inventory.append(new_item)
    return jsonify({"message": "fetched and saved successfully", "item": new_item}), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)