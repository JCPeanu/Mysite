class Car:
    def __init__(self, name, weight, cap, mileage, price):
        self.name = name
        self.weight = weight
        self.cap = cap
        self.mileage = mileage
        self.price = price
    def info(self):
        fmt = '{:10}{:10}{:10}{:10}{:10}'
        return fmt.format(self.name, self.weight, self.cap, self.mileage, self.price)
def print_cars(cars):
    for car in cars:
        print(car.info())

def select_weight_less_equal(cars, weight):
    chosen = []
    for car in cars:
        if car.weight <= weight:
            chosen.append(car)
    return chosen
def select_price_range(cars, low, high):
    chosen = []
    for car in cars:
        if car.price <= high and car.price >= low:
            chosen.append(car)
    return chosen
def select_price_and_weight_range(cars, low, high, weight):
    chosen = []
    for car in cars:
        if car.weight <= weight:
            if car.price <= high and car.price >= low:
                chosen.append(car)
    return chosen
def read_cars():
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    with open('Cars.txt') as f1:
        line = f1.readline()
        line = line.strip()
        ts = line.split()
        print(fmt.format(ts[0], ts[1], ts[2], ts[3], ts[4]))
        cars = []
        for line in f1:
            line = line.strip()
            ts = line.split()
            car = Car(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            cars.append(car)
        print('select weight less equal:')
        chosen_cars = select_weight_less_equal(cars, 500)
        print_cars(chosen_cars)

        print('select price in range:')
        chosen_cars = select_price_range(cars, 100000, 700000)
        print_cars(chosen_cars)
        print('select by two conditions:')
        chosen1 = select_weight_less_equal(cars, 450)
        chosen2 = select_price_range(chosen1, 100000, 700000)
        print_cars(chosen2)
read_cars()