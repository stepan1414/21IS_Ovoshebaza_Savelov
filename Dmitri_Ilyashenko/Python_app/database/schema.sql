PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS deliveries;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS warehouses;

-- СКЛАДЫ
CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT
);

-- СОТРУДНИКИ
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    warehouse_id INTEGER,
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- ПОСТАВЩИКИ
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT
);

-- ТОВАРЫ
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    unit TEXT
);

-- ПОСТАВКИ
CREATE TABLE deliveries (
    delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    supplier_id INTEGER,
    warehouse_id INTEGER,
    quantity INTEGER,
    date TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(warehouse_id)
);

-- ДАННЫЕ
INSERT INTO warehouses (name, location) VALUES
('Главный склад', 'Москва'),
('Холодильник', 'СПб');

INSERT INTO employees (full_name, warehouse_id) VALUES
('Иван Иванов', 1),
('Петр Петров', 2);

INSERT INTO suppliers (name, phone) VALUES
('ООО Овощи', '111-111'),
('Фермер Иван', '222-222');

INSERT INTO products (name, unit) VALUES
('Картофель', 'кг'),
('Морковь', 'кг');