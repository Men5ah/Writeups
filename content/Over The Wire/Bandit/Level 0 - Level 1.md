---
tags:
  - otw
  - bandit
level: "0"
publish: true
---
# Bandit Level 0 → 1

## 🔗 Connection Info

```bash
ssh bandit{{level}}@bandit.labs.overthewire.org -p 2220
```

## Goal

> The password for the next level is stored in a file called **readme** located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

## Concepts / Commands Used

- ls
- cd
- cat
- file
- du
- find
## Approach

- I wanted to know what I was working with. Used `ls` to display the contents of the folder.
- Only one file in the folder. Used `cat` to display its content.
- This output the password into the terminal.

## Commands

- ls
- cat

## Gotchas / Mistakes

None

## Password Found

```
6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR
```

_(double pipes = Obsidian spoiler-style highlight, remove if not using that plugin)_

## Notes / Things Learned

- Using ls to print the contents of the current folder.
- Using cat to display the contents of a file.
## Related Levels

- [[Level 0]]
- [[Level 1 - Level 2]]
