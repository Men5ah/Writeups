# vault door 1

Category: #Reverse_Engineering 
Level: #Medium 
Author: #Mark_E_Haase
Tags:

---

## Challenge

> This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here:

## Files

- [VaultDoor1.java](https://challenge-files.picoctf.net/c_fickle_tempest/df83732fa379fb7cf3373e872748a40ec53c5baa532f3274e1ab499cd3d3b197/VaultDoor1.java)

## Hints

1. Look up the charAt() method online
---

## Initial Observations

Java source code.

---

## Analysis

The challenge is asking to make sense of a complicated Array in some Java source code. This challenge is the first in a series of unlocking vault doors.

Upon inspection, the code seems to be a password checker. The program creates a new Vault Door and a scanner to collect input for the vault password. The program first uses `substring()` to check that the input begins with the expected flag prefix, `picoCTF{`, before using `charAt()` to check individual characters."

In the `checkPassword` boolean method, it is checking if the string is 32 characters long and then check for each index, in a random order, if the character at that index matches the hardcoded character in the comparison. If they all match, the program prints "Access granted."

Within the code there is a comment:

```Java
    // I came up with a more secure way to check the password without putting

    // the password itself in the source code. I think this is going to be

    // UNHACKABLE!! I hope Dr. Evil agrees...
```

And although the password itself isn't in the source code, the `checkPassword` function is still using plaintext characters for comparison like below:

```Java
password.charAt(0)  == 'd' &&

password.charAt(29) == '2' &&

password.charAt(4)  == 'r' &&

password.charAt(2)  == '5' &&

password.charAt(23) == 'r' &&
```

So, via static analysis, the flag can be rearranged if written in order based on the `charAt` index.

---

## Solution

- Use static analysis to rearrange the flag

### Other Tools

- VSCode

---

## Flag

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_1ef266}
```

---

## Key Takeaways

- **Static analysis** can reveal sensitive information by examining source code without executing the program.
- `charAt(index)` in Java returns the character at the specified **zero-based index** of a string.
- When a password is checked character-by-character in a scrambled order, the `charAt()` indices can be used to reconstruct the password in its correct order.
- Obfuscating the order of password checks does **not** make a password secure if the expected characters are still present directly in the source code.

---

## References

- Java `String.charAt()`
- [Java String Documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)

## Related Concepts

- Reverse engineering
- Static analysis
- Source code analysis
- Java `String`
- `charAt()`
- Zero-based indexing
- Password validation
- Code obfuscation
- Hardcoded credentials
- [[vault door 3]]