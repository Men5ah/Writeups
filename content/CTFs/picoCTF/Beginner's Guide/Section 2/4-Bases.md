---
publish: true
---

# Bases

Category: #General_Skills  
Level: #Easy 
Author: #Sanjay_C #Danny_Tunitis 
Tags:

---

## Challenge

> What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

## Files

- None

## Hints

1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
---

## Initial Observations

It is immediately clear that this is encoded text rather than plain English. Since the challenge title is _Bases_, I'll investigate whether it has been encoded using a base encoding scheme such as Base64.

---

## Analysis

Instead of checking manually, I will check with CyberChef to see what is going on. It doesn't seem to be a ROT3 or ROT13 Caesar Cipher, so I'll check the Data format next.  The string contains only letters and numbers, has no spaces or punctuation, and its length is a multiple of four. These are common characteristics of Base64-encoded data, making Base64 a likely candidate.

---

## Solution

![[Pasted image 20260728220310.png]]
### Python (if applicable)

```python
import base64
# Base 64 to plaintext converter
to_convert = 'bDNhcm5fdGgzX3IwcDM1'
print(base64.b64decode(to_convert).decode())
```

### Other Tools

- CyberChef

---

## Flag

```
picoCTF{l3arn_th3_r0p35}
```

---

## Key Takeaways

- Base64 is an encoding scheme, not an encryption algorithm. It is designed to represent binary data using printable ASCII characters.
- Base64 uses a character set consisting of uppercase letters, lowercase letters, digits, `+`, and `/`, with `=` sometimes used as padding.
- Encoded Base64 strings can often be identified by their character set and lengths that are multiples of four.
- CyberChef provides a quick way to identify and decode common encoding schemes such as Base64.
- Python's built-in `base64` module can be used to encode and decode Base64 data programmatically.

---

## References

- picoCTF - Bases Challenge
- https://en.wikipedia.org/wiki/Base64
- https://docs.python.org/3/library/base64.html
- https://gchq.github.io/CyberChef/

## Related Concepts

- Base64 Encoding
- Character Encoding
- Binary-to-Text Encoding
- CyberChef
- Python `base64` Module