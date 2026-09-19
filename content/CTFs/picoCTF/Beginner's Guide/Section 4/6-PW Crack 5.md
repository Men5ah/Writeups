---
publish: true
---

# PW Crack 5

Category: #General_Skills 
Level: #Medium 
Author: #Syreal 
Tags: #password_cracking #hashing

---

## Challenge

> Can you crack the password to get the flag?
>
> Download the password checker [here](https://artifacts.picoctf.net/c/31/level5.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/31/level5.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/31/level5.hash.bin) in the same directory too. Here's a [dictionary](https://artifacts.picoctf.net/c/31/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.

## Files

- In the project description.

## Hints

1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`
3. The `str_xor` function does not need to be reverse engineered for this challenge.

---

## Initial Observations

There is a dictionary with all the passwords this time, a text file. Knowing how to open a file in python will be useful.

---

## Analysis

This challenge builds on the previous PW Crack challenges. Instead of storing all possible passwords inside the Python script, the password candidates have been moved into an external dictionary file.

The hint suggests that file handling is important, so I need to open `dictionary.txt` and process its contents line by line. Since text files usually contain newline characters at the end of each line, I need to remove this whitespace before hashing the password. The `strip()` function can be used for this.

```python
with open('dictionary.txt', 'r') as d:
    for line in d:
        password = line.strip()
```

After obtaining each cleaned password, the existing hash comparison logic from the previous challenges can be reused. This turns the attack into a dictionary attack, where a predefined list of possible passwords is tested until one produces the same hash as the stored password hash.

Because the dictionary contains many possible passwords, automation is necessary instead of manually testing each candidate.

From there the program itself can start comparing and finding the correct password. Since there are so many lines in the dictionary file, I am also removing the portion where the program prints that the password is incorrect to save time.


---

## Solution

### Python (if applicable)

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
#     user_pw = input("Please enter correct password for flag: ")
#     user_pw_hash = hash_pw(user_pw)

    with open('dictionary.txt','r') as d:
        for line in d:
            pos_pw = d.strip()
            if( hash_pw(pos_pw) == correct_pw_hash ):
                print(pos_pw + " is the correct password")
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), pos_pw)
                print(decryption)
                return
            
level_5_pw_check()

```

### Other Tools

- Python `hashlib` module for generating MD5 hashes
- Python file handling (`open()` and `with` statements)
- Thonny (or another Python IDE) for modifying and testing the script

---

## Flag

```
picoCTF{h45h_sl1ng1ng_36e992a6}
```

---

## Key Takeaways

- Password cracking often relies on testing many possible candidates rather than reversing a hash.
- Dictionary attacks use a predefined list of possible passwords and compare their hashes against a known hash.
- External files can be processed efficiently in Python using file objects and loops.
- The `strip()` function is useful when processing text files because it removes unwanted whitespace characters such as newline characters.
- The `with` statement automatically manages file resources by closing files after they are used.
- Small implementation details matter when processing files; mixing file iteration with `readline()` can accidentally skip data.

---

## References

- picoCTF - PW Crack 5 Challenge
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://docs.python.org/3/library/stdtypes.html#str.strip
- https://docs.python.org/3/library/hashlib.html
- https://en.wikipedia.org/wiki/Dictionary_attack

## Related Concepts

- Password Cracking
- Dictionary Attacks
- Brute Force Attacks
- Hashing
- MD5
- File Processing
- Python Iterators
- Static Analysis
- Authentication Systems
- [[5-PW Crack 4]]