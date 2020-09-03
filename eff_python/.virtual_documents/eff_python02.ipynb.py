class Resister:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resister):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
        
    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms
        
        


r2 = VoltageResistance(1e3)
print(f"Before: {r2.current:.2f} amps")
r2.voltage = 10
print(f"After: {r2.current:.2f} amps")


class BoudedResitance(Resister):
    def __init__(self, ohms):
        super().__init__(ohms)
        
    @property 
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f"ohms must be > 0; got {ohms}")
        self._ohms = ohms
        
        


r3 = BoudedResitance(1e3)
r3.ohms = 0


r3 = BoudedResitance(-5)


class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0
        
    def __repr__(self):
        return f"Bucket(quota={self.quota})"


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False # there are no water in this period
    if bucket.quota - amount < 0:
        return False # there are any water , but not enough
    bucket.quota -= amount
    return True  # there are full of bucket




from datetime import timedelta, datetime


class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
    
    def __repr__(self):
        return (f"NewBucket(max_quota={self.max_quota})"
               f"quota_consumed={self.quota_consumed}")
    
    @property
    def quota(self):
        return self.max_quota - slef.quota_consumed
    
    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # reset assign for new period
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # enter assign for new period
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta
            
bucket = Bucket(60)
print("Initial", bucket)
fill(bucket, 100)
print("Filled", bucket)

if deduct(bucket, 99):
    print("Had 99 quota")
else:
    print("Not enough for 99 quota")
    
print("Now", bucket)

if deduct(bucket, 3):
    print("Had 3 quota")
else:
    print("Not enough for 3 quota")
    
print("Still", bucket)


class Grade:
    def __get__(self, instance, instance_type):
        pass
    def __set__(self, instance, value):
        pass
    
class Exam:
    # class property
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 40


class Grade:
    def __init__(self):
        self._value = 0
        
    def __get__(self, instance, instance_type):
        return self._value
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._value = value



class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
    
    
first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print("Writing", first_exam.writing_grade)
print("Science", first_exam.science_grade)


second_exam = Exam()
second_exam.writing_grade = 75
print(f"Second {second_exam.writing_grade} is right")
print(f"First {first_exam.writing_grade} is wrong; "
     f"should be 82")


class Grade:
    def __init__(self):
        self._values = {}
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value
        
        


from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value
        
    


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
    
first_exam = Exam()
first_exam.writing_grade = 82

second_exam = Exam()
second_exam.writing_grade = 75
print(f"First {first_exam.writing_grade} is right")
print(f"Second {second_exam.writing_grade} is right")


class LazyRecord:
    def __init__(self):
        self.exists = 5
        
    def __getattr__(self, name):
        value = f"Value for {name}"
        setattr(self, name, value)
        return value
    
    


data = LazyRecord()
print("Before:", data.__dict__)
print("foo:   ", data.foo)
print("After: ", data.__dict__)


class LoggingLazyRecort(LazyRecord):
    def __getattr__(self, name):
        print(f" * Called __getattr__({nameget_ipython().getoutput("r}), "")
             f"populating instance dicitonary")
        result = super().__getattr__(name)
        print(f" * Returning {resultget_ipython().getoutput("r}")")
        return result
    
    
data = LoggingLazyRecort()
print("exists:         ", data.exists)
print("First foo:      ", data.foo)
print("Second foo:     ", data.foo)


class ValidatingRecord:
    def __init__(self):
        self.exists = 5
        
    def __getattribute__(self, name):
        print(f" * Called __getattribute__({nameget_ipython().getoutput("r})")")
        try:
            value = super().__getattribute__(name)
            print(f" * Found {nameget_ipython().getoutput("r} , returning {value!r}")")
            return value
        except AttributeError:
            value = f"Value for {name}"
            print(f" * Setting {nameget_ipython().getoutput("r}, to {value!r}")")
            setattr(self, name, value)
            return value
        
        
data = ValidatingRecord()
print("exists:         ", data.exists)
print("First foo:      ", data.foo)
print("Second foo:     ", data.foo)
            


import numpy as np

from mpl_toolkits.mplot3d import  Axes3D
import matplotlib.pyplot as plt

get_ipython().run_line_magic("matplotlib", " inline")


def f(x, y):
    return (x**2 + y**2)**3 - (x**2)*(y**3)

x = y = np.arange(-1000, 1000)
z = f(x, y)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection="3d")


Axes3D.plot(self=ax, xs=x,ys=y,zs=z)
plt.show()


class MissingPropertyRecord:
    def __getattr__(self, name):
        if name == "bad_name":
            raise AttributeError(f"{name} is missing")
            
            
            
data = MissingPropertyRecord()
data.bad_name


data = LoggingLazyRecort() # implemented __getattr__ method
print("Before:  ", data.__dict__)
print("Has first foo: ", hasattr(data, "foo"))
print("After:   ", data.__dict__)
print("Has second foo:  ", hasattr(data, "foo"))


data = ValidatingRecord()
print("Has first foo : ", hasattr(data, "foo"))
print("Has second foo : ", hasattr(data, "foo"))


class SavingRecord:
    def __setattr__(self, name, value):
        # preserve the data of Record
        super().__setattr__(name, value)
        
        
class LoggingSavingRecord(SavingRecord):
    def __setattr__(sef, name, value):
        print(f"* Called __setattr__({nameget_ipython().getoutput("r}, {value!r})")")
        super().__setattr__(name, value)
        
        
data = LoggingSavingRecord()
print("Before: ", data.__dict__)
data.foo = 5
print("After: ", data.__dict__)
data.foo = 7
print("Finally: ", data.__dict__)


class BrokenDictionaryRecord:
    def __init__(self, data):
        self._data = {}
        
    def __getattribute__(self, name):
        print(f"* Called __getattribute__({nameget_ipython().getoutput("r})")")
        return self._data[name]

    
data = BrokenDictionaryRecord({"foo": 3})
data.foo


class DictionaryRecord:
    def __init__(self, data):
        self._data = data
        
    def __getattribute__(self, name):
        print(f"* Called __getattribute__({nameget_ipython().getoutput("r})")")
        data_dict = super().__getattribute__("_data")
        return data_dict[name]
    
    
data = DictionaryRecord({"foo": 3})
print("foo: ", data.foo)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print(f"* Running {meta}.__new__ for {name}")
        print("Bases: ", bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)
    
class MyClass(metaclass=Meta):
    stuff = 123
    
    def foo(self):
        pass
    
class MySubClass(MyClass):
    other = 567
    
    def bar(self):
        pass
    



class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # validate only subclass of Polygon
        print(bases)
        if not isinstance(bases, object):
            if class_dict["sides"] < 3:
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None # should specify in subclass
    
    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180
    

class Triangle(Polygon):
    sides = 3


class Rectangle(Polygon):
    sides = 4


class Nonagon(Polygon):
    sides = 9


assert Triangle.interior_angles() == 180
assert Rectangle.interior_angles() == 360
assert Nonagon.interior_angles() == 1260


print("Before Class")

class Line(Polygon):
    print("Before sides")
    sides = 2
    print("After sides")
    
print("After class")


class BetterPolygon:
    sides = None # should specify in subclass
    
    # Implicity convert to a class method if this is defined as a instance method
    # When subclass is defined , this method runs , 
    # then class variable (sides) is validated
    def __init_subclass__(cls):
        super().__init_subclass__() # object.__init_subclass__
        print(cls)
        if cls.sides < 3:
            raise ValueError("Polygons need 3+ sides")
            
    @classmethod
    def interior_anagles(cls):
        return (cls.sides - 2) * 180
    

class Hexagon(BetterPolygon):
    sides = 6
    
assert Hexagon.interior_anagles() == 720


print("Before class")

class Point(BetterPolygon):
    sides = 1
    
print("After class")


class ValidateFilled(type):
    def __new__(meta, name, bases, class_dict):
        # validate subclass of Filled
        if bases:
            if class_dict["color"] not in ("red", "green"):
                raise ValueError("Fill color must be supported")
        return type.__new__(meta, name, bases, class_dict)
    

class Filled(metaclass=ValidateFilled):
    color = None # should specify in subclass


class RedPetagon(Filled, Polygon):
    color = "blue"
    sides = 5


class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        # validate only class which is not root
        if not class_dict.get("is_root"):
            if class_dict["sides"] < 3:
                raise ValueError("Polygon need 3+ sides")
        return type.__new__(meta, name, bases, class_dict)
    
    
class Polygon(metaclass=ValidatePolygon):
    is_root = True
    sides = None # should specify in subclasses
    

class ValidateFilledPolygon(ValidatePolygon):
    def __new__(meta, name , bases, class_dict):
        # validate only class which is not root
        if not class_dict.get("is_root"):
            if class_dict["color"] not in ("red", "green"):
                raise ValueError("Fill color must be supported")
        return super().__new__(meta, name, bases, class_dict)
    

class FilledPolygon(Polygon, metaclass=ValidateFilledPolygon):
    is_root = True
    color = None # should specify in subclasses
    


class GreenPentagon(FilledPolygon):
    color = "green"
    sides = 5
    

greenie = GreenPentagon()
print(greenie)
assert isinstance(greenie, Polygon)


class OrangePentagon(FilledPolygon):
    color = "orange"
    sides = 5


class RedLine(FilledPolygon):
    color = "red"
    sides = 2


class Filled:
    color = None # should specify in subclass
    
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.color not in ("red", "green", "blue"):
            raise ValueError("Fills need a valid color")


class RedTriangle(Filled, Polygon):
    color = "red"
    sides = 3
    
    
ruddy = RedTriangle()
assert isinstance(ruddy, Filled)
assert isinstance(ruddy, Polygon)


import json


class Serializable:
    def __init__(self, *args):
        self.args = args
        
    def serialize(self):
        return json.dumps({"args": self.args})
    

class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        
        
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
    
point = Point2D(5, 3)
print("Object:  ", point)
print("Serialized: ", point.serialize())


# serialize : 複数の並列データを直列化して送信すること

class BetterSerializable:
    def __init__(self, *args):
        print(args)
        self.args = args
        
    def serialize(self):
        return json.dumps({
            "class": self.__class__.__name__,
            "args": self.args,
        })
    
    def __repr__(self):
        name = self.__class__.__name__
        args_str = ", ".join(str(x) for x in self.args)
        return f"{name}({args_str})"
            
registry = {}

def register_class(target_class):
    registry[target_class.__name__] = target_class

def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    target_class = registry[name]
    return target_class(*params["args"])

    
class EventBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        
        
        
register_class(EventBetterPoint2D)


before = EventBetterPoint2D(5, 3)
print("Before:  ", before)
data = before.serialize()
print("Serialized: ", data)
after = deserialize(data)
print("After: ", after)


class Point3D(BetterSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z
        

point = Point3D(5, 9, -4)
data = point.serialize()
deserialize(data)


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls
    

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z
        
        
before = Vector3D(10, -7, 3)
print("Before:  ", before)
data = before.serialize()
print("Serialized:  ", data)
print("After:  ", deserialize(data))


class BetterRegisteredSerializable(BetterSerializable):
    def __init_subclass__(cls):
        super().__init_subclass__()
        register_class(cls)
        
    
class Vector1D(BetterRegisteredSerializable):
    def __init__(self, magnitude):
        super().__init__(magnitude)
        self.magnitude = magnitude
        
        
before = Vector1D(6)
print("Before:  ", before)
data = before.serialize()
print("Serialized:  ", data)
print("After:   ", deserialize(data))


class Field:
    def __init__(self, name):
        self.name = name
        self.internal_name = "_" + self.name
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        

class Customer:
    # class property
    first_name = Field("first_name") # 冗長
    last_name = Field("last_name")
    prefix = Field("prefix")
    suffix = Field("suffix")
    
    
customer = Customer()
print(f"Before: {customer.first_nameget_ipython().getoutput("r} {customer.__dict__}")")
customer.first_name = "Euclid"
print(f"After: {customer.first_nameget_ipython().getoutput("r} {customer.__dict__}")")


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = "_" + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


# base class for using the meta class
class DatabaseRow(object, metaclass=Meta):
    pass

# the difference between using meta class and before is needless argument for constructer
class Field:
    def __init__(self):
        # these is assigned for a meta class
        self.name = None
        self.internal_name = None
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        

class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()
    
    
cust = BetterCustomer()
print(f"Before: {cust.first_nameget_ipython().getoutput("r} {cust.__dict__}")")
cust.first_name = "Euler"
print(f"After: {cust.first_nameget_ipython().getoutput("r} {cust.__dict__}")")


class BrokenCustomer:
    first_name = Field()
    second_name = Field()
    prefix = Field()
    suffix = Field()
    
    
cust = BrokenCustomer()
cust.first_name = "Mersenne"


# Descriptor
class Field:
    def __init__(self):
        self.name = None
        self.internal_name = None
        
    def __set_name__(self, owner, name):
        # when creating class, this method is called in every discrypta
        self.name = name
        self.internal_name = "_" + name
        
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return getattr(instance, self.internal_name, "")
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)
        



class FixedCustomer:
    first_name = Field()
    second_name = Field()
    prefix = Field()
    suffix = Field()
    
    
cust = FixedCustomer()
print(f"Before: {cust.first_nameget_ipython().getoutput("r} {cust.__dict__}")")
cust.first_name = "Mersenne"
print(f"After: {cust.first_nameget_ipython().getoutput("r} {cust.__dict__}")")



