def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 305, 64, 53]

squares = list(map(lambda x: x ** 2, a))
print(squares)

primes = list(filter(is_prime, a))
print(primes)


