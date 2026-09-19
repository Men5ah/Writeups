---
publish: true
---

# Big Zip

Category: #General_Skills 
Level: #Easy 
Author: #Syreal 
Tags:

---

## Challenge

> Unzip this archive and find the flag.

## Files

- https://artifacts.picoctf.net/c/504/big-zip-files.zip

## Hints

1. Can grep be instructed to look at every file in a directory and its subdirectories?

---

## Initial Observations

The hint suggests grep to look into every directory, so I'll have to look into that.

---

## Analysis

The challenge name and prompt both point to `unzip` as the first step: 

```bash
unzip big-zip-files.zip
```

This extracts a large, deeply nested set of directories and files, too many to search one at a time. Since this challenge involves `grep`, I could reuse the pattern-matching approach from [[5-First Grep]] and [[4-strings it]]] to search for the flag format directly:

Since I know that grep is used to find patterns using regular expressions, I can write the command to find it straight away.
```bash
grep -oE "picoCTF\{.*\}"
```

There is a slight issue however. There are so many directories inside the zipped folder provided. It will be far too difficult to run grep for each directory and folder. The hint suggests that there is a way to look in each directory and subdirectory so I'll use `man` to pull up the manual.

After some reading I found this:

>[!note] Grep Manual
-r, --recursive:
Read all files under each directory, recursively, following symbolic links only if they are on the command line.  Note that if no file operand is given, grep searches the working directory.  This is equivalent to the -d recurse option.

By adding this to the command, it should return the flag I need.

The syntax for `grep` is:
```bash
grep [OPTION] PATTERNS [FILE]
```
So the new option `-r` should be part of the options. 

---

## Solution

### Commands

```bash
grep -roE "picoCTF\{.*\}"
# Assuming you are in the big-zip-files folder
```

```bash
grep -roE "picoCTF\{.*\}" big-zip-files
# If you are not in the big-zip-files folder
```
### Python (if applicable)

```python
pass
```

### Other Tools

- `unzip` (to extract the archive before searching)
- `man` (to look up `grep`'s recursive option)

---

## Flag

```
picoCTF{gr3p_15_m4g1c_ef8790dc}
```

---

## Key Takeaways

- `grep` does not search subdirectories by default, the `-r` (or `--recursive`) flag is required to traverse an entire directory tree.
- When a task involves searching many files across nested folders, checking `man <command>` for a recursive/bulk option is faster than trying to script a manual loop.
- Combining flags (`-r`, `-o`, `-E`) lets `grep` do targeted, recursive, pattern-only extraction in a single command instead of multiple passes.
- Always unzip/extract an archive as the first step when the prompt calls for it, it's easy to skip mentioning in a writeup even though it's a required action.

---

## References

- https://man7.org/linux/man-pages/man1/grep.1.html
- https://linux.die.net/man/1/unzip

## Related Concepts

- Regular Expressions
- Recursive File Search
- Command-Line Archive Extraction
- Pattern Matching
- Filesystem Traversal