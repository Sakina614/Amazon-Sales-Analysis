CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    state VARCHAR(100),
    address TEXT
);
CREATE TABLE sellers(
    seller_id INT PRIMARY KEY,
    seller_name VARCHAR(200),
    brand_type VARCHAR(100)
);
CREATE TABLE category(
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200),
    price NUMERIC(10,2),
    cogs NUMERIC(10,2),

    category_id INT,
    seller_id INT,

    CONSTRAINT products_FOREIGN KEY(category_id)
        REFERENCES category(category_id),

    FOREIGN KEY(seller_id)
        REFERENCES sellers(seller_id)
);

CREATE TABLE inventory(
    inventory_id INT PRIMARY KEY,

    product_id INT,

    stock_remaining INT,
    ware_house_id INT,

    restock_date DATE,

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);

CREATE TABLE orders(
    order_id INT PRIMARY KEY,

    order_date DATE,

    customer_id INT,

    order_status VARCHAR(50),

    product_id INT,

    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);

CREATE TABLE order_items(
    order_item_id INT PRIMARY KEY,

    order_id INT,

    product_id INT,

    quantity INT,

    price_per_unit NUMERIC(10,2),

    total_price NUMERIC(10,2),

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
);

CREATE TABLE payments(
    payment_id INT PRIMARY KEY,

    payment_date DATE,

    payment_mode VARCHAR(50),

    payment_status VARCHAR(50),

    order_id INT,

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
);

CREATE TABLE shipping(
    shipping_id INT PRIMARY KEY,

    order_id INT,

    delivery_status VARCHAR(50),

    shipping_date DATE,

    return_date DATE,

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
);