# INVENTORY
import pandas as pd
import numpy as np
import random

from faker import Faker

fake = Faker()

random.seed(42)
np.random.seed(42)
inventory = []

warehouse_ids = [101, 102, 103, 104, 105]

for inventory_id in range(1, 1001):

    inventory.append({
        "inventory_id": inventory_id,
        "product_id": inventory_id,
        "stock_remaining": random.randint(10, 1000),
        "ware_house_id": random.choice(warehouse_ids),
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