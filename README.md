# **Inventory Management System API**

A Flask-based RESTful API designed to manage product inventory with integration to the OpenFoodFacts API for automated product data retrieval. Tested and validated using Postman and pytest.

## **Features**

* **CRUD Operations:** Complete endpoints to create, read, update, and delete inventory items.  
* **External API Integration:** Fetch product information directly from OpenFoodFacts via barcode or search query and save it into local storage.  
* **In-Memory Storage:** Lightweight array-based simulation for local state management.  
* **Automated Unit Testing:** Full test coverage utilizing pytest and unittest.mock.

## **File Structure**

Plaintext  
├── app.py          \# Core Flask API application and routes  
├── test\_app.py     \# Unit tests for testing endpoints and API mocking  
└── README.md       \# Project documentation

## **Prerequisites & Installation**

* **Python 3.8+**  
* Required packages: flask, requests, pytest

Install dependencies:

Bash  
pip install flask requests pytest

## **Running the Application**

Start the Flask development server:

Bash  
python app.py

The application will run locally at \[http://127.0.0.1:5555/\](http://127.0.0.1:5555/).

## **API Endpoints & Postman Usage**

Set request headers in Postman to Content-Type: application/json for POST and PATCH requests.

| Method | Endpoint | Description | Postman Body (raw JSON) / Notes |
| :---- | :---- | :---- | :---- |
| GET | / | Welcome root route | None |
| GET | /inventory | Fetch all inventory items | None |
| GET | /inventory/\<id\> | Fetch specific item by ID | None |
| POST | /inventory | Add new item to inventory | {"product\_name": "peanut butter"} |
| PATCH | /inventory/\<id\> | Update item product name | {"product\_name": "hazelnut spread"} |
| DELETE | /inventory/\<id\> | Remove item from inventory | None |
| POST | /inventory/external/\<query\> | Fetch from OpenFoodFacts & save | Pass barcode or term in URL (e.g., /inventory/external/0056195003005) |

## **Example Requests & Responses**

### **1\. Fetch All Items**

* **GET /inventory**  
* **Response (200 OK):**

JSON  
\[  
  {  
    "id": 1,  
    "product\_name": "nutella"  
  },  
  {  
    "id": 2,  
    "product\_name": "chipotle"  
  }  
\]

### **2\. Add New Item**

* **POST /inventory**  
* **Request Body:**

JSON  
{  
  "product\_name": "peanut butter"  
}

* **Response (201 Created):**

JSON  
{  
  "id": 3,  
  "product\_name": "peanut butter"  
}

### **3\. Add Item via External API**

* **POST /inventory/external/0056195003005**  
* **Response (201 Created):**

JSON  
{  
  "item": {  
    "id": 4,  
    "product\_name": "almond milk"  
  },  
  "message": "fetched and saved successfully"  
}

## **Running Unit Tests**

Execute automated tests with pytest:

Bash  
pytest test\_app.py  
