

# 具体工厂的父类，描述具体工厂的公共接口
class CarFactory(object):
    def create_car(self):
        pass


# 奥迪工厂
class AudiFactory(CarFactory):
    def create_car(self):
        return Audi()


# 宝马工厂
class BMWFactory(CarFactory):
    def create_car(self):
        return BMW()


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

    def __init__(self):
        self.factory = None

    def show(self, car):
        factory = {'audi': AudiFactory, 'bmw': BMWFactory}
        self.factory = factory[car]()                       # 根据参数选择需实例化的工厂
        car_to_sell = self.factory.create_car()             # 根据具体工厂实例化汽车
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
