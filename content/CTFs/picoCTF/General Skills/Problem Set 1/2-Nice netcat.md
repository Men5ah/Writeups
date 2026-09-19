# 2-Nice netcat

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> There is a nice program that you can talk to by using this command in a shell: 
> $ nc wily-courier.picoctf.net 58238, but it doesn't speak English...

## Files

- None

## Hints

1. You can practice using netcat with this picoGym problem: [[3-What's a net cat]]
2. You can practice reading and writing ASCII with this picoGym problem: [[1-Let's Warm Up]]

---

## Initial Observations

Using `netcat` is familiar, but the program doesn't speak English so I'm sure there is some kind of encryption or encoding involved.

---

## Analysis



Connecting to the program with netcat:

```bash
nc wily-courier.picoctf.net 58238
```

returns a long list of numbers, the first 5 are shown below.

```
112 
105 
99 
111 
67 

```

Looking at Hint #2 suggests that these numbers may be ASCII codes that has to be transformed into plaintext to continue with the challenge.

Using CyberChef, I use the `From Decimal` ingredient in a recipe and pasted the numbers from the program. This returned the flag.

---

## Solution

1. Use netcat to connect to the program.
2. Use an ASCII converter to convert the decimal numbers into text
3. Retrieve the flag.
### Other Tools

- CyberChef ("From Decimal" recipe)
- Netcat (`nc`)
---

## Flag

```
picoCTF{g00d_k1tty!_n1c3_k1tty!_e9c85}
```

---

## Key Takeaways

- Netcat (`nc`) is a simple, general-purpose tool for connecting to and communicating with services over TCP/UDP — a foundational skill for interacting with remote CTF challenge instances.
- When a program's output "doesn't make sense" as plain text, check whether it's numeric — a stream of numbers in the 0–127 range is a strong signal of ASCII decimal encoding.
- CyberChef's "From Decimal" recipe (as opposed to "From Hex" used in the earlier Warm Up challenge) is the correct tool when values are given as base-10 numbers rather than hexadecimal.
- Building on previous, simpler challenges (like single-character hex-to-ASCII conversion) makes it easier to recognize similar encoding patterns at scale in later challenges.

---

## References

- https://gchq.github.io/CyberChef/
- https://man7.org/linux/man-pages/man1/nc.1.html
- https://www.ascii-code.com/

## Related Concepts

- Netcat / TCP Communication
- ASCII Decimal Encoding
- CyberChef Recipes
- Remote Service Interaction