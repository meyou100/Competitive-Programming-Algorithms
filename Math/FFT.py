from typing import List
import math

#coeffs must be given in the form a_0 + a_1 x + a_2 x^2 ...
def fft(coeffs: List[float]) -> List[float]:
    n = len(coeffs)
    if n == 1:
        return coeffs

    w = math.e ** (2j * math.pi / n)
    y_even, y_odd = fft(coeffs[::2]), fft(coeffs[1::2])
    y = [0] * n
    for i in range(n // 2):
        y[i] = y_even[i] + w ** i * y_odd[i]
        y[i + n // 2] = y_even[i] - w ** i * y_odd[i]
    return y

def ifft(coeffs: List[float]) -> List[float]:
    n = len(coeffs)
    if n == 1:
        return coeffs

    w = math.e ** (-2j * math.pi / n)
    y_even, y_odd = ifft(coeffs[::2]), ifft(coeffs[1::2])
    y = [0] * n
    for i in range(n // 2):
        y[i] = y_even[i] + w ** i * y_odd[i]
        y[i + n // 2] = y_even[i] - w ** i * y_odd[i]
    return y

a, b = fft([1,2,3,4,0,0,0,0]), fft([4,5,6,7,0,0,0,0])
c = []
for i in range(8):
    c.append(a[i] * b[i])
print([a.real / 8 for a in ifft(c)])
