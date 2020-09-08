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
# Dict型を継承して、新しいメソッドを付け足す
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



