---
tags:
  - otw
  - bandit
level: "3"
publish: true
---
# Bandit Level 3 → 4

## 🔗 Connection Info

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in a hidden file in the **inhere** directory.

## Concepts / Commands Used

- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)
## Recon

What files/state exist at login (`ls -la`, `cat readme`, etc.)

## Approach

- After a google search, it seems that using the `-a` flag with `ls` displays ALL files in the directory.

- Used `ls` to find the `inhere` directory
- Used `cd` to change directory to enter `inhere`
- Used `ls -a` to print all the files in the directory whether hidden or not.
- Use `cat` normally to display the content of the hidden file.

## Commands

```bash
cat ...Hiding-From-You
```

## Gotchas / Mistakes

- Not knowing the flags and options associated with the commands can delay time. Using the `man` pages/online search is useful.

## Password Found

```
xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

- using the `-a` ALL flag with `ls`

## Related Levels

- [[Level 2 - Level 3]]
- [[Level 4 - Level 5]]
