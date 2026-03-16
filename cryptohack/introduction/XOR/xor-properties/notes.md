# XOR Properties — Notes

This challenge demonstrates how to use the algebraic properties of XOR to
undo a chain of encryptions and recover the flag. The goal is not only to
solve the problem but to build intuition for how XOR behaves in cryptographic
constructions such as stream ciphers, OTP, CTR mode, mask generation, and
many CTF-style XOR chains.

---

##  XOR Properties Used

We rely on four essential identities:

### **1. Commutative**
```

A ^ B = B ^ A

```

### **2. Associative**
```

(A ^ B) ^ C = A ^ (B ^ C)

```

### **3. Identity**
```

A ^ 0 = A

```

### **4. Self-inverse**
```

A ^ A = 0

```

These make XOR reversible:

```

(X ^ K) ^ K = X

````

This principle allows us to “cancel out” keys by XORing the same key again.

---

##  Converting Hex Strings to Bytes — `binascii.unhexlify`

The challenge provides hex-encoded strings.  
Before XORing them, we must convert them into `bytes`.

### What `unhexlify()` does:
```python
from binascii import unhexlify
unhexlify("414243")  # b'ABC'
````

It:

* Takes a hex string (`"41"`, `"42"`, `"43"`)
* Converts each pair into a byte
* Returns a `bytes` object

Hex → Bytes is essential because XOR operates on raw bytes, not hex strings.

---

##  Implementing Bytewise XOR

We define a helper function:

```python
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])
```

### Step-by-step breakdown:

#### **1. `zip(a, b)`**

Pairs each byte:

```
zip(b"\x01\x02", b"\x10\x20")
→ (1,16), (2,32)
```

#### **2. List comprehension**

```
[x ^ y for (x,y)] → bytewise XOR
```

#### **3. `bytes([...])`**

Converts the list of integers back into a bytes sequence.

This function is reusable across many CryptoHack XOR problems.

---

##  Step-by-Step Decryption Logic

We are given four lines:

```
KEY1 = a6c8...
KEY2 ^ KEY1 = 37dc...
KEY2 ^ KEY3 = c154...
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee...
```

### **Step 1 — Recover KEY2**

Using:

```
(KEY2 ^ KEY1) ^ KEY1 = KEY2
```

### **Step 2 — Recover KEY3**

Using:

```
(KEY2 ^ KEY3) ^ KEY2 = KEY3
```

### **Step 3 — Recover the FLAG**

Final expression:

```
FLAG ^ KEY1 ^ KEY3 ^ KEY2
```

Re-XOR with all three keys:

```
FLAG = FLAG_XOR ^ KEY1 ^ KEY2 ^ KEY3
```

Every key appears exactly twice → all cancel out → only FLAG remains.

---

##  Summary

* `unhexlify()` converts hex strings to raw bytes.
* The custom `xor(a, b)` function performs bytewise XOR.
* XOR algebra lets us cancel out keys and isolate the plaintext.
* The final flag is extracted by reversing the XOR chain.

Flag omitted intentionally.
