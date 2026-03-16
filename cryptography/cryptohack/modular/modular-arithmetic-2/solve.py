"""
Modular Arithmetic 2 — Solution Script

This script demonstrates how to compute modular exponentiation efficiently
using Python's built-in pow(base, exponent, modulus), which performs fast
modular exponentiation. Numerical outputs are intentionally omitted from
the repository in accordance with CryptoHack rules.
"""

def mod_exp_examples():
    p = 17
    results = {
        "3^17 mod 17": pow(3, 17, p),
        "5^17 mod 17": pow(5, 17, p),
        "7^16 mod 17": pow(7, 16, p),
    }
    return results


def fermat_prime_example():
    p = 65537
    base = 273246787654
    exponent = 65536  # p − 1
    return pow(base, exponent, p)


def main():
    examples = mod_exp_examples()
    fermat_example = fermat_prime_example()

    # Debug prints for learning purposes only
    for desc, value in examples.items():
        print(f"{desc} = {value}")

    print("base^(p-1) mod 65537 =", fermat_example)


if __name__ == "__main__":
    main()
