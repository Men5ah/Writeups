---
publish: true
---

# plumbing

Category: #General_Skills 
Level: #Medium 
Author: #Alex_Fulton #Danny_Tunitis 
Tags:

---

## Challenge

> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?
> Connect to fickle-tempest.picoctf.net `<PORT>`

## Files

- 

## Hints

1. Remember the flag format is picoCTF{XXXX}

2. What's a pipe? No not that kind of pipe... This kind

---

## Initial Observations

This is another netcat challenge. What is a pipe?

---

## Analysis

The challenge asks to keep the output from a program AND search for a flag. This is implying that the solution to this challenge should be done in one command. Using netcat, I connected to the program which seems to print thousands of lines and the terminal eventually stops printing. The lines can be any one of these four:

```
Not a flag either
I don't think this is a flag either
This is definitely not a flag
Again, I really don't think this is a flag.
```

It is possible that the flag is in here somewhere but it stops printing before the flag is printed.

Using the second hint, I read a little about the pipe `|` which essentially uses the output from one command as input for the next one, allowing commands to be chained together instead of running them one at a time.

Since I am looking for a specific pattern, I can reuse what I learned from [[5-First Grep]]. Instead of saving the output from `nc` to a file first, I can use a pipe to send its output directly to `grep`.

The resulting pipeline is:

nc → grep

`nc` produces the output, and the pipe (`|`) sends that output to `grep`, which searches for the `picoCTF{...}` pattern. This allows me to search the program's output as it is being produced rather than manually looking through thousands of lines.

---

## Solution

### Commands

```bash
nc fickle-tempest.picoctf.net <port> | grep -oE "picoCTF\{.*\}"
```

### Other Tools

- `nc` / `netcat` — used to establish a connection to the remote challenge program
- `grep` — used to search the program's output for the flag pattern

---

## Flag

```
picoCTF{digital_plumb3r_1eBfC512}
```

---

## Key Takeaways

- A pipe (`|`) connects the standard output of one command to the standard input of another command.
- Pipes allow commands to be chained together so that the output of one program can be processed immediately by another program without first saving it to a file.
- `grep` can be used to filter a continuous stream of data and return only lines that match a specified pattern.
- The `-o` option makes `grep` print only the portion of the line that matches the pattern.
- The `-E` option enables Extended Regular Expressions, allowing patterns such as `picoCTF\{.*\}` to be used.
- Network tools such as `nc` can produce data that can be processed directly by other command-line tools.

---

## References

- https://man7.org/linux/man-pages/man1/nc.1.html
- https://man7.org/linux/man-pages/man1/grep.1.html
- https://www.gnu.org/software/bash/manual/html_node/Pipelines.html

## Related Concepts

- Unix Pipes
- Standard Input (stdin)
- Standard Output (stdout)
- Command Chaining
- `grep`
- Regular Expressions
- Netcat (`nc`)
- Data Streams
- Linux Command Line






