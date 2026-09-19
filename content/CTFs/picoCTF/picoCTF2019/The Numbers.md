---
publish: true
---

# The Numbers

Category: #Cryptography 
Level: #Easy 
Author: #Danny_Tunitis 
Tags:

---

## Challenge

> The numbers... what do they mean?


The flag is in the format PICOCTF{}

## Files

- [numbers.png](https://challenge-files.picoctf.net/c_fickle_tempest/7b39deba4212c233b1628c93f16639ed02ad90f51436d2a8914bb11f74a982d3/the_numbers.png)

## Hints

1. The flag is in the format PICOCTF{}

---

## Initial Observations

Since the challenge provides a PNG image, the first step is to inspect the file and then view the image itself. The flag may be embedded in the image or represented visually.

---

## Analysis

Downloaded the file and inspected it using `cat` and `grep` to look for the flag.

Nothing showed up so I opened the actual file with a photo viewer.

Inside there are is a string of numbers, which I can tell is the flag because it had the curly braces used in the flag.

From analysis, the flag is in the format "PICOCTF{}", it is safe to assume that each number before the opening curly brace corresponds to a letter in "PICOCTF", strongly suggesting an **A1Z26** substitution. This means that each number corresponds to its position in the alphabet which is justified because in "PICOCTF", there are 2 Cs and each C in the image is `3`.

Writing a simple Python program, I can write out the flag.

---

## Solution

### Python

```python
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

output = "".join(alphabet[number - 1] for number in numbers)

print(output)
```

### Other Tools

- Image viewer — used to inspect the contents of the PNG
- Python — used to convert the numerical values into their corresponding alphabetic characters
- CyberChef — can be used to perform A1Z26-style number-to-letter conversions

---

## Flag

```
PICOCTF{THENUMBERSMASON}
```

---

## Key Takeaways

- Information in a file does not always need to be extracted as text; sometimes the contents must be inspected visually.
- A sequence of numbers between 1 and 26 can indicate an A1Z26 substitution, where each number corresponds to a letter's position in the alphabet.
- Repeated numerical values can help confirm a suspected encoding. In this challenge, the repeated `3`s correspond to the repeated `C`s in `PICOCTF`.
- Python can automate simple substitution and character-conversion tasks, making it less error-prone than manually converting a long sequence of numbers.

---

## References

- https://www.dcode.fr/letter-number-cipher
- https://gchq.github.io/CyberChef/

## Related Concepts

- A1Z26 Cipher
- Substitution Ciphers
- Alphabetical Indexing
- Number-to-Letter Encoding
- Image Analysis
- Python String Manipulation