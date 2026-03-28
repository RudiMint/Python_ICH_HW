# task 1

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
# def sorted_orders(data):
#     result = []
#     for d in data:
#         if d["price"] > 500:
#             result.append(d["product"])
#     return result
#
# products_list = sorted(sorted_orders(orders), key=lambda x: x[0].lower())

product_list = sorted(
    map(lambda x: x["product"],
        filter(lambda x: x["price"] > 500, orders)),
    key=lambda x: x[0].lower()
)

print(product_list)


# task 2

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

# price = lambda x, y: x * y
# sales_dict = {k[0]: price(k[1], k[2]) for k in sales}
# sorted_sales = dict(sorted(sales_dict.items(), key=lambda x: x[1], reverse=True))


sorted_sales = dict(sorted(
    {product: amount * price for product, amount, price in sales}.items(), key=lambda x: x[1], reverse=True)
)
print(sorted_sales)
