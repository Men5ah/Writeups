# Undo

Category: #General_Skills 
Level: #Easy 
Author: #Yahaya_Meddy
Tags:

---

## Challenge

> Can you reverse a series of Linux text transformations to recover the original flag?
> Start searching for the flag here `nc foggy-cliff.picoctf.net [PORT]`

## Files

- None

## Hints

1. For text translation and character replacement, see [`tr`command documentation](https://man7.org/linux/man-pages/man1/tr.1.html).

---

## Initial Observations

What immediately stands out?

---

## Analysis

The challenge is asking to reverse a series of Linux text transformations. Once connected with `nc`, the program displays the following:

```
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KXA2OTgxcHBxLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: 
```

The first step is to decode this Base64 encoded string. From the `man` [page](https://man7.org/linux/man-pages/man1/base64.1.html) for this command, the normal syntax is:

```bash
base64 [option]... [file]
```

Decoding with base64 is `base64 -d` or `base64 --decode` using the `-d` option. The next step then displays.

```
--- Step 2 ---
Current flag: )p6981ppq-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it: 
```

The flag is currently reversed, the command to reverse this is `rev`, which has the following syntax:

```bash
rev [option] [file...]
```

Once entered, step 3 is displayed.

```
--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-qpp1896p)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: 
```

To replace characters with different ones, I have to look to the hint provided which is the `tr`(translate) command which translates or deletes characters and uses the syntax:

```bash
tr [option]... String1 [String2]
```

So, to change the dashes to underscores, the command will be `tr '-' '_'`  which then displays step 4.

```
--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_qpp1896p)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: 
```

Now the parentheses need to be replaced with curly braces. The command for this is `tr '()' '{}'` which displays step 5.

```
--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_qpp1896p}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: 
```

The command for ROT13 is `tr A-Za-z N-ZA-Mn-za-m`. According to the `man` page, you can use a range of characters to replace `String1` and `String2`. So the range here is from uppercase A to lowercase z which will be replaced with characters from uppercase N to lowercase m. Entering this command gets the flag.

```
Congratulations! You've recovered the original flag:
>>> picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_dcc1896c}

```

---

## Solution

### Commands

```bash
base64 -d
rev
tr '-' '_'
tr '()' '{}'
tr A-Za-z N-ZA-Mn-za-m
```

### Other Tools

- base64
- rev
- tr

---

## Flag

```
picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_dcc1896c}
```

---

## Key Takeaways

- Linux text-processing commands can be used together to transform, decode, and manipulate text.
- When reversing transformations, the **order matters**. Each operation must be undone in the reverse order in which it was originally applied.
- The `tr` command can translate characters between two character sets, making it useful for substitutions such as replacing `-` with `_` or performing ROT13.
- Common Linux commands such as `base64 -d`, `rev`, and `tr` are useful tools for solving text-based CTF challenges.

---

## References

- [Linux `tr` command documentation](https://man7.org/linux/man-pages/man1/tr.1.html)
- [Linux `base64` command documentation](https://man7.org/linux/man-pages/man1/base64.1.html)
- [Linux `rev` command documentation](https://man7.org/linux/man-pages/man1/rev.1.html)

## Related Concepts

- Base64 encoding/decoding
- ROT13
- Character substitution
- Text transformations
- Linux pipes and text processing
- `tr` character sets and ranges
- Reversing transformations
- Command-line utilities