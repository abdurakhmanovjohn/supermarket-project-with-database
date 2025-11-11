# from modules.products import Product
# from db import execute_query

# class Supermarket:
#   def __init__(self, name, address):
#     self.name = name
#     self.address = address

#   def view_products(self):
#     products = Product.get_all()
#     print("\n======= Mahsulotlar =======")
#     # for i, p in enumerate(products, start=1):
#     #   print(f"{i}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
#     for p in products:
#       print(f"ID: {p.id}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")