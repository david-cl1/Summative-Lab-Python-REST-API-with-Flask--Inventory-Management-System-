from flask import Flask, request, current_app, g, make_response

app=Flask(__name__)

@app.route('/')
def home():
    print ("Welcome to the food inventory")
    selection=input("""
        1:View inventory
        2:View one item
        3:Add a new item
        4:Update an item
        5:Remove an item
        """)
    if selection == 1:

    
@app.route('/inventory')
def inventory():

@app.route('/inventory/int:<id>', methods = ["GET"])
@app.route('/inventory', methods = ["POST"])
@app.route('/inventory/int:<id>', methods = ["PATCH"])
@app.route('/inventory/int:<id>', methods = ["DELETE"])

if __name__ == '__main__':
    app.run(port=5555, debug=True)