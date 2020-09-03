get_ipython().getoutput("python --version")


a = b'h\x65llo'
print(list(a))
print(a)


a = "a\u0300 propos"
print(list(a))
print(a)


b = []
if not b:
    print("b is empty")


b = [1]
if b:
    print("b is not empty")
else:
    print("b is empty")


from typing import Union

def to_str(bytes_or_str: Union[str, bytes]) -> str:
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b"foo")))
print(repr(to_str("bar")))


def to_bytes(bytes_or_str: Union[str, bytes]) -> bytes:
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str

print(repr(to_bytes(b"foo")))
print(repr(to_bytes("bar")))


print(b"one"+b"two")


print("one"+"two")


b"one"+"two"


import numpy as np

from matplotlib import pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")

def f(x):
    return x**2 + 2*x

x = np.arange(-1,10)
y = [f(i) for i in x]

fig = plt.figure()
plt.plot(x, y, ".-")
plt.show()



assert b"red" > b"blue"
assert "red" > "blue"


assert b"red" > "red"


assert "red" > b"blue"


print(b"foo" == "foo")


print(b"red get_ipython().run_line_magic("s"", " % b\"blue\")")


print("red get_ipython().run_line_magic("s"", " % \"blue\")")


print(b"red get_ipython().run_line_magic("s"", " % \"blue\")")


with open("random.bin", "wb") as f:
    f.write(b"\xf1\xf2\xf3\xf4\xf5")


with open("random.bin", "rb") as f:
    data = f.read()


data


with open("random.bin", "r") as f:
    data = f.read()


assert data == b"\xf1\xf2\xf3\xf4\xf5"


a = 0b10111011
b = 0xc5f
print("Binary is get_ipython().run_line_magic("d,", " hex is %d\" % (a, b))")


key = "my_var"
value = 1.234
formatted = "get_ipython().run_line_magic("-10s", " = %.2f\" % (key, value)")
print(formatted)



reordered_string = "get_ipython().run_line_magic("-10s", " = %.2f\" % (value, key)")


reordered_string = "get_ipython().run_line_magic(".2f", " = %-10s\" % (key, value)")


key = "my_var"
value = 1.234

old_way = "get_ipython().run_line_magic("-10s", " = %.2f\" % (key, value)")

new_way = "get_ipython().run_line_magic("(key)-10s", " = %(value).2f\" % {")
    "key": key, "value": value
}

reordered = "get_ipython().run_line_magic("(key)-10s", " = %(value).2f\" % {")
    "value": value, "key": key
}

assert old_way == new_way == reordered


# 要はフォーマット文字列が見やすいし、キャストの問題も解決してくれるからこれ使えってこと。

key = "my_var"
value = 1.234

formatted = f"{key} = {value}"
print(formatted)


formatted = f"{keyget_ipython().getoutput("r:<10} = {value:.2f}"")
print(formatted)


from urllib.parse import parse_qs


my_values = parse_qs("red=5&blue=0&green=",
                    keep_blank_values=True)
print(repr(my_values))


print("red:", my_values.get("red"))
print("green:", my_values.get("green"))
print("Opacity:", my_values.get("opacity"))


red = my_values.get("red", [""])[0] or 0
print(f"red :   {redget_ipython().getoutput("r}")")


# hard to see
red = int(my_values.get("red", [""])[0] or 0)
print(red)


from typing import List
# So, by using ternary operator, it is easy to see
red_str: List[str] = my_values.get("red", [""])
red = int(red_str[0]) if red_str[0] else 0
print(red)


green_str = my_values.get("green", [""])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
    
print(green)


from typing import Dict
# if you used the logic like this, you must use helper funciton
def get_first_int(values: Dict[str, List[str]], key: str, default: int=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    else:
        return default
    
# this is more clear than others. (using "or", using Ternary Operator) 
green = get_first_int(my_values, "green")

print(green)

# the profit made by readabilty　is more than  the one made by code is simple
# you should keep DRY on mind 


snack_calories = {
    "chips" : 140,
    "popcorn" : 80,
    "nuts" : 190,
}

items = tuple(snack_calories.items())
print(items)


item = ("Peanut butter", "Jelly")
first = item[0]
second = item[1]

print(first, "and", second)


first, second = item # unpack
print(first, "and", second)


favorite_snacks = {
    "salty": ("pretzels", 100),
    "sweet": ("cookies", 180),
    "veggie": ("carrotes", 20),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f"favarite {type1} is {name1} with {cals1} calories")
print(f"favarite {type2} is {name2} with {cals2} calories")
print(f"favarite {type3} is {name3} with {cals3} calories")


from typing import List, Union
# bubble sort
def bubble_sort(a: List[Union[str, float]]):
    for _ in range(1, len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                tmp = a[i]
                a[i] = a[i-1]
                a[i-1] = tmp
                
                
names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort(names)
print(names)


nums = [ 1, 2, 5, 11, 7, 8, 8, 10]
bubble_sort(nums)
print(nums)


def bubble_sort2(a: List[int], i: int)-> List[int]:
    if a[i] < a[i-1]:
        tmp = a[i]
        a[i] = a[i-1]
        a[i-1] = tmp
        return a
    else:
        return a


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from IPython.display import HTML
get_ipython().run_line_magic("matplotlib", " inline")



nums = [ 1, 2, 5, 11, 7, 8, 10, 3, 4, 6]

ims = []

fig = plt.figure()
for i in range(1, len(nums)):
    a = bubble_sort2(nums, i)
    x = np.arange(1, len(a)+1)
    im = plt.plot(x, np.array(a))
    ims.append(im)
    
ani = animation.ArtistAnimation(fig, ims, interval=500)
HTML(ani.to_jshtml())


nums


def bubble_sort3(a: List[Union[str, float]]):
    for _ in range(1, len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                # swap
                a[i-1], a[i] = a[i], a[i-1]
                
names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort3(names)
print(names)


snacks = [
    ("bacon", 350),
    ("donut", 240),
    ("muffin", 190),
]

for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"#{i+1}: {name} has {calories} calories")


for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")


from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
        
print(bin(random_bits))
print(random_bits)


a = 1

a |= 2

print(a)


# |= inplcace OR operator
# here, toward bit set 
a = 3
print(bin(a))
a |= 1
print(bin(1))
print(bin(a))
print(a)

a = 2
print(bin(a))
a |= 5
print(bin(5))
print(bin(a))
print(a)


flavor_list = ["valila", "chocolate", "pecan", "strawberry"]


it = enumerate(flavor_list)
print(next(it))
print(next(it))


for i, flavor in enumerate(flavor_list):
    print(f"{i+1}: {flavor}")


# specify the start num
for i, flavor in enumerate(flavor_list, 1):
    print(f"{i}: {flavor}")


names = ["Cacilia", "Lise", "Marie"]
counts = [len(n) for n in names]

print(counts)


longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
        
print(longest_name)


longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)


longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)


from itertools import zip_longest

names.append("Rosalind")

for name, count in zip_longest(names, counts):
    print(f"{name}: {count}")


for i in range(3):
    print("Loop", i)
else:
    print("else blockget_ipython().getoutput("")")


for i in range(3):
    print("Loop", i)
    if i == 2:
        break
else:
    print("else blockget_ipython().getoutput("")")


for x in []:
    print("Never runs")
else:
    print("For Else blockget_ipython().getoutput("")")


while False:
    print("Never runs")
else:
    print("While Else blockget_ipython().getoutput("")")



a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print("Not coprime")
        break
else:
    print("Coprime")


def coprime(a: int, b: int)->bool:
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4, 9)
assert not coprime(3, 6)


def coprime2(a: int, b: int)->bool:
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime2(4, 9)
assert not coprime2(3, 6)


a = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(a[3:5])
print(a[1:7])


assert a[:5] == a[0:5]


assert a[5:] == a[5:len(a)]


a[:]


a[:5]


a[:-1]


a[4:]


a[-3:]


a[2:5]


a[2:-1]


a[-3:-1]


b = a[3:]
print(b)
b[1] = 99


print(b)


print(a)


a[2:7] = [99, 22, 14]
print(a)


b = a[:]
assert b == a and b is not a


b = a
print(a)
print(b)


a[:] = [101, 102, 103]
assert a is b


x = ["red", "orange", "yellow", "green", "blue", "purple"]
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)


x = b"mongoose"
y = x[::-1]

print(y)


x = "寿司"
y = x[::-1]
print(y)


w = "寿司"
x = w.encode("utf-8")
y = x[::-1]
z = y.decode("utf-8")


# itertools.islice


car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending


print(oldest, second_oldest, others)


numbers = [93, 86, 68, 70]
numbers.sort()
print(numbers)


class Tool:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    def __repr__(self):
        return f"Tool({self.nameget_ipython().getoutput("r}, {self.weight})"")
    
    
tools = [
    Tool("level", 3.5),
    Tool("hammer", 1.25),
    Tool("screwdriver", 0.5),
    Tool("chisel", 0.25)
]


tools.sort()


print("Unsortd", repr(tools))
tools.sort(key=lambda x: x.name)
print("\nSored: ", tools)


tools.sort(key=lambda x: x.weight)
print("By weight: ", tools)


votes = {
    "baguette": ["Bob", "Alice"],
    "ciabatta": ["Coco", "Deb"]
}

key = "brioche"
who = "Elimer"

names = votes.get("key")
if names is None:
    votes[key] = names = []

names.append(who)


names


from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()

visits.add("England", "Bath")
visits.add("England", "London")

print(visits.data)


# ファイルシステムにあるソーシャルネットワークプロフィールの写真を管理するプログラムを書いてるとする。
pictures = {}

path = "profile_1234.png"

handle = pictures.get(path)
if handle is None:
    try:
        handle = open(path, "a+b")
    except OSError:
        print(f"Failed to open path {path}")
        raise
    else:
        pictures[path] = handle
    
    
handle.seek(0)
image_data = handle.read()


try:
    handle = pictures.setdefault(path, open(path, "a+b"))
except OSError:
    print(f"Failed to open path {path}")
    raise

else:
    handle.seek(0)
    image_data = handle.read()
    



from collections import defaultdict

def open_picture(profile_path: str):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path {profile_path}")
        raise

# defaultdict はコンストラクタに渡される関数には引数がないと仮定してる
pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()


# 欠損キーを扱うロジック
# Dict型を継承して、新しいメソッドを付け足す = dictのサブクラスとしてPictures
class Pictures(dict):
    def __missing__(self, key: str):
        value = open_picture(key)
        self[key] = value
        return value
    
pictures = Pictures()
handle = pictures[path] # ここでキーのpathがなければ上で定義した__missing__が呼ばれる
handle.seek(0)
image_data = handle.read()


image_data


def get_stats(numbers: int):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)

print(f"Min: {minimum}\nMax: {maximum}")


first, second = 1, 2
assert first == 1
assert second == 2

def my_funciton():
    return 1, 2

first, second = my_funciton()
assert first == 1
assert second == 2


def get_avg_ration(numbers: List[int])->List[float]:
    average = sum(numbers) / len(numbers)
    scaled = [x/average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

longest, *middle, shortest = get_avg_ration(lengths)

print(f"Longest: {longest:>4.0get_ipython().run_line_magic("}")", "")
print(f"Shortest: {shortest:>4.0get_ipython().run_line_magic("}")", "")


def get_stats(numbers: List[int]):
    minimum = min(numbers)
    maximum = max(numbers)
    
    count = len(numbers)
    average = sum(numbers) / count
    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle-1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
        
    return minimum, maximum, average, median, count


minimum, maximum, average, median, count = get_stats(lengths)

print(minimum, maximum, average, median, count)


def careful_divide(a: float, b: float)->float:
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print("Invalid inputs")


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.
    
    Raises:
        ValueError: When the inputs cannot be divieded
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")


def sort_priority(values, group):
    """ priority sort
    
    """
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sort_priority(numbers, group)
print(numbers)


from typing import List, Set

def sort_priority2(numbers: List[int], group: Set[int]) -> bool:
    found = False # scope: sort_priority2
    def helper(x):
        if x in group:
            found = True # scope: helper - not good
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print("Found: ", found)
print(numbers)


def sort_priority3(numbers: List[int], group: Set[int]) -> bool:
    found = False 
    def helper(x):
        nonlocal found # new
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False
        
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)
    
sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")
        
log("My numbers are ", [1, 2])
log("Hi there", [])


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")
        
log("My numbers are ", [1, 2])
log("Hi there")


favorites = [7, 33, 99]
log("Favorite colors", *favorites)


def my_generator():
    for i in range(10):
        yield i
        
def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)


def remainder(number: int, divisor: int) -> int:
    return number % divisor

assert remainder(20, 7) == 6


my_kwargs = {
    "number": 20,
    "divisor": 7,
}

assert remainder(**my_kwargs) == 6


def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
print_parameters(alpha=1.5, beta=9, gamma=4)


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f"{flow:.3} kg per second")


def flow_rate(weight_diff: float, time_diff: float, period=1) -> float:
    return ( weight_diff / time_diff ) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)


def flow_rate(weight_diff: float, time_diff: float,
              period=1, units_per_kg=1) -> float:
    return ( (weight_diff * units_per_kg) / time_diff ) * period


pounds_per_hour = flow_rate(weight_diff, time_diff,
                           period=3600, units_per_kg=2.2)


# 関数が呼ばれるたびにデフォルト引数が評価されるものと仮定
from time import sleep
from datetime import datetime

def log(message, when=datetime.now()):
    print(f"{when}: {message}")
    
log("Hi thereget_ipython().getoutput("")")


sleep(0.1)
log("Hi againget_ipython().getoutput("")")


# default 引数はモジュールの読み込み時にしか評価されない

def log(message, when=None):
    """Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


log("Hi thereget_ipython().getoutput("")")
sleep(0.1)
log("Hi again")


import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print("Foo: ", foo)
print("Bar: ", bar)


assert foo is bar


def decode(data, default=None):
    """Load JSON data from a string.
    
    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode("bad data")
foo["stuff"] = 5
bar =decode("also bad")
bar["meep"] = 1
print("Foo: ", foo)
print("Bar: ", bar)
assert foo is not bar


from typing import Optional

def log_typed(message: str, 
             when: Optional[datetime]=None) -> None:
    """Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f"{when}: {message}")


def safe_division(number, divisor, ignore_overflow,
                 ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division(1.0, 10**500, True, False)
print(result)


result = safe_division(1.0, 0, False, True)
print(result)


def safe_division_b(number, divisor, ignore_overflow=False,
                 ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result)


result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result)


assert safe_division_b(1.0, 10**500, True, False) == 0


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                   ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


result = safe_division_c(1.0, 0, True, False)


result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float("inf")


try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    pass # 期待通り


assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) == 0.4



# def safe_division_d(numerator, denominator, /, *,
#                   ignore_overflow=False,
#                   ignore_zero_division=False):
#    try:
#        return number / divisor
#    except OverflowError:
#       if ignore_overflow:
#           return 0
#       else:
#           raise
#   except ZeroDivisionError:
#       if ignore_zero_division:
#           return float("inf")
#       else:
#           raise


get_ipython().getoutput("python3 --version")


# 位置専用引数が使えるのはpython3.8から
# '/,'で位置引数の終わりを示す


def trace(func):
    def wrapper(*args, **kwargs):
        result= func(*args, **kwargs)
        print(f"{func.__name__}{argsget_ipython().getoutput("r}, {kwargs!r}"")
             f"-> {resultget_ipython().getoutput("r}")")
        return result
    return wrapper


# equal fibonacci = trace(fibonacci)

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number

    """
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(4)


print(fibonacci)


# this function like this which is defined as decorator disturbs degub tools


help(fibonacci)


import pickle

pickle.dumps(fibonacci)


from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result= func(*args, **kwargs)
        print(f"{func.__name__}{argsget_ipython().getoutput("r}, {kwargs!r}"")
             f"-> {resultget_ipython().getoutput("r}")")
        return result
    return wrapper


@trace
def fibonacci(n):
    """Return the n-th Fibonacci number

    """
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(4)


print(fibonacci)


help(fibonacci)


import pickle

pickle.dumps(fibonacci)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for x in a:
    squares.append(x**2)
print(squares)


squares = [x**2 for x in a]


print(squares)


alt = map(lambda x: x ** 2, a)


even_squares = [x**2 for x in a if x % 2 == 0]


print(even_squares)


alt = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))


assert even_squares == list(alt)


even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
three_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_squares_dict)
print(three_cubed_set)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]


print(b, c)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
           for row in matrix if sum(row) >= 10]
print(filtered)


stock = {
    "nails": 25,
    "screws": 35,
    "wingnuts": 8,
    "washers": 24,
}

order = ["screws", "wingnuts", "clips"]

def get_batches(count: int, size: int) -> int:
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches
        
print(result)


found = {name: get_batches(stock.get(name, 0), 8)
        for name in order
        if get_batches(stock.get(name, 0), 8)}
print(found)


found = {name: batches for name in order
      if (batches := get_batches(stock.get(name, 0), 8))}


print(found)


get_ipython().getoutput("python --version")


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result
    


address = "Four score and seven years ago ..."
result = index_words(address)
print(result[:10])


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


it = index_words_iter(address)
print(next(it))
print(next(it))


result = list(index_words_iter(address))
print(result)


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset


from itertools import islice

with open("address.txt", "r") as f:
    it = index_file(f)
    results = islice(it, 0, 5)
    print(list(results))


from typing import List


def normalize(numbers: List[float]):
    total = sum(numbers) # ここと
    result = []
    # ここで別々に__iter__を呼び出す。
    # __iter__が呼び出され時にファイルから読み込むから複数回入力データを読み込む
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100


def read_visits(data_path):
    """generator to read int numbers in the file
    """
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits("my_numbers.txt")
#percentages = normalize(it)
print(list(it))
print(list(it)) # iteration process is already finished!


def normailze_copy(numbers: List[int]):
    numbers = list(numbers) # duplicate iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits("my_numbers.txt")
percentages = normailze_copy(it)
print(percentages)
assert sum(percentages) == 100


def normalize_func(get_iter):
    total = sum(get_iter()) # new iterator
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


path = "my_numbers.txt"
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100


class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
                
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100


def normalize_defensive(numbers):
    if iter(numbers) is numbers: # raise Error if numbers type is Iterator
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages)

Visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)



import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')


value = [len(x) for x in open("my_file.txt")]
print(value)


it = (len(x) for x in open("my_file.txt"))
print(it)


print(next(it))


print(next(it))


# can create the value from "generator", so we can prevent it from out of memeory


roots = ((x, x**0.5) for x in it)


print(next(roots))


def move(period, speed):
    for _ in range(period):
        yield speed
        
def pause(delay):
    for _ in range(delay):
        yield 0
    


# hard to see

def animate():
    for delta in move(4, 5.0):
        yield delta
    for delta in pause(3):
        yield delta
    for delta in move(2, 3.0):
        yield delta


def render(delta):
    #print(f"Delta: {delta:.1f}")
    # somethin process to let image move
    # ...
    pass

def run(func):
    for delta in func():
        render(delta)


run(animate)


# easy to see since using "yield from ~ "
def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(3, 3.0)
    
run(animate_composed)


get_ipython().run_cell_magic("timeit", "", """run(animate)""")


get_ipython().run_cell_magic("timeit", "", """run(animate_composed)""")


import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

def transmit(output):
    if output is None:
        print(f"Output is None")
    else:
        print(f"Output: {output:>5.1f}")
        
def run(it):
    for output in it:
        transmit(output)


run(wave(3.0, 8))


def my_generator():
    received = yield 1
    print(f"received = {received}")
    
it = iter(my_generator())
output = next(it)
print(f"output = {output}")
      
try:
      next(it)
except StopIteration:
      pass
else:
      assert False


it = iter(my_generator())
output = it.send(None) # get output of first generator
print(f"output = {output}")

try:
    it.send("Helloget_ipython().getoutput("") # send to generator")
except StopIteration:
    pass


# 入力信号に基づいて正弦波の振幅を変調する
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield # receive the first
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output # receive the next


def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10,
    ]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))


def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)
    
run(complex_wave())


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)
    
run_modulating(complex_wave_modulating())


def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # get next value
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)
    
def run_cascading():
    amplitudes = [
        7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10,
    ]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)
        
run_cascading()





class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3
    
it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError("test error")))


def my_generator():
    yield 1
    
    try:
        yield 2
    except MyError:
        print("Got MyError")
    else:
        yield 3
    
    yield 4
    
it = my_generator()
print(next(it))
print(next(it))
print(it.throw(MyError("test error")))


class Reset(Exception):
    pass

def timer(period):
    current = period #copy?
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period
            
def check_for_reset():
    # 外部イベントをボーリングして待つ
    # ...
    pass

def annouce(remaining):
    print(f"{remaining} ticks remaining")
    
def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            annouce(current)
            
run()


class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period
        
    def reset(self):
        self.current = self.period
    
    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        annouce(current)
run()


import itertools

# chain
it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))


# repeat
it = itertools.repeat("hello", 3)
print(list(it))


# cycle
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)


it1, it2, it3 = itertools.tee(["first", "second"], 3)
print(list(it1))
print(list(it2))
print(list(it3))


class SimpleGradebook:
    def __init__(self):
        self._grades = {}
        
    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)
        
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradebook()
book.add_student("Issac Newton")
book.report_grade("Issac Newton", 90)
book.report_grade("Issac Newton", 95)
book.report_grade("Issac Newton", 85)

print(book.average_grade("Issac Newton"))


from collections import defaultdict

class BySubjectGradebook:
    def __init__(self):
        self._grades = {}
        
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
        
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)
        
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradebook()
book.add_student("Albert Einstein")
book.report_grade("Albert Einstein", "Math", 75)
book.report_grade("Albert Einstein", "Math", 65)
book.report_grade("Albert Einstein", "Gym", 90)
book.report_grade("Albert Einstein", "Gym", 95)
print(book.average_grade("Albert Einstein"))


from collections import namedtuple

Grade = namedtuple("Grade", ("score", "weight"))


class Subject:
    def __init__(self):
        self._grades = []
        
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
        
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)
        
    def get_subject(self, name):
        return self._subjects[name]
    
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)
        
    def get_student(self, name):
        return self._students[name]


book = Gradebook()
albert = book.get_student("Albert Einstein")
math = albert.get_subject("Math")
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject("Gym")
gym.report_grade(100, 0.40)
gym.report_grade(85, 0.60)
print(albert.average_grade())


names = ["Socrates", "Arichimedes", "Plato", "Aristotle"]
names.sort(key=len)
print(names)


def log_missing():
    print("Key added")
    return 0


from collections import defaultdict

current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]

result = defaultdict(log_missing, current)
print("Before: ", dict(result))
for key, amount in increments:
    result[key] += amount
print("After: ", dict(result))


def increment_with_report(current, increments):
    added_count = 0
    
    def missing():
        nonlocal added_count # state full clouja
        added_count += 1
        return 0
    
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
        
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


class CountMissing:
    def __init__(self):
        self.added = 0
        
    def missing(self):
        self.added += 1
        return 0
    


counter = CountMissing()
result = defaultdict(counter.missing, current) # reference method
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


class BetterCountMissing:
    def __init__(self):
        self.added = 0
        
    def __call__(self):
        self.added += 1
        return 0
    
counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)


counter = BetterCountMissing()
result = defaultdict(counter, current) # trust __call__ method
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


class InputData:
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
        
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplemetedError


# concreteness class
class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read.read()
        self.result = data.count("\n")
        
    def reduce(self, other):
        self.result += other.result


import os
from pathlib import Path

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


import os
import random


def write_test_files(tmpdir):
    os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), "w") as f:
            f.write("\n" * random.randint(0, 100))
            
tmpdir = "test_inputs"
#write_test_files(tmpdir)

result = mapreduce(tmpdir)
print(f"There are {result} lines")


class GenericInputData:
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()
        
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data):
            yield cls(os.path.join(data_dir, name))



class GenericWorker:
    def __init__(self, input_data):
        self.input_dta = input_data
        self.result = None
        
    def map(self):
        raise NotImplementedError
        
    def reduce(self, other):
        raise NotImplementedError
    
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers



class LineCountWorker(GenericWorker):
    pass


class MyBaseClass:
    def __init__(self, value):
        self.value = value
        
class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo:
    def __init__(self):
        self.value *= 2
        
class PlusFive:
    def __init__(self):
        self.value += 5
    


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print(f"First ordering is (5 * 2) + 5 = ", foo.value)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print("Second ordering still is", bar.value)


class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7
        
class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9


class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)


foo = ThisWay(5)
print("Should be (5 * 7) + 9 = 44 but is ", foo.value)


class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7
        
class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9



class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)
        
foo = GoodWay(5)
print("Should be 7 * (5 + 9) = 98 and is", foo.value)


mro_str = "\n".join(repr(cls) for cls in GoodWay.mro())
print(mro_str)


class ExplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


x = np.arange(-1,1)
y = x ** 3

plt.plot(x, y)
plt.grid()
plt.show()



class AutomaticTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3
        
class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3



assert ExplicitTrisect(9).value == 3
assert AutomaticTrisect(9).value == 3
assert ImplicitTrisect(9).value == 3


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
    
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
            
        else:
            return value
    


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(
    10, left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11))
)


print(repr(tree.to_dict()))


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent
    
    # solution:
    # we should only process the needed value and prevent it from the cycle
    # so, override _traverse method
    def _traverse(self, key, value):
        if (isinstance(value, BinaryTreeWithParent)) and (key == "parent"):
            return value.value # prevent it from the cycle
        else:
            return super()._traverse(key, value)
        


from pprint import pprint

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
pprint(root.to_dict())


class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent
        
my_tree = NamedSubTree("foobar", root.left.right)
pprint(my_tree.to_dict()) # not infinity loop


import json


class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    


from dataclasses import dataclass
from typing import Dict

class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [
            Machine(**kwargs) for kwargs in machines
        ]


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports=None, speed=None):
        self.ports = ports
        self.speed = speed

        
class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores=None, ram=None, disk=None):
        self.cores = cores
        self.ram = ram
        self.disk = disk




serialized = """{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [
        {"cores": 8, "ram": 32e9, "disk": 5e12},
        {"cores": 4, "ram": 16e9, "disk": 1e12},
        {"cores": 2, "ram": 4e9, "disk": 500e9}
    ]
}"""

deserialized = DatacenterRack.from_json(serialized)
roundtrip = deserialized.to_json()
assert json.loads(serialized) == json.loads(roundtrip)


class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10
        
    def get_private_field(self):
        return self.__private_field


foo = MyObject()
assert foo.public_field == 5


assert foo.get_private_field() == 10


foo.__private_field


class MyOtherObject:
    def __init__(self):
        self.__private_field = 71
        
    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field
    
    
bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71


bar.__dict__


class ApiClass:
    def __init__(self):
        self.__value = 5
        
    def get(self):
        return self.__value

    
class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = "Helloget_ipython().getoutput("!" # OK!")
        
a = Child()
print(f"{a.get()} and {a._value} are difference")


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)
        
    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


foo = FrequencyList(["a", "b", "a", "c", "b", "a", "d"])
print("Length is",  len(foo))
foo.pop()
print("After pop:", repr(foo))
print("Frequency:", foo.frequency())


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bar = [1, 2, 3]
bar[0]


bar.__getitem__(0)


class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f"Index {index} is out of range.")



trees = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6,
            right=IndexableNode(7),

        ),
    ),
    right=IndexableNode(
        15,
        left=IndexableNode(11),
    ),
)


print('LRR is', trees.left.right.right.value) 
print('Index 0 is', trees[0])
print('Index 1 is', trees[1])
print('11 in the tree?', 11 in trees)
print('17 in the tree?', 17 in trees)
print('Tree is', list(trees))


len(tree)


class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count



tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6,
            right=SequenceNode(7),

        ),
    ),
    right=SequenceNode(
        15,
        left=SequenceNode(11),
    ),
)


print('Tree length is', len(tree))


list(tree)


from collections.abc import Sequence

class BadType(Sequence):
    pass

foo = BadType()



class BetterNode(SequenceNode, Sequence):
    pass


tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6,
            right=BetterNode(7)
        )
    ),
    right=BetterNode(
        15,
        left=BetterNode(11)
    )
)


tree.index(7)


tree.count(10)



