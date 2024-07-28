Daily Expense Sharing Application
=================================

Overview
--------

This is a backend service for a daily expenses sharing application. The application allows users to add expenses and split them based on three different methods: exact amounts, percentages, and equal splits. The backend manages user details, validates inputs, and generates downloadable balance sheets.

Features
--------

*   **User Management**: Create and retrieve user details.
    
*   **Expense Management**: Add and retrieve expenses, split expenses using exact amounts, percentages, or equally.
    
*   **Balance Sheet**: Generate and download balance sheets showing individual and overall expenses.
Technologies Used
-----------------

*   Flask: Web framework
    
*   SQLAlchemy: ORM for database management
    
*   Marshmallow: For serialization and deserialization of data
    
*   SQLite: Database (For Larger Datasets can consider postgresql)
    

Setup and Installation
----------------------

### Prerequisites

*   Python 3.6+
    
*   Flask
    
*   SQLAlchemy
    
*   Marshmallow


### Installation

1.  **Clone the repository:**
```shell
git clone https://github.com/yourusername/DailyExpense_ConvinAI.git
cd DailyExpense_ConvinAI
```
2. **Create a virtual environment:**
```shell
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the dependencies:**
```shell
pip install -r requirements.txt
```
4. **Set up the database:**
```shell
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
5. **Run the application:**
```shell
flask run
```
API Endpoints
-------------

### User Endpoints

*   **Create User:**
    
    *   **URL:** `/user`
        
    *   **Method:** `POST`
        
    *   **Payload:**
      ```json
      {
        "email": "user@example.com",
        "name": "John Doe",
        "mobile": "1234567890"
      }
      ```
*   **Retrieve User Details:**
    
    *   **URL:** `/user/<id>`
        
    *   **Method:** `GET`
        

### Expense Endpoints

*   **Add Expense:**
    
    *   **URL:** `/expense`
        
    *   **Method:** `POST`
      
    *   **Payload:**
      ```json
      {
        "description": "Dinner",
        "amount": 100.0,
        "split_method": "equal",
        "user_id": 1,
        "participants": [
          {"user_id": 2},
          {"user_id": 3}
        ]
      }
      ```
*   **Add Expense:**
    *   **URL:** `/expense/user/<user_id>`
    
    *   **Method:** `GET`
    
*   **Retrieve All Expenses:**
    
    *   **URL:** `/expense`
        
    *   **Method:** `GET`
        
###   Balance Sheet Endpoint
    
*   **Generate Balance Sheet:**
    
    *   **URL:** `/balance\_sheet`
    
    *   **Method:** `GET`
  
    *   **Payload:**
    ```shell
    Balance Sheet Summary
    User,Total Amount
    Bob,516.67
    Eva,366.67
    David,366.67

    Detailed Expenses
    Description,Total Amount,Split Method,User,Individual Amount
    Team Lunch,350.00,equal,Bob,116.67
    Team Lunch,350.00,equal,Eva,116.67
    Team Lunch,350.00,equal,David,116.67
    Party,400.00,percentage,Bob,200.00
    Party,400.00,percentage,Eva,100.00
    Party,400.00,percentage,David,100.00
    Dinner,500.00,exact,Bob,200.00
    Dinner,500.00,exact,Eva,150.00
    Dinner,500.00,exact,David,150.00
    ```
  
