a = input("aの値を入力: ")
b = input("bの値を入力: ")

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