# 1-First Find

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> Unzip this archive and find the file named 'uber-secret.txt'

## Files

- - [Download zip file](https://artifacts.picoctf.net/c/501/files.zip)

## Hints

None

---

## Initial Observations

This is a new command. Will need a tutorial, no hints suggest that it is simple and straightforward to do.

---

## Analysis

The basic syntax of the `find` command is as follows:
```bash
find [options] [path] [expression]
```

- Options customize the find output e.g. `-name`, -`iname`, and `-type<br>`
- Path instructs `find` where to start looking for the search term
- Expressions tells `find` what to look for.

The archive contains an unknown directory structure, so manually checking each directory would be inefficient. The `find` command is useful because it can recursively search through a directory and its subdirectories for files matching a specified name.

For this challenge, I need to find  a file by name. From this [website](https://phoenixnap.com/kb/guide-linux-find-command), the syntax is as follows.

```bash
find ~ -name "file-name.extension"
find files/ -name "file-name.extension"
find . -name "file-name.extension"
```

The `~` symbol searches the current user's home directory (**`~`**) for any file with the provided name. Alternatively, you can use the actual directory where the zip folder was unzipped (`files/`) or if you want to start searching from the directory you are currently in, use `.`

So after unzipping the file, I used the command above to find `uber-secret.txt`. using the path provided in the output, i can use `cd` to get to the file and use `cat` to retrieve the flag.

This challenge shows a different approach to navigation as compared to [[2-Tab, Tab, Attack]]

---

## Solution

### Commands

```bash
unzip files.zip
find . -name "uber-secret.txt"
cd <path>
cat uber-secret.txt
```


---

### Other Tools

- `unzip` — extracts the provided ZIP archive
- `find` — searches for files and directories matching a specified condition
- `cd` — changes the current working directory
- `cat` — displays the contents of a file

---

## Flag

```
picoCTF{f1nd_15_f457_ab443fd1}
```

---

## References

- https://man7.org/linux/man-pages/man1/find.1.html
- https://phoenixnap.com/kb/guide-linux-find-command
- https://man7.org/linux/man-pages/man1/unzip.1.html

## Related Concepts

- File System Navigation
- File and Directory Search
- Linux Command Line
- Wildcards and Pattern Matching
- Recursive Searching
- File Permissions