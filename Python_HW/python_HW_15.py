# task 1

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

new_list = [e.lower() for e in text_list if " " not in e]

print(new_list)


# task 2

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

def discount_counter(num, dis):
    return num * (1 - dis / 100)

discount = int(input("enter discount >>> "))

print("{:<12} {:<13} {:<13}".format("Product", "old price", "new price"))

for pr in products:
    print("{:<12} {:>12.2f}$ {:>12.2f}$".format(pr[0], pr[1], discount_counter(pr[1], discount)))
