# Static ain't always noise

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> Can you look at the data in this binary? The bash script might help!
## Files

- [static](https://challenge-files.picoctf.net/c_wily_courier/34dfb62cf2c94a618c7cdc292ff1c4062b104773695071e9a16ab25ad8cc935c/static)
- [ltdis.sh](https://challenge-files.picoctf.net/c_wily_courier/34dfb62cf2c94a618c7cdc292ff1c4062b104773695071e9a16ab25ad8cc935c/ltdis.sh)

## Hints

None

---

## Initial Observations

 I need to figure out how to run bash scripts.

---

## Analysis

The challenge provides 2 files, a binary file and a bash script. Starting with investigating the files, the binary file displays non-readable text. The Bash script is a wrapper that uses disassembly and string-extraction tools to analyze the binary and displays some code and comments which show how to use the script. An important thing to note is:

```bash
echo "Usage: ltdis.sh <program-file>"
```
This is the output when the script isn't run properly. The output is saying that a file is required, possibly the binary file provided.

The name of the challenge is also a clue. "Static" refers to analyzing a program without executing it, while the "noise" refers to the large amount of machine code and binary data that is difficult to read directly. The provided script helps separate useful information from this noise by disassembling the binary and extracting readable strings.

To run the script, I have read that you have to use the `bash` command.:
```bash
bash ltdis.sh static
```

The result is as follows
```
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

So now I have to check inside `static.ltdis.strings.txt` which most likely has the flag. Since the length of the text file is unknown, using grep would be faster.

```bash
grep -oE "picoCTF\{.*\}" static.ltdis.strings.txt
```

which returns the flag.

---

## Solution

### Commands

```bash
bash ltdis.sh static
grep -oE "picoCTF\{.*\}" static.ltdis.strings.txt
```

### Other Tools

- `bash` — used to execute the provided Bash script
- `grep` — used to search the extracted strings for the flag pattern
- `strings` — used by the provided script to extract printable strings from the binary
- `objdump` — used by the provided script to disassemble the binary

---

## Flag

```
picoCTF{d15a5m_t34s3r_20335e41}
```

---

## References

- https://man7.org/linux/man-pages/man1/bash.1.html
- https://man7.org/linux/man-pages/man1/strings.1.html
- https://man7.org/linux/man-pages/man1/grep.1.html
- https://man7.org/linux/man-pages/man1/objdump.1.html

---

## Related Concepts

- Binary Analysis
- Static Analysis
- Disassembly
- Bash Scripting
- `strings`
- `grep`
- Regular Expressions
- Reverse Engineering
- Executable Files