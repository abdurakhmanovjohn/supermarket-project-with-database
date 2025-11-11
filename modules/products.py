from db import execute_query

class Product:
  def __init__(self, id, name, price, quantity, quantity_type):
    self.id = id
    self.name = name
    self.price = price
    self.quantity = quantity
    self.quantity_type = quantity_type

  @staticmethod
  def get_all():
    query = "SELECT id, product_name, product_price, product_quantity, product_quantity_type FROM products"
    rows = execute_query(query, fetch=True)
    return [Product(*r) for r in rows]

  @staticmethod
  def add(name, price, quantity, qtype):
    query = """
      INSERT INTO products (product_name, product_price, product_quantity, product_quantity_type)
      VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (name, price, quantity, qtype))
    print("Mahsulot qo'shildi!")

  @staticmethod
  def edit(id, name=None, price=None, quantity=None):
    if name:
      execute_query("UPDATE products SET product_name = %s WHERE id = %s", (name, id))
    if price:
      execute_query("UPDATE products SET product_price = %s WHERE id = %s", (price, id))
    if quantity:
      execute_query("UPDATE products SET product_quantity = %s WHERE id = %s", (quantity, id))
    print("Mahsulot tahrirlandi.")

  @staticmethod
  def remove(id):
    execute_query("DELETE FROM products WHERE id = %s", (id,))
    print("Mahsulot o'chirildi.")