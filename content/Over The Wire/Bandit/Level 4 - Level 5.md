---
tags:
  - otw
  - bandit
level: "4"
publish: true
---
# Bandit Level 4 → 5

## 🔗 Connection Info

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in the only human-readable file in the **inhere** directory. Tip: if your terminal is messed up, try the “reset” command.

## Concepts / Commands Used

- [ls](https://manpages.ubuntu.com/manpages/noble/man1/ls.1.html) , [cd](https://manpages.ubuntu.com/manpages/noble/man1/cd.1posix.html) , [cat](https://manpages.ubuntu.com/manpages/noble/man1/cat.1.html) , [file](https://manpages.ubuntu.com/manpages/noble/man1/file.1.html) , [du](https://manpages.ubuntu.com/manpages/noble/man1/du.1.html) , [find](https://manpages.ubuntu.com/manpages/noble/man1/find.1.html)
## Recon

- Directory called `inhere`
- 10 files labeled `-file00` to `-file09`

## Approach

- Stepped into `inhere`
- `ls` displayed 9 files. According to the goal, only one of them is human readable.
- Use file to display information about each file. 7 of them show up as "data", 1 is am OpenPGP Public Key, 1 is binary text, and 1 of them is ASCII text (which is the human readable one)
- Use `cat` to display the files contents.

## Commands

```bash
cat < -file07
```

## Gotchas / Mistakes

- Performing the file command one at a time for all 9 files.
- Much quicker to use `file ./*`

## Password Found

```
6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

- Using * when needing to represent "all" inside a directory

## Related Levels

- [[Level 3 - Level 4]]
- [[Level 5 - Level  6]]
