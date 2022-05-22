for n in range(100, 1000):
    a = n // 100
    b = n % 100 // 10
    c = n % 10
    if a * a * a + b * b * b + c * c * c == n:
        print(n)
