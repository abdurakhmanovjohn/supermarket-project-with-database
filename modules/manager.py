from modules import Product, User

# supermarket = Supermarket("JonnyBeck MCHJ", "Nomongon, Chortoq")

def manager():
  while True:
    print("\n1. Login\n2. Chiqish")
    choice = input("Tanlov: ")

    if choice == "2":
      print("Dasturdan chiqilmoqda...")
      break

    elif choice == "1":
      username = input("Foydalanuvchi nomi: ")
      password = input("Parol: ")
      current_user = User.login(username, password)
      if not current_user:
        print("Noto'g'ri ma'lumotlar!")
        continue

      if current_user.user_type == "admin":
        while True:
          print("\n======= Admin Panel =======")
          print("1. Mahsulotlarni ko'rish\n2. Mahsulot Qo'shish\n3. Mahsulotni Tahrirlash\n4. Mahsulotni O'chirish\n5. Sotuv tarixi \n6. Chiqish")
          choice = input("Tanlov: ")
          if choice == "1":
            # supermarket.view_products()
            products = Product.get_all()
            print("\n======= Mahsulotlar =======")
            # for i, p in enumerate(products, start=1):
            #   print(f"{i}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
            for p in products:
              print(f"ID: {p.id}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
          elif choice == "2":
            n = input("Nom: ")
            p = int(input("Narx: "))
            q = int(input("Miqdor: "))
            t = input("Turi: ")
            Product.add(n, p, q, t)
          elif choice == "3":
            i = int(input("Mahsulot ID: "))
            n = input("Yangi nom (bo'sh qoldirish mumkin): ") or None
            p = input("Yangi narx: ") or None
            q = input("Yangi miqdor: ") or None
            Product.edit(i, n, int(p) if p else None, int(q) if q else None)
          elif choice == "4":
            i = int(input("O'chirish uchun ID: "))
            Product.remove(i)
          elif choice == "5":
            pass
          elif choice == "6":
            break

      elif current_user.user_type == "client":
        while True:
          print("\n======= Mijoz Panel =======")
          print("1. Mahsulotlarni ko'rish\n2. Savatchaga qo'shish\n3. Savatchani ko'rish\n4. Xarid qilish\n5. Balans\n6. Chiqish")
          choice = input("Tanlov: ")
          if choice == "1":
            products = Product.get_all()
            print("\n======= Mahsulotlar =======")
            # for i, p in enumerate(products, start=1):
            #   print(f"{i}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
            for p in products:
              print(f"ID: {p.id}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
          elif choice == "2":
            pid = int(input("Mahsulot ID: "))
            qty = int(input("Miqdor: "))
            current_user.add_to_basket(pid, qty)
          elif choice == "3":
            current_user.view_basket()
          elif choice == "4":
            current_user.checkout()
          elif choice == "5":
            current_user.view_balance()
          elif choice == "6":
            break