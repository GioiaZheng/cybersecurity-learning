# You either know, XOR you don't — Notes

This is the final XOR challenge in the *Introduction* course.  
It combines everything learned so far:

- Hex decoding  
- XOR as a reversible operation  
- Single-byte and multi-byte XOR  
- Using **known plaintext** to recover a secret key  

The ciphertext given by the challenge is:

```text
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
````

Our goal is to find the flag, in the usual format `crypto{...}`.

---

## 1. First observation — it’s hex, not raw bytes

The string we see is hexadecimal.
To do XOR, we must first convert it into bytes.

```python
from binascii import unhexlify

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = unhexlify(cipher_hex)
```

At this point:

* `cipher_hex` is a **string of hex characters**
* `cipher` is a **bytes object**, the real data we can XOR

Why this step is necessary:

> XOR works on numbers / bytes, not on ASCII hex digits.

---

## 2. Key idea — remember the flag format

The challenge hint says:

> "Remember the flag format and how it might help you."

On CryptoHack, flags always look like:

```text
crypto{something_here}
```

That means we almost certainly know the **first 7 characters** of the plaintext:

```text
"crypto{"
```

So we know:

* `plaintext[0..6]  = "crypto{"`
* `ciphertext[0..6] = cipher[:7]` (from the bytes we decoded)

This is called a **known-plaintext attack**:
we know part of the message, so we can use it to recover the key.

---

## 3. XOR property — recovering the key

Encryption with XOR usually looks like:

```text
C = P ^ K
```

Where:

* `C` = ciphertext
* `P` = plaintext
* `K` = key (or part of the key)

Because XOR is self-inverse:

```text
P = C ^ K
K = C ^ P
```

So if we know `C` and `P`, we can get `K`.

For each position `i` in the first 7 bytes:

```text
key[i] = cipher[i] ^ ord("crypto{"[i])
```

In Python:

```python
known_plain = b"crypto{"
partial_key = bytes([c ^ p for c, p in zip(cipher[:7], known_plain)])
print(partial_key)
```

This reveals the **first few bytes of the key**.

---

## 4. Recognizing a pattern in the key

When we compute `partial_key`, we get something that looks like readable ASCII:

```text
b"myXORke"
```

This looks very suspiciously like English:

> "myXORke"

It is natural to guess that the full key is:

```text
b"myXORkey"
```

So the full key is probably:

```python
key = b"myXORkey"
```

This is an **8-byte key**.
The cipher is most likely encrypted with a **repeating-key XOR**:

```text
cipher[i] = plaintext[i] ^ key[i % len(key)]
```

This is similar in spirit to a Vigenère cipher, but operating on bytes.

---

## 5. Decrypting with a repeating XOR key

Now we apply the guessed key across the whole ciphertext:

```python
key = b"myXORkey"

plaintext = bytes(
    [c ^ key[i % len(key)] for i, c in enumerate(cipher)]
)

print(plaintext.decode())
```

Explanation:

* `enumerate(cipher)` gives us both the index `i` and byte `c`
* `key[i % len(key)]` cycles through the key: 0,1,2,...,7,0,1,2,...
* We XOR each ciphertext byte with the corresponding key byte
* The result is a new bytes object, which we decode as UTF-8 text

The output is a nice readable string starting with `crypto{...}` —
this is the flag.

(Flag is intentionally omitted here.)

---

## 6. Why this challenge is important

This challenge teaches several key concepts:

1. **Hex decoding**
   Using `binascii.unhexlify` to turn hex into bytes.

2. **Known-plaintext attack**
   If you know part of the message (like `crypto{`), you can often recover part
   of the key using `key = ciphertext ^ plaintext`.

3. **Recognizing structure in keys**
   Seeing `b"myXORke"` suggests the full key is `b"myXORkey"`.

4. **Repeating-key XOR**
   Many ciphers (and a lot of CTF challenges) encrypt using a short key that is
   repeated over the whole message.

5. **XOR reversibility**
   The same operation used for encryption (XOR with key) is also used
   for decryption.

---

## 7. Summary

* Convert hex to bytes with `unhexlify`
* Use the known flag prefix `"crypto{"` to recover a part of the key
* Notice the partial key is human-readable and guess the full key
* Apply repeating-key XOR decryption to the whole ciphertext
* Obtain the flag in the format `crypto{...}`

Flag is intentionally not included in this repository.
