from flask import Flask, request, current_app, g, make_response

app=Flask(__name__)

barcode = 3274080005003 #3274080005003 for nutella
api_url= f"https://world.openfoodfacts.net/api/v3.6/product/{barcode}.json?fields=product_name,brands,nutriments" 
#temporary python list as a storage 
inventory= [
    {"id":1
    "product_name":
     }
]
 

@app.route('/')
def home():
    return "Welcome to the food inventory"
    
@app.route('/inventory', methods = ["GET"])#show all items in the inventory
def show_inventory():
    for item in inventory:
        return item["product_name"]

@app.route('/inventory/int:<id>', methods = ["GET"])# shows pecific item in the inventory
def get_item (id):
    for item in inventory:
        if item["id"] == id:
            return item 
        return "item not found", 404

@app.route('/inventory', methods = ["POST"]) #adds new item to the inventory
def add_item():
    new_id = len(inventory)+1

    new_item ={"id":f"{new_id}"}
   
    inventory.append(new_item)


@app.route('/inventory/int:<id>', methods = ["PATCH"])#updates an items info in the inventory
def update_item(id):

@app.route('/inventory/int:<id>', methods = ["DELETE"])#deletes an item from the inventory
def remove_item(id):

if __name__ == '__main__':
    app.run(port=5555, debug=True)