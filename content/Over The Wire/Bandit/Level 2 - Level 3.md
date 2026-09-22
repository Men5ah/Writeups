---
tags:
  - otw
  - bandit
level: "2"
publish: true
---
# Bandit Level 2 → 3

## 🔗 Connection Info

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in a file called `--spaces in this filename--` located in the home directory

## Concepts / Commands Used

-  [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)
- [Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)

## Recon

- A file called `--spaces in this filename--`

## Approach

- Used `ls` to print the directory's contents.
- Used a combination of the file path and quotes to `cat` the file's contents into the terminal. File path because the file name starts with `--` and the quotes because the file name has white spaces in it.

## Commands

- cat ./"--spaces in this filename--"

## Gotchas / Mistakes

- Trying to used the file path alone since it starts with a special character returned a `No such file or directory` error. This is because the terminal treats whitespaces as a separator.
- To prevent this, use single or double quotes when referring to a file or directory with spaces in its name.

## Password Found

```
7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

- Use quotes when you have whitespaces.

## Related Levels

- [[Level 1 - Level 2]]
- [[Level 3 - Level 4]]
