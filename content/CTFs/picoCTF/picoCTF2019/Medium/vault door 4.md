---
publish: true
---

# vault door 4

Category: #Reverse_Engineering 
Level: #Medium 
Author: #Mark_E_Haase 
Tags:

---

## Challenge

> This vault uses ASCII encoding for the password.
> The source code for this vault is here:

## Files

-  [VaultDoor4.java](https://challenge-files.picoctf.net/c_fickle_tempest/5a242afc9022df976b1c18fe9364788579431217536fca41006714b29d8931e1/VaultDoor4.java)

## Hints

1. Use a search engine to find an "ASCII table"
2. You will also need to know the difference between octal, decimal, and hexadecimal numbers.

---

## Initial Observations

This challenge builds on the previous Vault Door challenges, but instead of rearranging characters or using loops to obscure the password, it uses different numerical representations of ASCII characters.

---

## Analysis

The vault door is protected using different representations of **ASCII character codes**. The goal is therefore to convert each numeric representation back into its corresponding character.

The `checkPassword` method first converts the user's input into a byte array using `getBytes()`. It then creates another byte array called `myBytes` containing the expected password. A `for` loop compares the two arrays one byte at a time. If every byte matches, the password is accepted.

The values in `myBytes` are written using several different number bases:

- The first section contains **decimal** values.
- The second section contains **hexadecimal** values, indicated by the `0x` prefix.
- The third section contains **octal** values, indicated by the leading `0`.
- The final section already contains characters represented directly as character literals.

For example:

```
0x6a
```

is hexadecimal. Converting it to decimal gives `106`, which corresponds to the character `j` in ASCII.

Similarly, an octal value such as:

```
0137
```

represents decimal `95`, which corresponds to `_` in ASCII.

Therefore, rather than treating the values as ordinary decimal numbers, I need to identify the **base of each value first**, convert it to its ASCII character, and then combine the resulting characters in their original order.

Using CyberChef to decode each section gives the complete password/flag.

---

## Solution

- Open CyberChef
- Use the From Decimal, From Hexadecimal, and From Octal recipes to get each part of the flag.
- Add the plaintext at the end and that's your flag.
### Other Tools

- CyberChef

---

## Flag

```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_ 30dc85bed}
```

---

## Key Takeaways

- ASCII assigns numerical values to characters, allowing text to be represented using numbers.
- The same ASCII character can be represented using different number bases, such as **decimal, hexadecimal, and octal**.
- The prefix `0x` indicates a hexadecimal value, while a leading `0` in Java integer literals can indicate an octal value.
- When analyzing source code, it is important to identify the **number base** being used before interpreting a numerical value.
- CyberChef can quickly convert numerical representations into ASCII text, but understanding the underlying conversion makes it possible to solve the challenge manually.

---

## References

- [ASCII Table — ASCII Code](https://www.ascii-code.com/)
- Java Integer Literals — Oracle
- [CyberChef](https://gchq.github.io/CyberChef/)

## Related Concepts

- ASCII
- Character encoding
- Decimal
- Hexadecimal
- Octal
- Number base conversion
- Byte arrays
- Java `getBytes()`
- Static analysis
- Reverse engineering
- CyberChef
