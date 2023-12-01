from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi

a = sin(0 * pi)
b = sin(pi / 2)
N = 100
h = (b - a) / N
S=0

for k in range(1,N + 1):
    S += (h / 2) * ((a + (k - 1) * h) + (a + k * h))
print(S)