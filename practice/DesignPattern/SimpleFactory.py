

# 生产汽车的工厂, 用于根据参数实例化对应的汽车类
class Factory(object):
    @staticmethod
    def create_car(car):
        car_to_create = {'audi': Audi, 'bmw': BMW}
        return car_to_create[car]()


# 汽车父类
class Car(object):
    def __init__(self):
        self._price = 0

    def get_price(self):            # 获取价格
        return self._price

    def set_price(self, price):      # 设置价格
        self._price = price


# 奥迪汽车类
class Audi(Car):
    def __init__(self):
        self._price = 200000

    def run(self):
        res = 'Audi is fast!'
        return res


# 宝马汽车类
class BMW(Car):
    def __init__(self):
        self._price = 600000

    def run(self):
        res = 'BMW is fast than Audi！'
        return res


# 车店类向工厂类传递参数实例化对应的汽车
class CarStore(object):

    def show(self, car):
        car_to_sell = Factory.create_car(car)
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
