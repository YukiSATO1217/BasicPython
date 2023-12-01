a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
while b != 0:
    a, b = b, a % b
c = a

print("最大公約数は" + str(c) +"です")