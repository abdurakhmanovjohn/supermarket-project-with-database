from db import execute_query

class User:
  def __init__(self, id, username, password, user_type):
    self.id = id
    self.username = username
    self.password = password
    self.user_type = user_type

  @staticmethod
  def login(username, password):
    query = "SELECT id, username, password, user_type FROM users WHERE username = %s AND password = %s"
    user = execute_query(query, (username, password), fetch=True)
    if not user:
      return None
    id, username, password, user_type = user[0]
    if user_type == "admin":
      return Admin(id, username, password, user_type)
    else:
      return Client(id, username, password, user_type)

class Admin(User):
  def __init__(self, id, username, password, user_type):
    super().__init__(id, username, password, user_type)

class Client(User):
  def __init__(self, id, username, password, user_type):
    super().__init__(id, username, password, user_type)

  def view_balance(self):
    query = "SELECT balance FROM users WHERE id = %s"
    balance = execute_query(query, (self.id,), fetch=True)
    print(f"Sizning balansingiz: {balance[0][0]} so'm")

  def add_to_basket(self, product_id, quantity):
    query = """
      INSERT INTO user_basket (product_id, customer_id, quantity, price, created_time)
      VALUES (%s, %s, %s, (SELECT product_price FROM products WHERE id = %s), NOW())
    """
    execute_query(query, (product_id, self.id, quantity, product_id))
    print("Mahsulot savatchaga qo'shildi.")

  def view_basket(self):
    query = """
      SELECT b.id, p.product_name, b.quantity, b.price
      FROM user_basket b
      JOIN products p ON b.product_id = p.id
      WHERE b.customer_id = %s
    """
    basket = execute_query(query, (self.id,), fetch=True)
    if not basket:
      print("Savatcha bo'sh.")
      return
    print("\n======= Savatcha =======")
    total = 0
    for i, (bid, name, qty, price) in enumerate(basket, start=1):
      print(f"{i}. {name} - {qty} dona x {price} = {qty * price} so'm")
      total += qty * price
    print(f"Jami: {total} so'm")

  def checkout(self):
    query_get = "SELECT product_id, quantity, price FROM user_basket WHERE customer_id = %s"
    items = execute_query(query_get, (self.id,), fetch=True)
    if not items:
      print("Savatcha bo' sh.")
      return
    total = sum(q * p for _, q, p in items)
    balance_query = "SELECT balance FROM users WHERE id = %s"
    balance = execute_query(balance_query, (self.id,), fetch=True)[0][0]
    if balance < total:
      print("Balans yetarli emas!")
      return
    execute_query("UPDATE users SET balance = balance - %s WHERE id = %s", (total, self.id))
    for pid, qty, price in items:
      execute_query("""
        INSERT INTO sales_history (customer_id, product_id, quantity, price, sale_made)
        VALUES (%s, %s, %s, %s, NOW())
      """, (self.id, pid, qty, price))
      execute_query("UPDATE products SET product_quantity = product_quantity - %s WHERE id = %s", (qty, pid))
    execute_query("DELETE FROM user_basket WHERE customer_id = %s", (self.id,))
    print("Xarid muvaffaqiyatli amalga oshirildi!")
  
  def view_sale_history(self):
    query_get = "SELECT * FROM sales_history"
    items = execute_query(query_get, (), fetch=True)
    if not items:
      print("Sotuv tarixi bo'sh")
      return
    else:
      print("\n ======= Stovular Tarixi =======")
      # for i, item in enumerate(items, 1):
      #   sales_id, customer_id, product_id, quantity, price, sale_made_time = item
      #   print(f"{i}")
      for item in items:
        sales_id, customer_id, product_id, quantity, price, sale_made_time = item
        print(f"Sotuv ID: {sales_id}, Mijoz ID: {customer_id}, Produkt ID: {product_id}, Miqdor: {quantity}, Narx: {price}, Sotuv bo'lgan vaqt: {sale_made_time}")
    
    return items


  def view_user_buy_history(self):
    query_get = "SELECT * FROM sales_history WHERE customer_id=%s"
    items = execute_query(query_get, (self.id), fetch=True)
    if not items:
      print("Sotuv tarixi bo'sh")
      return
    else:
      print("\n ======= Stovular Tarixi =======")
      # for i, item in enumerate(items, 1):
      #   sales_id, customer_id, product_id, quantity, price, sale_made_time = item
      #   print(f"{i}")
      for item in items:
        sales_id, product_id, quantity, price, sale_made_time = item
        print(f"Sotuv ID: {sales_id}, Produkt ID: {product_id}, Miqdor: {quantity}, Narx: {price}, Sotuv bo'lgan vaqt: {sale_made_time}")
    
    return items
