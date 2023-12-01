a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a = int(a)
b = int(b)

if a == 1:
    print("素数ではありません")
else:
    for i in range(2, a):
        if a % i == 0:
            print("素数ではありません")
            break
    else:
        print("素数です")

if b == 1:
    print("素数ではありません")
else:
    for i in range(2, b):
        if b % i == 0:
            print("素数ではありません")
            break
    else:
        print("素数です")
