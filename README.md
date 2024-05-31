# Fastkart E-commerce Project

## Overview

Fastkart is a full-featured e-commerce web application built with Django. It includes functionality for user account management, shopping cart, order processing, and store management. The project provides a robust platform for online shopping experiences.

## Features

- **User Authentication**: Register, login, and manage user profiles.
- **Product Management**: Add, update, and remove products.
- **Shopping Cart**: Add items to the cart and proceed to checkout.
- **Order Management**: Process and track orders.
- **Static Files**: CSS, HTML, and JavaScript for frontend design and interactions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ashok66678/Fastkart-Ecommerce-Project.git


## Setup Instructions

2. Navigate to the project directory.

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage
Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).  
Admin interface is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Project Structure
- `account/`: User account management.
- `cart/`: Shopping cart functionality.
- `ecom/`: Core application logic.
- `order/`: Order processing and management.
- `static/`: Static files (CSS, JS, images).
- `store/`: Product and store management.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default, can be changed)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
 
