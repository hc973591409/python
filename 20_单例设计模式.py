class Person(object):
    # 定义一个类属性，没创建就false
    __instance = None
    init_flag = False
    # 单利模式，之创建一次，如果多次创建，对象只有一个
    # 只初始化一次
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            print(cls.__instance)
        return cls.__instance           #返回创建对象地址

    def __init__(self, age):
        if not Person.init_flag:
            self.age = age
            Person.init_flag = True
        else:
            return


a = Person(18)
print(a.age)
b = Person(19)
print(b.age)
print(id(a))
print(id(b))

