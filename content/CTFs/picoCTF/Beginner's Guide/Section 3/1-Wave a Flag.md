---
publish: true
---

# Wave a Flag

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags: None

---

## Challenge

> Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## Files

- [warm](https://challenge-files.picoctf.net/c_wily_courier/5a478d0b24d6a4f4185e3adb7a78c41cdad626fb02fe80e083dc33bf8b197d3d/warm)

## Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget <URL here>`, where the url can be found in the details section.
3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.
---

## Initial Observations

File provided is a binary file. Hints suggest to run it in terminal.

---

## Analysis

So following the hints, I used `wget` to download the file and ran `chmod +x warm` to make it an executable. According to Geeks for Geeks, `chmod` (change mode) is used to modify file and directory permissions. It controls who can read, write, or execute a file by setting access rights for the owner, group, or others.

```bash
chmod [options] [mode] [file_name]
```
where you can add optional flags that modify the behavior of the `chmod` command. Mode (in symbolic form) can either be; u, g, o, a, which specify user category; +, -, =, indicate add, remove, or set specific permissions; and 'r', 'w', 'x', stand for read, write, and execute permissions, respectively.

I can also use `ls -l warm` to show detailed information about the file. Running that gives me:

"-rw-rw-r-- 1 \[userName\]-academy \[userName\]-academy 19312 Dec 12  2025 warm"

and after running the command given, this is what it looks like

"-rwxrwxr-x 1 \[userName\]-academy \[userName\]-academy 19312 Dec 12  2025 warm"

This means that the command given in the hint is changing the mode to allow execute permissions. The x bits in the first part of the file information denote that the file is now available for execution.

So now that the file is executable, using `./warm` returns the following:

"Hello user! Pass me a -h to learn what I can do!"

Using --help returns:
"I don't know what '--help' means! I do know what -h means though!"

Which is in line with the last hint.

With what I've gotten so far, I can move on to the solution


---

## Solution

### Commands

```bash
./warm -h
```
Which will produce the following text:

"Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}"
### Python (if applicable)

```python
pass
```

### Other Tools

- chmod

---

## Flag

```
picoCTF{b1scu1ts_4nd_gr4vy_ac5832c}
```

---

## Key Takeaways

- Linux files must have execute permissions before they can be run as programs. The `chmod +x` command grants execute permission.
- The `./` prefix tells the shell to execute a program from the current directory rather than searching for it in the system's `PATH`.
- Many command-line programs implement help flags such as `-h` or `--help`, making them a good first step when exploring an unfamiliar executable.
- Challenge hints often point toward standard command-line conventions. In this case, trying the `-h` flag revealed the flag directly.
- Reading a program's help output is a common reconnaissance technique when solving CTF challenges or learning new command-line tools.

---

## References

- picoCTF - Wave a Flag Challenge
- https://man7.org/linux/man-pages/man1/chmod.1.html
- https://man7.org/linux/man-pages/man1/wget.1.html
- https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html
- https://ryanstutorials.net/linuxtutorial/commandline.php

## Related Concepts

- Linux File Permissions
- `chmod`
- Executable Files
- Command-Line Arguments
- Help Flags (`-h`, `--help`)
- Linux Shell
- Reconnaissance