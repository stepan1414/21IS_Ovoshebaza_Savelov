import sqlite3

conn = sqlite3.connect("vegetable_base.db")
cursor = conn.cursor()

cursor.executescript("""
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS varieties;
DROP TABLE IF EXISTS warehouses;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT
);

CREATE TABLE varieties (
    variety_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    supplier_id INTEGER,
    variety_id INTEGER,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL,
    FOREIGN KEY (variety_id) REFERENCES varieties(variety_id) ON DELETE CASCADE
);

INSERT INTO products (name) VALUES 
('Картофель'),
('Морковь'),
('Лук'),
('Капуста'),
('Свекла');

INSERT INTO suppliers (name, contact) VALUES
('Поставщик 1', '123456'),
('Поставщик 2', '654321'),
('Поставщик 3', '111111'),
('Поставщик 4', '222222'),
('Поставщик 5', '333333');

INSERT INTO varieties (name, product_id) VALUES
('Молодой', 1),
('Красный', 1),
('Сладкий', 2),
('Белый', 3),
('Зимний', 4);

INSERT INTO warehouses (location, supplier_id, variety_id) VALUES
('Склад 1', 1, 1),
('Склад 2', 2, 2),
('Склад 3', 3, 3),
('Склад 4', 4, 4),
('Склад 5', 5, 5);
""")

conn.commit()
conn.close()

print("База данных создана!")
