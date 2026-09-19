# PW Crack 1

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags: #password_cracking

---

## Challenge

> Can you crack the password to get the flag?
> Download the password checker [here](https://artifacts.picoctf.net/c/11/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc) in the same directory too.

## Files

- [here](https://artifacts.picoctf.net/c/11/level1.py)
- [flag](https://artifacts.picoctf.net/c/11/level1.flag.txt.enc)

## Hints

1. To view the file in the webshell, do: `$ nano level1.py`

2. To exit `nano`, press Ctrl and x and follow the on-screen prompts.

3. The `str_xor` function does not need to be reverse engineered for this challenge.


---

## Initial Observations

This challenge will involve some kind of code manipulation and file I/O like the previous one.

---

## Analysis

Ideally, the challenge would require me opening the file using the `nano` command, which is a modeless command-line text editor and is simpler to use as compared to vim. If I were to use the webshell for this challenge I would use `nano level1.py` to open it up so I can inspect it. I prefer an IDE such as Thonny since it's lightweight and comes with its own Python installation.

After inspecting the code, I can tell that its a fairly easy challenge. There is a variable called `flag_enc` which stores the contents of the encrypted flag file after it is read from disk. The challenge notes that the encrypted flag file must be in the same directory because the script expects to open it by filename.This is most likely why it was mentioned in the challenge description that it should be in the same directory.

Next is a function called `level_1_pw_check` which asks the user for a password. The next part is an `if` block that checks if the user's input is equal to '1e1a' using the `==` operator for the comparison. If there is a match, the file is decrypted and printed. If the password is wrong, the program says that the password is wrong and ends.

Rather than attempting to guess the password, the first step is to inspect the source code. If the password verification is implemented directly in the script, there is a chance that the expected password has been hard-coded. This turns out to be the case, as the comparison `user_pw == '1e1a'` reveals the correct password immediately.

---

## Solution

### Commands

```bash
python level1.py
```

1. When prompted, enter '1e1a' as the password.
2. The program will decrypt the binary file and return the key.
### Python (if applicable)

```python
pass
```

### Other Tools

- nano

---

## Flag

```
picoCTF{545h_r1ng1ng_fa343060}
```

---

## Key Takeaways

- Reading the source code of a program can reveal hard-coded values such as passwords, API keys, or other secrets without needing to reverse engineer the executable.
- Python's `open()` and `read()` functions are commonly used to load data from files, making file I/O an important concept to understand when analyzing scripts.
- Conditional statements (`if`) often determine whether privileged functionality, such as decrypting a file, is executed.
- Before attempting more complex techniques, inspect the source code for hard-coded credentials or obvious logic flaws.
- Using a code editor or IDE with syntax highlighting can make it easier to understand unfamiliar code.
- 
- 

---

## References

- picoCTF - PW Crack 1 Challenge
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://docs.python.org/3/library/functions.html#open
- https://docs.python.org/3/reference/compound_stmts.html#if

## Related Concepts

- Source Code Review
- Static Analysis
- Python File I/O
- Conditional Statements
- Password Authentication
- XOR Encryption