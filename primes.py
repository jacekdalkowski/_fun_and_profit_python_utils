
def gen_primes():
    n = 2
    primes = set()
    while n < 5000:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

primes = list(gen_primes())
print primes