---
publish: true
---

# PW Crack 3

Category: #General_Skills 
Level: #Medium 
Author: #Syreal 
Tags: #password_cracking #hashing

---

## Challenge

> Can you crack the password to get the flag?
> 
> Download the password checker [here](https://artifacts.picoctf.net/c/17/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/17/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/17/level3.hash.bin) in the same directory too.
> 
> There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

## Files

-  In the challenge description

## Hints

1. To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`

2. To exit `bvi` type `:q` and press enter.

3. The `str_xor` function does not need to be reverse engineered for this challenge.

---

## Initial Observations

A new file has been added, a binary file and a hint to use `bvi`, a visual editor for binary files.

---

## Analysis

Similar to the previous PW Crack challenges, the goal is to recover the correct password. However, instead of being directly visible or encoded in the source, the password must be identified by comparing hashes. The challenge compares the MD5 hash of the user's input with the stored hash of the correct password contained in `level3.hash.bin`.

This challenge introduces hasing via `hash_pw(pw)`. The way this works is the function takes an input of some kind and uses a hashing algorithm such as MD5 or SHA-256 to create a fixed-length hash. This is useful because hashing algorithms are deterministic, the same input produces the same output. The program isn't storing the actual password, it stores a fingerprint of the password and checks whether the fingerprints match.

Following the hint and using `bvi`, I was able to open the binary file but I did not really know what to do from there.

Since there are 7 possible passwords, there are 2 approaches to take. The first one is running the program 7 times and using each possible password as input until you get the correct one, which is fine because there are only 7 possible passwords. The second approach, and the better one, is to modify the program to use a loop.

In the `level_3_pw_check` function, I commented out the user input and placed the `if` statement into a for loop that loops through the possible password list `pos_pw_list`. For each one, if the password is wrong, it will output that the password is wrong. For the correct password, it goes straight to decrypting the file and printing the flag. I can probably modify the program further to print out the correct password.

---

## Solution

### Python

```python
import hashlib

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

flag_enc = open('level3.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

def level_3_pw_check():
#     user_pw = input("Please enter correct password for flag: ")
#     user_pw_hash = hash_pw(user_pw)
    
    for pw in pos_pw_list:
        if( hash_pw(pw) == correct_pw_hash ):
            print("Correct password: " + pw)
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), pw)
            print(decryption)
            return
        print(pw + " is incorrect")



level_3_pw_check()
```

### Other Tools

- bvi (Binary Visual Editor) for inspecting binary files
- Python `hashlib` module for generating MD5 hashes
- Thonny (or another Python IDE) for modifying and testing the script

---

## Flag

```
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

---

## Key Takeaways

- Hashing converts data into a fixed-length representation that can be used for verification without storing the original value.
- Password checks often work by comparing the hash of user input against a stored hash rather than comparing plaintext passwords.
- MD5 is a hashing algorithm, but it is considered insecure for protecting real passwords because it is fast and vulnerable to brute-force attacks.
- When a program provides a small list of possible values, automation with a script is usually faster and less error-prone than manually testing each option.
- Binary files can contain useful information, but they often need specialized tools such as `bvi`, `xxd`, or `hexdump` to inspect.

---

## References

- picoCTF - PW Crack 3 Challenge
- https://docs.python.org/3/library/hashlib.html
- https://www.kali.org/tools/bvi/
- https://en.wikipedia.org/wiki/MD5

## Related Concepts

- Password Cracking
- Hashing
- MD5
- Brute Force Attacks
- Dictionary Attacks
- Static Analysis
- Binary File Inspection
- Python Automation
- [[3-PW Crack 2]]