import pandas as pd
import numpy as np
import random

from faker import Faker

fake = Faker()

random.seed(42)
np.random.seed(42)

customers = []

for customer_id in range(1, 5001):

    customers.append({
        "customer_id": customer_id,
        "f_name": fake.first_name(),
        "l_name": fake.last_name(),
        "state": fake.state(),
        "address": fake.address().replace("\n", ", ")
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/customers.csv",
    index=False
)

print("Customers Created")

brand_types = [
    "Electronics",
    "Fashion",
    "Home",
    "Sports",
    "Beauty",
    "Books",
    "Toys"
]

sellers = []

for seller_id in range(1, 501):

    sellers.append({
        "seller_id": seller_id,
        "seller_name": fake.company(),
        "brand_type": random.choice(brand_types)
    })

sellers_df = pd.DataFrame(sellers)

sellers_df.to_csv(
    "data/sellers.csv",
    index=False
)

print("Sellers Created")

category_names = [
    "Electronics",
    "Computers",
    "Mobiles",
    "Fashion",
    "Shoes",
    "Beauty",
    "Kitchen",
    "Furniture",
    "Books",
    "Toys",
    "Sports",
    "Automotive",
    "Pet Supplies",
    "Grocery",
    "Jewelry",
    "Office",
    "Health",
    "Baby",
    "Gaming",
    "Music",
    "Garden",
    "Tools",
    "Luggage",
    "Watches",
    "Accessories"
]

categories = []

for category_id, category_name in enumerate(category_names, start=1):

    categories.append({
        "category_id": category_id,
        "category_name": category_name
    })

categories_df = pd.DataFrame(categories)

categories_df.to_csv(
    "data/categories.csv",
    index=False
)

print("Categories Created")

products = []

for product_id in range(1, 1001):

    price = round(random.uniform(10, 1000), 2)

    cogs = round(
        price * random.uniform(0.4, 0.8),
        2
    )

    products.append({
        "product_id": product_id,
        "product_name": fake.word().title() + " " + fake.word().title(),
        "price": price,
        "cogs": cogs,
        "category_id": random.randint(1, 25),
        "seller_id": random.randint(1, 500)
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/products.csv",
    index=False
)

print("Products Created")

warehouses = [
    "New York",
    "Texas",
    "California",
    "Florida",
    "Illinois"
]

inventory = []

for inventory_id in range(1, 1001):

    inventory.append({
        "inventory_id": inventory_id,
        "product_id": inventory_id,
        "stock_remaining": random.randint(10, 1000),
        "ware_house": random.choice(warehouses),
        "restock_date": fake.date_between(
            start_date="-30d",
            end_date="+60d"
        )
    })

inventory_df = pd.DataFrame(inventory)

inventory_df.to_csv(
    "data/inventory.csv",
    index=False
)

print("Inventory Created")

statuses = [
    "Delivered",
    "Shipped",
    "Pending",
    "Returned",
    "Cancelled"
]

weights = [
    70,
    15,
    8,
    5,
    2
]

orders = []

for order_id in range(1, 20001):

    orders.append({
        "order_id": order_id,
        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "customer_id": random.randint(1, 5000),
        "order_status": random.choices(
            statuses,
            weights=weights,
            k=1
        )[0],
        "product_id": random.randint(1, 1000)
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/orders.csv",
    index=False
)

print("Orders Created")

product_price_lookup = (
    products_df
    .set_index("product_id")["price"]
    .to_dict()
)

order_items = []

order_item_id = 1

for order_id in range(1, 20001):

    item_count = random.randint(2, 4)

    for _ in range(item_count):

        product_id = random.randint(1, 1000)

        quantity = random.randint(1, 5)

        price = product_price_lookup[product_id]

        order_items.append({
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "price_per_unit": price,
            "total_price": round(
                quantity * price,
                2
            )
        })

        order_item_id += 1

order_items_df = pd.DataFrame(order_items)

order_items_df.to_csv(
    "data/order_items.csv",
    index=False
)

print("Order Items Created")

payment_modes = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "PayPal",
    "Gift Card"
]

payments = []

for payment_id in range(1, 20001):

    order_status = orders_df.loc[
        payment_id - 1,
        "order_status"
    ]

    if order_status == "Cancelled":
        payment_status = "Refunded"

    elif order_status == "Pending":
        payment_status = "Pending"

    else:
        payment_status = "Paid"

    payments.append({
        "payment_id": payment_id,
        "payment_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "payment_mode": random.choice(
            payment_modes
        ),
        "payment_status": payment_status,
        "order_id": payment_id
    })

payments_df = pd.DataFrame(payments)

payments_df.to_csv(
    "data/payments.csv",
    index=False
)

print("Payments Created")

shipping = []

for shipping_id in range(1, 20001):

    status = orders_df.loc[
        shipping_id - 1,
        "order_status"
    ]

    return_date = None

    if status == "Returned":

        return_date = fake.date_between(
            start_date="-1y",
            end_date="today"
        )

    shipping.append({
        "shipping_id": shipping_id,
        "order_id": shipping_id,
        "delivery_status": status,
        "shipping_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "return_date": return_date
    })

shipping_df = pd.DataFrame(shipping)

shipping_df.to_csv(
    "data/shipping.csv",
    index=False
)

print("Shipping Created")