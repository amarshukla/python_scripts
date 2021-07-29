class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    pass
    name = ""
    def name(self):
	    return self.name

ob1 = Logger()
ob1.name = "rahul"
print(ob1.name)

ob2 = Logger()
ob2.name = "priya"
print(ob2.name)
print(ob1.name)
print(ob1==ob2)
