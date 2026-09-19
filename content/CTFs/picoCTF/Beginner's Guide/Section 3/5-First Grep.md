---
publish: true
---

# First Grep

Category: #General_Skills 
Level: #Easy 
Author: #Alex_Fulton #Danny_Tunitis 
Tags: None

---

## Challenge

> Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.
> 
> The flag is in this [file](https://challenge-files.picoctf.net/c_fickle_tempest/d0b2e96347614d19414d591c946a1789fa8bd35487fcbfabf9437d0acfcaa503/file).



## Files

- [file](https://challenge-files.picoctf.net/c_fickle_tempest/d0b2e96347614d19414d591c946a1789fa8bd35487fcbfabf9437d0acfcaa503/file)

## Hints

1. grep tutorial

---

## Initial Observations

I am assuming that the file has a lot of text in it with the flag buried within a string so it won't be enough to just use the `strings` command.

---

## Analysis

This is one of the easier challenges since grep is such a useful tool. Using `cat` on the file returns its contents, it doesn't look like the flag is going to be by itself on a single line. Since `picoCTF` flags follow a predictable format (`picoCTF{...}`), I can use `grep` with a regular expression to search for this pattern instead of manually reading through the file.

For reference on the patterns see [Regex](https://www.rexegg.com/regex-quickstart.php)

---

## Solution

### Commands

```bash
grep -E "picoCTF\{.*\}"
```
This is will highlight the flag in the file. From what I have read, it should be printing only the flag to the terminal, maybe the whole file is one big string.

I have just read that if you want only the match to be in the output, you should include the `o` option in the command.

```bash
grep -oE "picoCTF\{.*\}"
```
### Other Tools

- strings
- grep
- file

---

## Flag

```
picoCTF{grep_is_good_to_find_things_e3C4b360}
```

---

## Key Takeaways

- `grep` is a powerful command-line tool used to search for patterns inside files or command output.
- By default, `grep` returns the entire line containing the matched pattern, not only the matching text.
- Regular expressions can be used with `grep` to create more flexible search patterns.
- The `-E` option enables Extended Regular Expressions, allowing operators such as `+`, `?`, `|`, and `{}` to be used without escaping.
- Searching with tools like `grep` is much faster and more reliable than manually inspecting large files.

---

## References

- picoCTF - First Grep Challenge
- https://man7.org/linux/man-pages/man1/grep.1.html
- https://en.wikibooks.org/wiki/Regular_Expressions/POSIX-Extended_Regular_Expressions
- https://www.gnu.org/software/grep/manual/

## Related Concepts

- Linux Command Line
- `grep`
- Regular Expressions (Regex)
- Extended Regular Expressions (ERE)
- Pattern Matching
- Text Searching
- Unix Pipes (`|`)