# Magikarp Ground Mission

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin.
>
> Login via `ssh` as `ctf-player` with the password, `8c606eb1` on the host `wily-courier.picoctf.net` and port `65434`.

## Files

- none

## Hints

1. Finding a cheatsheet for bash would be really helpful!

---

## Initial Observations

I have used ssh before so this challenge should be familiar. I also think that some knowledge of terminal commands is useful here.

---

## Analysis

The core of Linux involves the command line interface (CLI).The CLI can be used to access files on a machine so its useful to know a few key ones.

The first one I know of is `ls` which is used to list the contents of the current directory.
```bash
ls
```

The next one is `cd` which is used to change directories. This is followed by the name of a folder in the current directory.
```bash
cd <folder>
```
If you ever need to step out of a folder, you still use `cd`but followed by `../` which will take you up one level.

If you are lost and can't see your current directory, you can use `pwd` to print the working directory.

The last thing for this challenge will be to use `cat` you can use this to 'open' files i.e. printing their contents to the terminal.

Using `ls` shows 2 text files, `1of3.flag.txt` and `instructions-to-2-of-3.txt` which implies that the flag is separated into 3 parts within this challenge.

The image below shows the commands used to retrieve the 3 parts of the flag.

![[Pasted image 20260810103947.png]]

---

## Solution

### Commands

```bash
ssh ctf-player@wily-courier.picoctf.net -p [PORT]
ls
cat 1of3.flag.txt
cat instructions-to-2-of-3.txt
pwd
cd ../../../      # To go to the root
ls                # To print contents
cat 2of3.flag.txt
cat instructions-to-3-of-3.txt
cd home/ctf-player
ls
cat 3of3.flag.txt
```

### Other Tools

- ssh
- ls
- cd
- cat
- pwd

---

## Flag

```
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```

---

## Key Takeaways

- `ls`, `cd`, `pwd`, and `cat` are the essential building blocks for navigating and reading files in any Linux shell — foundational for nearly every future challenge involving a remote or local shell.
- Absolute paths (`cd /home/ctf-player`) can be faster and less error-prone than chaining several relative `cd ../` commands when the target location is known.
- Challenges can be structured as multi-step breadcrumb trails, where each file both rewards progress (a flag fragment) and directs the next action (instructions to the next location) — a pattern likely to reappear in other "explore the filesystem" challenges.
- `pwd` is a simple but valuable sanity check any time navigation across multiple directories risks losing track of the current location.

---

## References

- https://www.gnu.org/software/bash/manual/bash.html
- https://man7.org/linux/man-pages/man1/ssh.1.html

## Related Concepts

- Linux Filesystem Navigation
- SSH Remote Access
- Relative vs. Absolute Paths
- Command-Line File Reading