class Notebook:
  _sku = 'unknown'
  _price = 0
  _size = 'unknown'
  def __init__(self, sku, price, size):
      self._sku = sku
      self._price = price
      self._size = size
  def getSku(self):
      return self._sku
  def getPrice(self):
      return self._price
  def getSize(self):
      return self._size
  def info(self):
      return 'Notebook: {} {} {}'.format(self._sku, self._price, self._size)
  def prDetails(self):
      print(self.info())

class Pen:
  _sku = 'unknown'
  _price = 0
  _color = 'unknown'
  def __init__(self, sku, price, color):
      self._sku = sku
      self._price = price
      self._color = color
  def getSku(self):
      return self._sku
  def getPrice(self):
      return self._price
  def getColor(self):
      return self._color
  def info(self):
      return 'Pen: {} {} {}'.format(self._sku, self._price, self._color)
  def prDetails(self):
      print(self.info())


def test():
  nb1 = Notebook('#001', 200, '4K')
  p1 = Pen('#00a', 200, 'Black')
  nb1.prDetails()
  p1.prDetails()
test()