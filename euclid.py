a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
import random

def euclid3(a, b):
    while b != 0:
        a, b = b, a % b
    c = a
    print("最大公約数は" + str(c) + "です")
    
def euclid4(a, b):
    while b != 0:
        a, b = b, a % b
    c = a
    if c == 1:
        print (True)
    else:  
        print(False)

def extra(a, b):
    p = 0
    for i in range(100000):
        a, b = random.sample(range(1, 10000), 2)
        while b != 0:
            a, b = b, a % b
        c = a
        if c == 1:
            p += 1
    print("各組が互いに素である確率は" + str(p / 100000) + "です")

euclid3(a, b)
euclid4(a, b)
extra(a, b)

from math import pi

print(6 / (pi ** 2))