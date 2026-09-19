---
publish: true
---

# strings it

Category: #General_Skills 
Level: #Easy 
Author: #Sanjay_C/Danny_Tunitis 
Tags: None

---

## Challenge

> Can you find the flag in [file](https://challenge-files.picoctf.net/c_fickle_tempest/a35dc624cfda858ed12a4bce57f832dad3b433bad6cde2b98e25fae4bc8ff760/strings) without running it?

## Files

- [file](https://challenge-files.picoctf.net/c_fickle_tempest/a35dc624cfda858ed12a4bce57f832dad3b433bad6cde2b98e25fae4bc8ff760/strings)

## Hints

1. strings

---

## Initial Observations

This is a simple challenge that involves strings. Maybe it has something to do with concatenating them to make the flag.

---

## Analysis

The challenge has asked that the file not be run which probably means it is some kind of code file. Using `cat` or `nano` yield no readable results in the webshell.

There may be a clue inside the file, so using `chmod` I add execute permissions to it and run the file and it points me in the direction of the `strings` function, so I can use `man strings` to find out more.

### strings
For each _file_ given, GNU **strings** prints the printable character sequences that are at least 4 characters long (or the number given with the options below) and are followed by an unprintable character.

It uses the following syntax:
```bash
strings [options] filename

e.g strings -n 2 file.bin
```

The option to specify the minimum length of string to look for might be useful so I'm including it in the syntax for reference.

Using `strings strings` works and returns a long list of strings that are at least 4 characters long. Since the flag starts with `picoCTF` a 7 character string, i think that if I include a minimum length option in the command, it will reduce the amount of strings I have to look through to find the flag. That doesn't seem to work and using the `-h` flag only returns the same information in the `man` page.

After some reading online, it seems like I can use `grep` to search for specific strings similar to using `Ctrl+F` on a keyboard. So now the approach is to get the strings in the file and use `grep` to search for the flag. This works.


> [!NOTE] The Pipe `|`
> It **connects the output of one command directly to the input of another command**.

> ![NOTE] Other Useful Information
> You can use `&&` to run 2 commands provided the first one is a success.
> Use `;` to run 2 or more commands regardless of whether the first one succeeds or not.

---

## Solution

By first getting the strings in the file, you can pipe (`|`) the output to the `grep` command. This will return the flag.

### Commands

```bash
strings strings | grep 'picoCTF'
```
### Other Tools

- strings
- grep

---

## Flag

```
picoCTF{5tRIng5_1T_60eA8fdA}
```

---

## Key Takeaways

- The `strings` utility extracts printable character sequences from binary files, making it useful for inspecting executables without running them.
- Pipes (`|`) allow the output of one command to be used as the input to another, enabling powerful command-line workflows.
- `grep` can filter command output to quickly locate specific text, such as a picoCTF flag.
- Reading the manual page (`man strings`) is a useful way to learn the purpose and available options of unfamiliar Linux commands.
- Many CTF challenges can be solved through static analysis, avoiding the need to execute potentially unknown or unsafe binaries.

---

## References

- picoCTF - strings it Challenge
- https://man7.org/linux/man-pages/man1/strings.1.html
- https://man7.org/linux/man-pages/man1/grep.1.html
- https://www.gnu.org/software/binutils/docs/binutils/strings.html

## Related Concepts

- Static Analysis
- GNU `strings`
- `grep`
- Unix Pipes (`|`)
- Linux Command Line
- Binary Inspection