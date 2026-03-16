# XOR Properties

**Category:** XOR
**Points:** 15

This challenge explores the algebraic properties of XOR and demonstrates how to reverse a multi-layer XOR encryption chain.
By applying XOR identities, we can recover hidden keys and ultimately extract the plaintext.

---

##  What I Learned

* XOR properties: commutativity, associativity, self-inverse
* Why XOR is reversible: `X ^ K ^ K = X`
* How multi-layer XOR chains can be undone step by step
* How to decode hex strings using `binascii.unhexlify`
* How to implement byte-wise XOR in Python
* How XOR cancellation helps reveal unknown keys in cryptography

---

##  Method

### 1. Decode hex strings into bytes

```python
from binascii import unhexlify
KEY1 = unhexlify("a6c8...")
```

### 2. Implement bytewise XOR

```python
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
```

### 3. Use XOR algebra to recover the keys

* `(KEY2 ^ KEY1) ^ KEY1 = KEY2`
* `(KEY2 ^ KEY3) ^ KEY2 = KEY3`

### 4. Undo the full chain

```
FLAG = (FLAG ^ KEY1 ^ KEY2 ^ KEY3) ^ KEY1 ^ KEY2 ^ KEY3
```

All keys appear twice → they cancel → only the flag remains.

### 5. Combine them into code

(Flag intentionally omitted)

---

##  Status

Challenge solved on CryptoHack.
The actual flag is **not included** in this repository to follow CryptoHack rules.
