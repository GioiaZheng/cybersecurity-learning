# Notes — Bytes and Big Integers

Public-key cryptosystems (like RSA) operate on integers modulo **n**.  
To encrypt a text message, we first need to convert it into an integer.

This challenge is the reverse process:  
we are given a **big integer**, and we must convert it back into bytes and then
into a readable string.

---

##  Encoding pipeline

Example with message `"HELLO"`:

1. **Text → ASCII bytes**  
   `"HELLO"` → `[72, 69, 76, 76, 79]`

2. **Bytes → hex**  
   `[0x48, 0x45, 0x4c, 0x4c, 0x4f]`

3. **Hex → big integer**  
   `0x48454c4c4f` → `310400273487`

This is how RSA represents plaintext numerically.

The challenge gives a big integer and asks us to decode it back.

---

##  PyCryptodome helper functions

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes

# bytes → integer
n = bytes_to_long(b"HELLO")

# integer → bytes
m = long_to_bytes(n)
````

Finally:

```python
m.decode()  # back into string
```

---

##  Why this matters

* RSA does **math on integers**, not on text
* Messages must be encoded into integers before encryption
* Understanding this is essential for later challenges like RSA, DH, factoring, padding Oracle, etc.

---

#  Troubleshooting Log — My Real Debug Experience

During this challenge I encountered several common cryptography-coding issues.
Here is the full record of what went wrong and how I fixed it.

---

##  **Issue 1: Mixed Python versions (3.12 & 3.13)**

At first, I installed `pycryptodome`, but Python still showed:

```
ModuleNotFoundError: No module named 'Crypto'
```

###  Reason:

My computer had **two Pythons**:

* Python **3.12** (installed manually → has pycryptodome)
* Python **3.13** (Microsoft Store → cannot access installed packages)

VS Code was accidentally using the *wrong* Python (3.13).

###  Fix:

In VS Code:

```
Ctrl + Shift + P → Python: Select Interpreter
→ Choose: C:\Python312\python.exe
```

After selecting the correct interpreter:

```bash
python --version
```

shows:

```
Python 3.12.x
```

and Crypto imports work normally.

---

#  Completion

After fixing all issues, I successfully decoded the integer using:

```python
from Crypto.Util.number import long_to_bytes
msg = long_to_bytes(n).decode()
```

The flag was correctly extracted but is not included here to respect CryptoHack rules.
