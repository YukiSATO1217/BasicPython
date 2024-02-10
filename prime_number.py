a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO
def pri(a):

    try:
        a = int(a)
        if a <= 0:
            return "エラー"
        elif a == 1:
            return False
        else:
            for i in range(2, a):
                if a % i == 0:
                    return False
            else:
                return True
    except ValueError:
        return "エラー"
print(pri(a))
print(pri(b))

    if "." in a:
        print("エラー")
    else:
        a = int(a)
        if a <= 0:
            print("エラー")
        elif a == 1:
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

