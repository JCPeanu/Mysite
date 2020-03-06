'''lst1 = [99, 66, 22]
lst2 = lst1
print('lst1:', lst1, 'lst2:', lst2 )
lst2[0] = 777
print('lst1:', lst1, 'lst2:', lst2 )
lst1[-1] = 333
print('lst1:', lst1, 'lst2:', lst2 )

lst3 = [1, 2, 3]
lst4 = [4, 5, 6]
print('lst3:', lst3, 'lst4:', lst4)
lst4[0] = 777
print('lst3:', lst3, 'lst4:', lst4 )
lst3[-1] = 333
print('lst3:', lst3, 'lst4:', lst4 )'''
'''
class Thing:
    _name = 'unknown'
    def __init__(self, name):
        self.name = name
'''
'''
def test():
    t1 = Thing('wood')
    t2 = Thing('iron')
    print(t1._name, t2._name)
    t1.name = 'glass'
    print(t1._name, t2._name)
    t3 = t2
    t3._name = 'salt'
    print(t2._name, t3._name)
test()

def change(t):
    t._name = 'air'
def test2():
    t1 = Thing('tissue')
    print(t1._name)
    change(t1)
    print(t1._name)
test2()'''

class Item:
  _sku = 'unknown'
  _price = 0
  def get_sku(self):
    return self._sku
  def get_price(self):
    return self._price
  def pr_details(self):
    print(self.info())
  def say_hello(self):
    self.intro()

class Notebook(Item):
  def __init__(self, sku, price, size):
    self._sku = sku
    self._price = price
    self._size = size
  def get_size(self):
    return self._size
  def info(self):
    return '{} {} {}'.format(self._sku, self._price, self._size)
  def pr_details(self):
    print('sku:', self._sku)
    print('price:', self._price)
    print('size:', self._size)
  def intro(self):
    print('I am a notebook.')

class Pen(Item):
  def __init__(self, sku, price, color):
    self._sku = sku
    self._price = price
    self._color = color
  def get_color(self):
    return self._color
  def info(self):
    return '{} {} {}'.format(self._sku, self._price, self._color)
  def pr_details(self):
    print('sku:', self._sku)
    print('prie:', self._price)
    print('color:', self._color)
  def intro(self):
    print('I am a pen.')

class Shop(Item):
    _brand = 'unknown'
    _items = None
    def __init__(self, brand):
      self._brand = brand
      self._items = []
    def add_item(self, item):
      self._items.append(item)
    def list_items(self):
      for item in self._items:
        print(item.info())
    def find_item(self, sku):
      for item in self._items:
        if item.get_sku() == sku:
          return item
      return None
    def pr_item(self, sku):
      item = self.find_item(sku)
      if item:
        print(item.info())
      else:
        print('not found')
    def find_cheapest(self):
      cheapest = self._items[0]
      for item in self._items:
        if item._price < cheapest._price:
          cheapest = item
      return cheapest

def test():
  shop = Shop("St King")
  shop.add_item(Notebook("sku01", 100, "8k"))
  shop.add_item(Pen("sku02", 20, "red"))
  shop.add_item(Notebook("sku03", 80, "16k"))
  shop.add_item(Pen("sku04", 30, "black"))

  shop.list_items()
  shop.pr_item("sku02")
  shop.pr_item("sku03")
  shop.pr_item("skuAA")

  item = shop.find_item("sku03")
  item.pr_details()

  # find_item returns None if not found
  item = shop.find_item("abc")
  print(item == None)
  
  cheapest = shop.find_cheapest()
  print(cheapest.info())
  
test()