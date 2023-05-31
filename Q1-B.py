primenum = [h for h in range(1, 1001) if all(h % i != 0 for i in range(2, int(h**0.5) + 1))]
print(primenum)
