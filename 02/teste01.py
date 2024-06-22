import math

n = float(input("digite o valor do cateto oposto"))
n_2 = float(input("digite o valor do cateto adjacente"))

n_f = math.hypot(n, n_2)

print(f"o cateto oposto é {n} e o adjacente é{ n_2} e a hypotenusa é {n_f:.2f}")

#calcula a hipotenusa