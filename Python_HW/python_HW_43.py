from congiguration import client

client.admin.command("ping")
print("Connection successful!")

db = client["ich_edit"]
collection_name = "products_121225ptm_anastasiia_shevchenko"
collection = db[collection_name]

collection.delete_many({})

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Phone", "price": 800, "stock": 10},
    {"name": "Headphones", "price": 150, "stock": 20}
]

result = collection.insert_many(products)

print(f"added products: {len(result.inserted_ids)}")

collection.update_many(
    {},
    [{"$set": {"price": {"$multiply": ["$price", 1.2]}}}]
)

print("updated prices:")
for product in collection.find():
    print(product)

