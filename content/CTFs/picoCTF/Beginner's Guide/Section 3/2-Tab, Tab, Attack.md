# Tab, Tab, Attack

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.

## Files

- [Addadshashanammu.zip](https://challenge-files.picoctf.net/c_wily_courier/730d9106a6ce1d52c6463b90937ec89f5eb661388954fbd15cfa0c8a2eec012f/Addadshashanammu.zip)

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...
---

## Initial Observations

In the hint provided, it seems like the challenge might have something to do with unzipping the folder provided.

---

## Analysis

First, I need to figure out how to unzip a folder in the terminal. The command to unzip a folder in the terminal is `unzip`

```bash
unzip folder.zip

unzip folder.zip -d path/to/destination
```

Once unzipped, I can `cd` into that new directory, and since the name of the folder is so long, I will use `tab` to autocomplete. I can then use a combination of `ls` and `tab` to continue changing the directory until I hit a file in a deeply nested folder.

Although... with unzipping the file, the terminal prints all the nested folders that are being extracted so there is no need to use `ls` anymore. i can just `cd` into the last folder straightaway in one command.

![[Pasted image 20260731210050.png]]

```bash
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
```

Rather than typing each directory name in full, I repeatedly pressed the `Tab` key to autocomplete the next directory name. This is particularly useful when working with long or difficult-to-spell file names, as it saves time and avoids typing errors. By combining `cd` with tab completion, I quickly navigated to the executable.

 I can then `ls` to see what is in the directory. It seems there is a `C` file in there. Following what I learned from the challenge prior to this, I will use `ls -l` to see if it is executable. It is executable so now I can just use `./fang-of-haynekhtnamet` to execute the file.

This ends up giving me:
"*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}"

---

## Solution

### Commands

```bash
unzip Addadshashanammu.zip

cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/

ls -l fang-of-haynekhtnamet

./fang-of-haynekhtnamet
```

### Python (if applicable)

```python
pass
```

### Other Tools

- unzip

---

## Flag

```
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

---

## Key Takeaways

- The `Tab` key can autocomplete file and directory names, reducing typing and preventing spelling mistakes.
- The `unzip` command extracts the contents of ZIP archives into the current directory or a specified destination.
- Commands such as `ls` and `ls -l` are useful for exploring unfamiliar directory structures and checking file permissions.
- Executable files in Linux are run using the `./` prefix, provided they have execute permissions.
- Efficient use of shell features such as tab completion can significantly speed up navigation and reduce errors when working with deeply nested directories.
- 
- 

---

## References

- picoCTF - Tab, Tab, Attack Challenge
- https://man7.org/linux/man-pages/man1/unzip.1.html
- https://www.gnu.org/software/bash/manual/bash.html#Commands-For-Completion
- https://ryanstutorials.net/linuxtutorial/navigation.php

## Related Concepts

- Linux Shell
- Bash Tab Completion
- File System Navigation
- `cd`
- `ls`
- `unzip`
- Executable Files