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
  def intro(self):
    print('I am a pen.')


def test():
  nb1 = Notebook('#01A', 100, '4K')
  print(nb1.get_sku(), nb1.get_price(), nb1.get_size())
  nb1.pr_details()
  nb1.say_hello()
  p1 = Pen('B10', 50, 'Black')
  print(p1.get_sku(), p1.get_price(), p1.get_color())
  p1.pr_details()
  p1.say_hello()
test()