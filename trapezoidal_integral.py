from math import sin, pi, exp
# --example--
# print(sin(0))
# >>> 0
# -----------
def ti(f, a, b, N):
    h = (b - a) / N
    S = 0
    for k in range(1,N + 1):
        S += (h / 2) * (f(a + (k - 1) * h) + f(a + k * h))
    print(S)

ti(sin, 0, pi / 2, 50)
def f2(x):
    return 4 / (1 + x ** 2)
ti(f2, 0, 1, 100)
def f3(x):
    return (pi ** (1 / 2)) * exp(-x ** 2)
ti(f3, -100, 100, 1000)