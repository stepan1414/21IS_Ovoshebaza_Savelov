from services import (
    get_employees,
    get_warehouses,
    get_products,
    get_suppliers,
    get_deliveries
)

def show_employees():
    for r in get_employees():
        print(r["emp_id"], r["full_name"], r["warehouse"])

def show_warehouses():
    for r in get_warehouses():
        print(r["warehouse_id"], r["name"], r["location"])

def show_products():
    for r in get_products():
        print(r["product_id"], r["name"], r["unit"])

def show_suppliers():
    for r in get_suppliers():
        print(r["supplier_id"], r["name"], r["phone"])

def show_deliveries():
    for r in get_deliveries():
        print(r["delivery_id"], r["product"], r["supplier"], r["warehouse"], r["quantity"], r["date"])