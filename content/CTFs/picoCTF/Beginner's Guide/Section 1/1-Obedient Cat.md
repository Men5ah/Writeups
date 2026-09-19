---
publish: true
---
# Obedient Cat

Category: #General_Skills
Level: #Easy
Author: #Syreal

## Challenge

This file has a flag in plain sight (aka "in-the-clear").

[flag](https://challenge-files.picoctf.net/c_wily_courier/8d63e440ec205416efd07e5c9f9ea0ab050fe3f4c8fc30bebfcca22f0c902491/flag)

### Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2.   To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget and a link to the flag. The link can be copied from the details section.
3. $ man cat


## Approach

This challenge has provided a file that has the flag in plain sight. When downloaded, it seems like the file has no extension and thus the system can't decide which text editor to open it with.
![[Pasted image 20260719165542.png]]

If opened with Notepad, the flag is right there on the first line as follows
![[Pasted image 20260719165659.png]]
flag: picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}

This is an easy challenge, however, the hints suggest completing this in the terminal.

In the web shell, I'll use
```powershell
$ wget <link>
```
to download the file provided, replace <link> with the link to the file.

Once downloaded I'll use
```powershell
$ man cat
```
to pull up the manual, which provides detailed documentation, for the `concatenate` command.

Alternatively, I can use
```powershell
$ cat --help
```
but will focus on the version provided in the hint.

when I call `man cat`, I get something like this
![[Pasted image 20260720082647.png]]
showing me how to use the command.

For this challenge, I will go ahead and use
```powershell
cat flag
```

and my output should be the same as the first approach I used.
![[Pasted image 20260720083641.png]]

This is the end of the first challenge, now using the cat command shouldn't be too difficult when needed. On to the next!

Next Challenge
[[2-Super SSH]] 