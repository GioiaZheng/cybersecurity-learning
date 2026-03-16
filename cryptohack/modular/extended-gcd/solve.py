# Extended GCD – CryptoHack Challenge

p = 26513
q = 32321

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that:
        g = gcd(a, b)
        a*x + b*y = g
    """
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


if __name__ == "__main__":
    g, u, v = extended_gcd(p, q)

    print("gcd =", g)
    print("u =", u)
    print("v =", v)
    print("Verification:", p * u + q * v)

    print("Smaller coefficient:", min(u, v))  # <- This is the challenge answer
