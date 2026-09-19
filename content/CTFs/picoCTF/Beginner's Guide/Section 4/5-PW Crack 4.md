# PW Crack 4

Category: #General_Skills 
Level: #Medium 
Author: #Syreal 
Tags: #password_cracking #hashing 

---

## Challenge

> Can you crack the password to get the flag?
>
> Download the password checker [here](https://artifacts.picoctf.net/c/19/level4.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/19/level4.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/19/level4.hash.bin) in the same directory too.
>
> There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.

## Files

- In challenge description

## Hints

1. A for loop can help you do many things very quickly.
2. The `str_xor` function does not need to be reverse engineered for this challenge.

---

## Initial Observations

Similar observation to [[4-PW Crack 3]]

---

## Analysis

This challenge uses the same hashing mechanism as PW Crack 3, but increases the number of possible passwords from 7 to 100. Since the password candidates are already provided in `pos_pw_list`, there is no need to crack the MD5 hash directly. Instead, I can automate the process by hashing each candidate password and comparing the result with the stored hash.

The solution from PW Crack 3 can be reused with only minor changes. Instead of manually providing a password as input, the program will iterate through all values in `pos_pw_list` and identify the one whose hash matches the stored hash.

This is essentially a small-scale dictionary attack, where the attacker tests a known collection of possible passwords rather than randomly generating guesses.

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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_4_pw_check():
#     user_pw = input("Please enter correct password for flag: ")
#     user_pw_hash = hash_pw(user_pw)

    for pw in pos_pw_list:
        if( hash_pw(pw) == correct_pw_hash ):
            print(pw + " is the correct password")
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), pw)
            print(decryption)
            return
        print(pw+" is incorrect")


# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6288", "6152", "4c7a", "b722", "9a6e", "6717", "4389", "1a28", "37ac", "de4f", "eb28", "351b", "3d58", "948b", "231b", "973a", "a087", "384a", "6d3c", "9065", "725c", "fd60", "4d4f", "6a60", "7213", "93e6", "8c54", "537d", "a1da", "c718", "9de8", "ebe3", "f1c5", "a0bf", "ccab", "4938", "8f97", "3327", "8029", "41f2", "a04f", "c7f9", "b453", "90a5", "25dc", "26b0", "cb42", "de89", "2451", "1dd3", "7f2c", "8919", "f3a9", "b88f", "eaa8", "776a", "6236", "98f5", "492b", "507d", "18e8", "cfb5", "76fd", "6017", "30de", "bbae", "354e", "4013", "3153", "e9cc", "cba9", "25ea", "c06c", "a166", "faf1", "2264", "2179", "cf30", "4b47", "3446", "b213", "88a3", "6253", "db88", "c38c", "a48c", "3e4f", "7208", "9dcb", "fc77", "e2cf", "8552", "f6f8", "7079", "42ef", "391e", "8a6d", "2154", "d964", "49ec"]
level_4_pw_check()


```

### Other Tools

- Python `hashlib` module for generating MD5 hashes
- Thonny (or another Python IDE) for modifying and testing the script
---

## Flag

```
picoCTF{fl45h_5pr1ng1ng_ae0fb77c}
```

---

## Key Takeaways

- Increasing the number of possible passwords does not always require a more complex attack; automation can handle larger search spaces efficiently.
- A `for` loop can be used to test multiple candidate passwords quickly by repeating the same hashing and comparison process.
- When a password list is provided, the attack becomes a dictionary attack rather than randomly guessing possible passwords.
- Code reuse is an important skill in cybersecurity. The solution from a previous challenge can often be adapted for a more difficult version of the same problem.
- Hash functions allow programs to verify passwords without storing the plaintext password, but weak password choices can still be discovered by testing possible inputs.

---

## References

- picoCTF - PW Crack 4 Challenge
- https://docs.python.org/3/library/hashlib.html
- https://en.wikipedia.org/wiki/Dictionary_attack
- https://en.wikipedia.org/wiki/MD5

## Related Concepts

- Password Cracking
- Dictionary Attacks
- Brute Force Attacks
- Hashing
- MD5
- Python Automation
- Static Analysis
- Authentication Systems
- [[4-PW Crack 3]]