---
publish: true
---

# PW Crack 2

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags: #password_cracking 

---

## Challenge

> Can you crack the password to get the flag?
> Download the password checker [here](https://artifacts.picoctf.net/c/14/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc) in the same directory too.

## Files

- [here](https://artifacts.picoctf.net/c/14/level2.py) 
- [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc) 

## Hints

1. Does that encoding look familiar?

2. The `str_xor` function does not need to be reverse engineered for this challenge.

---

## Initial Observations

This is a step up from the challenge before this one. It may be more difficult.

---

## Analysis

This code is much similar to the one from [[2-PW Crack 1]]. The only difference here is that instead of the password being in plaintext in the `if` statement, it has been changed to a string of encoded characters. The password is represented using **hexadecimal integer literals**. Each value such as `0x34` is a hexadecimal number that is converted to its corresponding ASCII character using Python's `chr()` function.

There are 3 ways I can approach this. I can either use CyberChef to decode each character and I can use that as input, I can write a script to do the same thing, or I can modify the existing code instead of creating a whole new script. 

So by adding the following lines of code to the file:
```python
password = chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
print(password)
```

I can print the password to the terminal to see what it is and then use that as the input.

Alternatively, I can remove the need to enter a password in the first place. I can comment out the line that asks for input and replace the left side of the comparison with the encoded password so just running the program returns the key immediately. Note that I'll also have to replace the `user_pw` variable inside the `if` statement with the encoded password as well.

I'll have both versions in the Solution

---

## Solution

### Python (if applicable)

```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()

password = chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)
print("Password is: " + password)

def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()
```

```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level2.flag.txt.enc', 'rb').read()


def level_2_pw_check():
    if( chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39))
        print(decryption)
        return
    print("That password is incorrect")



level_2_pw_check()


```

### Other Tools

- CyberChef (optional, for decoding hexadecimal values)
- Thonny (or another Python IDE) for inspecting and modifying the script

---

## Flag

```
picoCTF{tr45h_51ng1ng_9701e681}
```

---

## Key Takeaways

- Source code can represent strings in many forms, including hexadecimal integer literals converted with `chr()`.
- The `chr()` function converts an integer Unicode code point into its corresponding character, while `ord()` performs the reverse conversion.
- Understanding how data is represented in source code is often enough to recover hidden values without complex reverse engineering.
- Before modifying a program, inspect the code to understand how it constructs or validates sensitive values such as passwords.
- CyberChef and simple Python scripts are both useful tools for decoding or reconstructing encoded data.

---

## References

- picoCTF - PW Crack 2 Challenge
- https://docs.python.org/3/library/functions.html#chr
- https://docs.python.org/3/library/functions.html#ord
- https://docs.python.org/3/library/functions.html#hex
- https://gchq.github.io/CyberChef/

## Related Concepts

- Source Code Review
- Static Analysis
- Hexadecimal
- ASCII
- Character Encoding
- Python `chr()` and `ord()`
- Password Authentication
- [[2-PW Crack 1]]