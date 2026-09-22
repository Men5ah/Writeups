---
tags:
  - otw
  - bandit
level: "5"
publish: false
---
# Bandit Level 5 → 6

## 🔗 Connection Info

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:

- human-readable
- 1033 bytes in size
- not executable

## Concepts / Commands Used

- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)
## Recon

What files/state exist at login (`ls -la`, `cat readme`, etc.)

## Approach

Step-by-step reasoning — what you tried and why.

## Commands

```bash
Command
```

## Gotchas / Mistakes

Anything that tripped you up, weird escaping, whitespace, hidden files, etc.

## Password Found

```
||password-goes-here||
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

Freeform — new tool, technique, or Linux concept worth remembering.

## Related Levels

- [[Bandit Level {{level-1}}]]
- [[Bandit Level {{level+1}}]]
