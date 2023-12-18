a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
def pri(a):
    if a == 1:
        print("素数ではありません")
    else:
        for i in range(2, a):
            if a % i == 0:
                print("素数ではありません")
                break
        else:
            print("素数です")
pri(a)
pri(b)