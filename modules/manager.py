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
          print("1. Mahsulotlarni ko'rish\n2. Mahsulot Qo'shish\n3. Mahsulotni Tahrirlash\n4. Mahsulotni O'chirish\n5. Sotuv tarixi\n6. Supermarket balansini ko'rish\n7. Chiqish")
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
            try:
              n = input("Nom: ")
              p = int(input("Narx: "))
              q = int(input("Miqdor: "))
              t = input("Turi: ")
              Product.add(n, p, q, t)
            except Exception:
              print("Yuqoridagi ma'lumotlar noto'g'ri kiritilgan, iltimos yana urinib ko'ring")
          elif choice == "3":
            try:
              i = int(input("Mahsulot ID: "))
              n = input("Yangi nom (bo'sh qoldirish mumkin): ") or None
              p = input("Yangi narx: ") or None
              q = input("Yangi miqdor: ") or None
              Product.edit(i, n, int(p) if p else None, int(q) if q else None)
            except Exception:
              print("Yuqoridagi ma'lumotlar noto'g'ri kiritilgan, iltimos yana urinib ko'rining")
          elif choice == "4":
            i = int(input("O'chirish uchun ID: "))
            Product.remove(i)
          elif choice == "5":
            current_user.view_sale_history()
          elif choice == "6":
            current_user.view_balance()
          elif choice == "7":
            break

      elif current_user.user_type == "client":
        while True:
          print("\n======= Mijoz Panel =======")
          print("1. Mahsulotlarni ko'rish\n2. Savatchaga qo'shish\n3. Savatchani ko'rish\n4. Savatchani tahrirlash\n5. Xarid qilish\n6. Balans\n7. Balansga pul qo'shish\n8. Xarid tarixi\n9. Chiqish")
          choice = input("Tanlov: ")
          if choice == "1":
            products = Product.get_all()
            print("\n======= Mahsulotlar =======")
            # for i, p in enumerate(products, start=1):
            #   print(f"{i}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
            for p in products:
              print(f"ID: {p.id}. {p.name} - {p.price} so'm, {p.quantity} {p.quantity_type}")
          elif choice == "2":
            try:
              pid = int(input("Mahsulot ID: "))
              qty = int(input("Miqdor: "))
              current_user.add_to_basket(pid, qty)
            except Exception:
              print("Xato: Miqdor noto'g'ri kiritilgan, iltimos faqat raqam kiriting")
              continue
          elif choice == "3":
            current_user.view_basket()
          elif choice == "4":
            try:
              current_user.view_basket()
              bid = int(input("Tahrirlash uchun savatcha ID: "))
              qty = int(input("Yangi miqdor (0 kiritilsa, o'chiriladi): "))
              current_user.edit_user_basket(bid, qty)
            except Exception:
              print("Xato: Miqdor yoki ID noto'g'ri kiritilgan, iltimos faqat raqam kiriting")
              continue
          elif choice == "5":
            current_user.checkout()
          elif choice == "6":
            current_user.view_balance()
          elif choice == "7":
            try:
              amount = int(input("Qo'shiladigan summa: "))
              current_user.add_money(amount)
            except ValueError:
              print("Xato: Iltimos, faqat raqam kiriting.")
              continue
          elif choice == "8":
            current_user.view_user_buy_history()
          elif choice == "9":
            break