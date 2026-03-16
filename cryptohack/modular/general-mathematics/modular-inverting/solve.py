"""
Modular Inverting — Multiplicative Inverse in F_p

This module demonstrates how to compute a modular multiplicative inverse
using Fermat's Little Theorem, assuming the modulus p is prime.

The numerical result is intentionally omitted from version control,
following CryptoHack rules.
"""

def modexp(a: int, e: int, m: int) -> int:
    """Fast modular exponentiation using Python's pow()."""
    return pow(a, e, m)


def inverse_mod_prime(a: int, p: int) -> int:
    """
    Compute the multiplicative inverse of a modulo p,
    using Fermat's Little Theorem: a^(p-2) mod p.
    Valid only when p is prime and a is not divisible by p.
    """
    return modexp(a, p - 2, p)


def main():
    a = 3
    p = 13

    inv = inverse_mod_prime(a, p)

    # Debug print for personal learning (safe to keep)
    print(f"Inverse of {a} mod {p} =", inv)


if __name__ == "__main__":
    main()
