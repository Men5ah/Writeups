---
publish: true
---

# 2-Warmed Up

Category: #General_Skills 
Level: #Easy 
Author: #Sanjay_C #Danny_Tunitis 
Tags: 

---

## Challenge

> What is 0x3D (base 16) in decimal (base 10)?

## Files

- None

## Hints

1. Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

---

## Initial Observations

My initial observation is that the challenge involves base conversions, simple enough. From base 16 to base 10.

---

## Analysis

Number base conversions can be done with some simple arithmetic. In this challenge, it is a to change a figure in base 16 (hexadecimal) to base 10 (decimal). To do this, I need to think about how numbers are represented in terms of their place values.

In base 10, let's take 159 for example. This has 3 place values; ones, tens, and hundreds. The summation of these 3 values creates 159 i.e. $(1*100)+(5*10)+(9*1) = 159$

Notice another thing, there is a relationship between the numbers on the right. they are all powers of 10 i.e. $100 = 10^2$, $10=10^1$, and $1=10^0$.

So if I need to convert from any base to base 10, I have to keep that in mind. For base 16, since the challenge has 2 places, the conversions will use the ones and "sixteens"places. One of the "numbers" in the challenge is a letter. This is part of the base 16 system. Base 16 includes numbers from 0 through 15, however the numbers 10-15 are represented by letters, so A -> 10 and so on.

---

## Solution

Converting by hand results in:

$(3*16^1)+(D*16^0)$
$(3*16^1)+(13*16^0)$
$48+13$
$61$

In CyberChef, it looks like this:
![[Pasted image 20260728211914.png]]
### Python (if applicable)

```python
# Base 16 to base 10 converter
to_convert = '0x3D'
print(int(to_convert, 16))
```

### Other Tools

- CyberChef
- - [Base Converter](https://www.rapidtables.com/convert/number/base-converter.html)
---

## Flag

```
picoCTF{61}
```

---

## Key Takeaways

- Hexadecimal (base 16) uses the digits `0–9` and the letters `A–F`, where `A = 10` through `F = 15`.
- Any number can be converted to decimal by multiplying each digit by its corresponding power of the base and summing the results.
- The `0x` prefix is commonly used to indicate that a number is written in hexadecimal.
- Python's built-in `int()` function can convert numbers from different bases by specifying the base as the second argument (e.g., `int("3D", 16)`).
- Understanding hexadecimal is an essential skill for cybersecurity, as it is frequently used to represent memory addresses, machine code, binary data, and encoded values.
---

## References

- https://mathbits.com/MathBits/CompSci/Introduction/tobase10.htm