class Counter:
    def __init__(self, n=0):
        self._count = n

    def increase(self):
        self._count += 1

    def get_count(self):
        return self._count

    def create_counter_with(n):
        temp = Counter()
        temp._count = n
        return temp

class User:
    """ eShop User """
    def __init__(self, email, password):
        """ Create new user """
        self._email = email
        self._password = password
        self._cart = None

    def get_email(self):
        return self._email

    def check_password(self,password):
        return self._password == password

    def open_cart(self):
        self._cart = ShoppingCart(belongs_to=self)

    def get_cart(self):
        return self._cart

    def hello(name):
        print('Hello {0}'.format(name))
        
class ShoppingCart:
    """A Shopping Cart"""
    def __init__(self, belongs_to):
        self._belongs_to = belongs_to
        self._items = []

    def add_product(self,product):
        self._items.append(product)

    def remove_product(self,product):
        self._items.remove(product)

    def generate_invoice(self):
        return Invoice(cart=self)

    def get_items(self):
        for p in self._items:
            yield p

    def get_user(self):
        return self._belongsto
    
    def __len__(self):
        return len(self._items)
        
class Invoice:
    """An invoice"""
    def __init__(self,cart):
        self._balance = 0
        self._lineitems = []
        self._user = cart.get_user()
        for product in cart.get_items():
            self._balance += product.get_price()
            self._lineitems.append(product)

    def get_balance(self):
        return self._balance

    def pay(self,amount):
        self._balance -= amount

class Product:
    """A product"""
    def __init__(self, upc, name):
        """Create a new product
           
           upc     the Universal Product Code (barcode)
           name    the name of the product
        """
        self._upc = int(upc)
        self._name = name
        self._price = 0
        
    def get_upc(self):
        return self._upc

    def get_name(self):
        return self._name

    def get_price(self):
        if 'GOLD' in self.get_name().upper():
            return 1000
        else:
            return 100
            
users = [ User('ali@example.com', 'secret'),
          User('banu@gmail.com', 'banu123'),
          User('cansu@metu.edu.tr','spam') ]

products = { 'book' : Product(232131233, 'Book'),
             'watch' : Product(45342233, 'Gold Watch'),
             'pen': Product(23423423,'Pen')}
