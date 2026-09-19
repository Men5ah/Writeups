# Let's Warm Up

Category: #General_Skills 
Level: #Easy 
Author: #Sanjay_C/Danny_Tunitis 
Tags:

---

## Challenge

> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Files

- none

## Hints

1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

---

## Initial Observations

This is a warmup to general skills in CTFs, shouldn't be too difficult since it's labeled easy.

---

## Analysis

At first glance, the challenge gives us `0x70` in hexadecimal. To get the flag,  I need to figure out what `0x70` translates to in ASCII. By using CyberChef, I can convert the hexadecimal value to it's ASCII form, which is a 'p'.

---

## Solution

### Commands

```bash

```

### Python (if applicable)

```python

```

### Other Tools

- CyberChef ("From Hex" recipe)

---

## Flag

```
picoCTF{p}
```

---

## ## Key Takeaways

- Hexadecimal is just an alternate base representation of the same byte value that maps to ASCII — converting between them is a matter of encoding, not "hacking."
- CyberChef is a fast, reliable GUI tool for quick encoding/decoding conversions (hex, base64, binary, etc.) without needing to write custom scripts.
- Simple conversions can be cross-checked quickly using built-in language functions, e.g., Python's `chr()` and `ord()` for character/code point conversions.
- Warmup challenges often test basic encoding literacy (hex, ASCII, base64) since these come up constantly in later, more complex challenges.

---

## References

- https://gchq.github.io/CyberChef/
- https://www.ascii-code.com/

## Related Concepts

- Hexadecimal Encoding
- ASCII Character Encoding
- Base Conversion
- CyberChef Recipes
- [[3-2warm]]