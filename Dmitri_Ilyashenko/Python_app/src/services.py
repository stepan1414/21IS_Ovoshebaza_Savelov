from db import get_connection

# ---------- EMPLOYEES ----------
def add_employee(name, wid):
    with get_connection() as conn:
        conn.execute("INSERT INTO employees VALUES (NULL, ?, ?)", (name, wid))
        conn.commit()

def get_employees():
    with get_connection() as conn:
        return conn.execute("""
        SELECT e.emp_id, e.full_name, w.name AS warehouse
        FROM employees e
        LEFT JOIN warehouses w ON e.warehouse_id = w.warehouse_id
        """).fetchall()

def update_employee(emp_id, name, wid):
    with get_connection() as conn:
        conn.execute("""
        UPDATE employees SET full_name=?, warehouse_id=? WHERE emp_id=?
        """, (name, wid, emp_id))
        conn.commit()

def delete_employee(emp_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM employees WHERE emp_id=?", (emp_id,))
        conn.commit()


# ---------- WAREHOUSES ----------
def add_warehouse(name, location):
    with get_connection() as conn:
        conn.execute("INSERT INTO warehouses VALUES (NULL, ?, ?)", (name, location))
        conn.commit()

def get_warehouses():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM warehouses").fetchall()

def delete_warehouse(wid):
    with get_connection() as conn:
        conn.execute("DELETE FROM warehouses WHERE warehouse_id=?", (wid,))
        conn.commit()


# ---------- PRODUCTS ----------
def add_product(name, unit):
    with get_connection() as conn:
        conn.execute("INSERT INTO products VALUES (NULL, ?, ?)", (name, unit))
        conn.commit()

def get_products():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM products").fetchall()


# ---------- SUPPLIERS ----------
def add_supplier(name, phone):
    with get_connection() as conn:
        conn.execute("INSERT INTO suppliers VALUES (NULL, ?, ?)", (name, phone))
        conn.commit()

def get_suppliers():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM suppliers").fetchall()


# ---------- DELIVERIES ----------
def add_delivery(pid, sid, wid, qty, date):
    with get_connection() as conn:
        conn.execute("""
        INSERT INTO deliveries VALUES (NULL, ?, ?, ?, ?, ?)
        """, (pid, sid, wid, qty, date))
        conn.commit()

def get_deliveries():
    with get_connection() as conn:
        return conn.execute("""
        SELECT d.delivery_id, p.name AS product, s.name AS supplier, w.name AS warehouse, d.quantity, d.date
        FROM deliveries d
        JOIN products p ON d.product_id = p.product_id
        JOIN suppliers s ON d.supplier_id = s.supplier_id
        JOIN warehouses w ON d.warehouse_id = w.warehouse_id
        """).fetchall()