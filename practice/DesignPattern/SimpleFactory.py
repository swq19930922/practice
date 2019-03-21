

# 生产汽车的工厂, 用于根据参数实例化对应的汽车类
class Factory(object):
    def create_car(self, car):
        car_to_create = {'audi': Audi, 'bmw': BMW}
        return car_to_create[car]()


# 奥迪汽车类
class Audi(object):
    def __init__(self):
        self.price = 200000

    def get_price(self):
        return self.price

    def set_price(self,price):
        self.price = price

    def run(self):
        res = 'Audi is fast!'
        return res


# 宝马汽车类
class BMW(object):
    def __init__(self):
        self.price = 600000

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def run(self):
        res = 'BMW is fast than Audi！'
        return res


# 车店类向工厂类传递参数实例化对应的汽车
class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def show(self, car):
        car_to_sell = self.factory.create_car(car)
        price = car_to_sell.get_price()
        desc1 = car_to_sell.run()
        desc2 = 'it needs %sRMB' % (price)
        return desc1+desc2


if __name__ == '__main__':
    car_to_buy = CarStore()
    res1 = car_to_buy.show('audi')
    res2 = car_to_buy.show('bmw')
    print(res1)
    print(res2)
