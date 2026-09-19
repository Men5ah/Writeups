# 2warm

Category: #General_Skills 
Level: #Easy 
Author: #Sanjay_C #Danny_Tunitis 
Tags:

---

## Challenge

> Can you convert the number 42 (base 10) to binary (base 2)?

## Files

- None

## Hints

1. Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.

---

## Initial Observations

My initial observation is that the challenge involves base conversions, simple enough. From base 10 to base 2.


---

## Analysis

This challenge requires converting from base 10 (decimal) to base 2 (binary). This can be done in many ways. Taking a look at the place values, we can notice that any decimal value is a combination of ones and zeros depending on their place in binary.

In binary, the places will be one, two, four, eight, sixteen and so on. So the trick is to:
1. Take the decimal value and find the highest power of 2 that is less than or equal to the decimal number. e.g for 42, the highest power of 2 is 32 or $2^5$ 
2. Next find the combination that adds up to make the decimal value. For this challenge, it will be $32+8+2 = 42$
3. Place a `1` for each power of 2 that was used in step 2 and a 0 for every other power of 2.
---

## Solution

| 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- |
| 1   | 0   | 1   | 0   | 1   | 0   |
### Python (if applicable)

```python
# Base 10 to base 2 converter
to_convert = 42
print(bin(to_convert)[2:])
```

### Other Tools

- CyberChef
- [Base Converter](https://www.rapidtables.com/convert/number/base-converter.html)
---

## Flag

```
picoCTF{101010}
```

---

## Key Takeaways

- Binary (base 2) uses only the digits `0` and `1`.
- Each position in a binary number represents a power of 2, starting from \(2^0\) on the right.
- A decimal number can be converted to binary by identifying which powers of 2 sum to the original value.
- Python's built-in `bin()` function converts an integer to its binary representation, prefixing the result with `0b`.
- Binary is the fundamental number system used by computers, making base conversions an essential skill in programming and cybersecurity.
---

## References

- picoCTF - 2Warm Challenge
- https://en.wikipedia.org/wiki/Binary_number
- https://en.wikipedia.org/wiki/Binary_numeral_system
- https://docs.python.org/3/library/functions.html#bin
- https://gchq.github.io/CyberChef/

## Related Concepts

- Number Systems
- Binary
- Decimal
- Base Conversion
- Powers of Two
- [[2-Warmed Up]]