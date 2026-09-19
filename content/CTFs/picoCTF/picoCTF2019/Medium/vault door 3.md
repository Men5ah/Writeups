# vault door 3

Category: #Reverse_Engineering 
Level: #Medium 
Author: #Mark_E_Haase 
Tags:

---

## Challenge

> This vault uses for-loops and byte arrays.
> The source code for this vault is here

## Files

-  [VaultDoor3.java](https://challenge-files.picoctf.net/c_fickle_tempest/d2e2ce5be3c6983378013b304e34bbcfe51617a2f3ec987437028efbdbd93c83/VaultDoor3.java)

## Hints

1. Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

---

## Initial Observations

Where is vault door 2?

---

## Analysis

The challenge is a step up from [[vault door 1]]. This time, the password isn't as easy to guess because of this method:

```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm13gf49_u_4_m9r540");
    }
```

The new `checkPassword` function first checks if the password length is 32 characters long. It then declares a length 32 character/byte array and a counter `i`. It then uses 4 for-loops to place characters into the array. 

The first for loop starts at `index 0` and goes to `index 7` and increments by 1 and assigns the character at `index i` to the same index in the buffer.

The second for loop starts at `index 8` and ends at `index 15` and also increments by 1 and assigns the character at `index 23-i` to the buffer at `index i`.

The third loop starts at index 16 and ends at 31 but increments by 2 and, like the second loop, assigns a character at `index 46-i` to the buffer at `index i`.

The last loop starts at `index 31` and ends when i is greater than or equal to 17 but decrements by 2 and, like the first loop, assigns the character at `index i` to the same index in the buffer.

The method then creates a string using the buffer and checks if it's equal to `"jU5t_a_sna_3lpm13gf49_u_4_m9r540"` and returns True or False.

It looks like the program is doing some kind of substitution. The string being compared against is the expected final contents of `buffer`. Therefore, I can work backwards through each loop to determine which character from the input password must be placed at each position. By tracing the index mappings, I can reconstruct the original password that produces the expected buffer.

By tracing the code, I can find the unscrambled version.

|Index|Password|Buffer|
|---|---|---|
|0|j|j|
|1|U|U|
|2|5|5|
|3|t|t|
|4|_|_|
|5|a|a|
|6|_|_|
|7|s|s|
|8|1|n|
|9|m|a|
|10|p|_|
|11|l|3|
|12|3|l|
|13|_|p|
|14|a|m|
|15|n|1|
|16|4|3|
|17|g|g|
|18|r|f|
|19|4|4|
|20|m|9|
|21|_|_|
|22|4|u|
|23|_|_|
|24|u|4|
|25|_|_|
|26|9|m|
|27|9|9|
|28|f|r|
|29|5|5|
|30|3|4|
|31|0|0|
Alternatively, I can use the scrambled version as the password and print the unscrambled version and use that as the flag.

---

## Solution

### Java

```java
    public boolean checkPassword(String password) {

        if (password.length() != 32) {

            return false;

        }

        char[] buffer = new char[32];

        int i;

        for (i=0; i<8; i++) {

            buffer[i] = password.charAt(i);

        }

        for (; i<16; i++) {

            buffer[i] = password.charAt(23-i);

        }

        for (; i<32; i+=2) {

            buffer[i] = password.charAt(46-i);

        }

        for (i=31; i>=17; i-=2) {

            buffer[i] = password.charAt(i);

        }

        String s = new String(buffer);

        System.out.println("picoCTF{" + s + "}");

        return s.equals("jU5t_a_sna_3lpm13gf49_u_4_m9r540");

    }
```

### Other Tools

- VSCode

---

## Flag

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_99f530}
```

---

## Key Takeaways

- `for` loops can be used to **reorder data** by writing elements from one position to another.
- When reverse engineering code, tracing the **value of loop variables and array indices** can reveal how data is transformed.
- A character array can be used as an intermediate buffer to rearrange a string without changing the original string.
- When a program compares a transformed value against a known string, the transformation can often be **reversed** to recover the original input.
- Creating an index table is a useful technique for understanding complicated loops and array manipulations.

---

## References

- [Java `for` Statement Documentation](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html)
- [Java Arrays Documentation](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)
- Java `String.charAt()` Documentation

## Related Concepts

- Reverse engineering
- Static analysis
- Array indexing
- Zero-based indexing
- `for` loops
- Character arrays
- String manipulation
- Index mapping
- Data transformation
- Reversing algorithms