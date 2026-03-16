# Greatest Common Divisor – CryptoHack Solution

def gcd(a, b):
    """Compute the GCD using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

a = 66528
b = 52920

answer = gcd(a, b)
print(answer)
