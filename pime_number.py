def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit=50):
    primes = [n for n in range(2, limit+1) if is_prime(n)]
    return primes

if __name__ == "__main__":
    primes = generate_primes(50)
    print("Prime numbers up to 50:")
    print(primes)
