# Vendor Management System

## Introduction

Welcome to the Vendor Management System, a Django-based application for managing vendors, purchase orders, and performance metrics.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Setup Instructions

### Requirements

- Python (>=3.6)
- Django
- Django REST Framework

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/vendor-management-system.git

1. Navigate to the project directory:

    ```bash
   cd vendor-management-system

3. Create a virtual environment:
   ```bash
   python -m venv venv

5. Activate the virtual environment:
    ```bash
   For Windows: .\venv\Scripts\activate

7. Install dependencies:
   ```bash
   pip install -r requirements.txt

9. Apply database migrations:
   ```bash
   python manage.py migrate

11. Run the development server:
    ```bash
    python manage.py runserver

Your Vendor Management System should now be accessible at http://127.0.0.1:8000/.

### **API Endpoints**
Vendor Management
* List all vendors:
    ```bash
      GET /api/vendors/

* Retrieve a specific vendor's details:
    ```bash
      GET /api/vendors/{vendor_id}/

* Create a new vendor:
   ```bash
   POST /api/vendors/

* Update a vendor details:
   ```bash
   PUT /api/vendors/{vendor_id}/

* Delete a vendor:
   ```bash
   DELETE /api/vendors/{vendor_id}/


### Purchase Order Management
* List all purchase orders:
   ```bash
   GET /api/purchase_orders/

* Retrieve details of a specific purchase order:
   ```bash
   GET /api/purchase_orders/{po_id}/

* Create a purchase order:
   ```bash
   POST /api/purchase_orders/

* Update a purchase order:
   ```bash
   PUT /api/purchase_orders/{po_id}/

* Create a purchase order:
   ```bash
     DELETE /api/purchase_orders/{po_id}/

### Vendor Performance Metrics
* Retrieve a vendor's performance metrics:
   ```bash
     GET /api/vendors/{vendor_id}/performance/

* Acknowledge a purchase order:
   ```bash
     POST /api/purchase_orders/{po_id}/acknowledge/



