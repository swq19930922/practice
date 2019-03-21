

# 抽象工厂，产生工厂的工厂
class AbstractFactory(object):
    def get_factory_audi(self):
        return AudiFactory()

    def get_factory_bmw(self):
        return BMWFactory()


# 奥迪工厂
class AudiFactory(object):
    def get_car_a4(self):       # 获取a4型车的实例
        return AudiA4()

    def get_car_a6(self):       # 获取a6型车的实例
        return AudiA6()


# 宝马工厂
class BMWFactory(object):
    def get_car_x3(self):       # 获取x3型车的实例
        return BMWX3()

    def get_car_x6(self):       # 获取x6型车的实例
        return BMWX6()


class Audi(object):
    pass


class BMW(object):
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
        self.factory = AbstractFactory()                                # 抽象工厂实例化

    def query(self, type, serials):
        # 通过用户传参对具体工厂实例化
        factory_getting_dict = {'audi': self.factory.get_factory_audi,
                                'bmw': self.factory.get_factory_bmw}
        factory = factory_getting_dict[type]()
        # 实例化具体产品
        if type.lower() == 'audi':
            audi_getting_dict = {'a4': factory.get_car_a4,
                                 'a6': factory.get_car_a6}
            car = audi_getting_dict[serials]()
        elif type.lower() == 'bmw':
            bmw_getting_dict = {'x3': factory.get_car_x3,
                                'x6': factory.get_car_x6}
            car = bmw_getting_dict[serials]()
        return car.show()


if __name__ == "__main__":
    store = CarStore()
    car_query = store.query('audi', 'a4')
    print(car_query)

