

# 抽象工厂，生产汽车工厂的工厂
class AbstractFactory(object):
    def get_factory(self, type):
        factory_to_create = {'audi': AudiFactory,
                             'bmw': BMWFactory}
        self.factory = factory_to_create[type]()
        return self.factory


# 子工厂的父类，描述具体工厂的公共接口
class IFactory(object):
    def get_car(self, serials):
        pass


# 奥迪工厂
class AudiFactory(IFactory):
    def get_car(self, serials):
        car_dict = {'a4': AudiA4, 'a6': AudiA6}
        self.car = car_dict[serials]()
        return self.car


# 宝马工厂
class BMWFactory(IFactory):
    def get_car(self, serials):
        car_dict = {'x3': BMWX3, 'x6': BMWX6}
        self.car = car_dict[serials]()
        return self.car


# 车父类
class Car(object):
    pass


# 奥迪车父类
class Audi(Car):
    pass


# 宝马车父类
class BMW(Car):
    pass


# a4类，具体产品类
class AudiA4(Audi):
    def show(self):
        return 'AudiA4 good!'


# a6类，具体产品类
class AudiA6(Audi):
    def show(self):
        return 'AudiA6 very good!'


# x3类，具体产品类
class BMWX3(BMW):
    def show(self):
        return 'BMWX3 nice!'


# x6类，具体产品类
class BMWX6(BMW):
    def show(self):
        return 'BMWX6 perfect!'


class CarStore(object):
    ''' 车店类 '''
    def __init__(self):
        self.factory = AbstractFactory()              # 抽象工厂实例化

    def query(self, type, serials):
        try:
            # 通过用户传参对具体工厂实例化
            factory = self.factory.get_factory(type)
            # 实例化具体产品
            car = factory.get_car(serials)
            return car.show()
        except KeyError:
            return 'we do not have this car!'


if __name__ == "__main__":
    store = CarStore()
    car_query = store.query('bmw', 'x3')
    print(car_query)

