# This script computes the two congruences given in the challenge.
# Final numeric outputs are intentionally NOT stored or committed,
# in accordance with CryptoHack guidelines.

def compute_modular_values():
    # First congruence: 11 ≡ x (mod 6)
    x = 11 % 6

    # Second congruence: 8146798528947 ≡ y (mod 17)
    y = 8146798528947 % 17

    # Compare the two results and keep the smaller value
    result = min(x, y)

    # Debug-style prints for local use only
    print("x =", x)
    print("y =", y)
    print("min(x, y) =", result)


if __name__ == "__main__":
    compute_modular_values()
