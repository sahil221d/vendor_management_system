# Vendor Management System

Vendor Management System is a Django application for managing vendors, purchase orders, and historical performance metrics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Endpoints](#endpoints)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/vendor-management-system.git

Endpoints
Vendors:

GET /api/vendors/: List all vendors or create a new vendor.
GET /api/vendors/<int:pk>/: Retrieve, update, or delete a specific vendor.
GET /api/vendors/<int:vendor_id>/performance/: Retrieve performance metrics for a specific vendor.
Purchase Orders:

GET /api/purchase_orders/: List all purchase orders or create a new one.
GET /api/purchase_orders/<int:pk>/: Retrieve, update, or delete a specific purchase order.
POST /api/purchase_orders/<int:po_id>/acknowledge/: Acknowledge a purchase order.
