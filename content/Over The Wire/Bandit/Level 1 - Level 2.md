---
tags:
  - otw
  - bandit
level: "1"
publish: true
---
# Bandit Level 1 → 2

## 🔗 Connection Info

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in a file called **-** located in the home directory.

## Concepts / Commands Used

- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)
- [Google Search for “dashed filename”](https://www.google.com/search?q=dashed+filename)
- [Advanced Bash-scripting Guide - Chapter 3 - Special Characters](https://linux.die.net/abs-guide/special-chars.html)

## Recon

A file called `-`

## Approach

- Using `ls` to display the directory's contents.
- Found a file called `-`
- Use file path to open the file using cat instead of just the name of the file.

## Commands

- cat ./-
- cat < -

## Gotchas / Mistakes

- Trying to access or find the file without its path.
- Since `-` is used as an argument in commands, the terminal is expecting some sort of flag after the hypen but if none is used the command just stalls. To find a file that is the name of a special character, using its file path is the correct appraoch.

## Password Found

```
PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

- Learned about using the file path to find and access files.

## Related Levels

- [[Level 0 - Level 1]]
- [[Level 2 - Level 3]]
