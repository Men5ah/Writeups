---
publish: true
---

# Glory of the Garden

Category: #Forensics 
Level: #Easy 
Author: #Danny / #jedavis
Tags:

---

## Challenge

> This file contains more than it seems.

## Files

- [garden.jpg](https://challenge-files.picoctf.net/c_fickle_tempest/6013221da747114c37db29c554381dbe4bb4e746cf6bd880f9c3b5d0b495a823/garden.jpg).

## Hints

1. What is a hex editor?
---

## Initial Observations

The file provided is jpg, which probably means it has something to do with the binary within the file.

---

## Analysis

The challenge says "This file contains more than it seems." When I open the image normally, it appears to be an ordinary picture of a garden with no obvious visual clues, so I need to inspect the file itself.

I initially tried using `cat` and `nano`, but these are not suitable for examining the raw contents of a JPEG file. The hint specifically mentions a hex editor, so I used [Hexed](https://hexed.it/) to inspect the hexadecimal representation of the file.

Searching the file for `picoCTF` revealed the flag near the end of the file. This indicates that there is additional readable data stored within the JPEG that is not visible when viewing the image normally.

There is also a simpler command-line approach. The `strings` command extracts sequences of printable characters from binary files. I can then pipe its output into `grep` and search specifically for the expected `picoCTF{...}` pattern.

---

## Solution

### Commands

```bash
strings garden.jpg | grep -oE "picoCTF\{.*\}"
```

### Other Tools

- **Hexed** — used to inspect the raw hexadecimal contents of the JPEG.
- **`strings`** — extracts printable character sequences from binary files.
- **`grep`** — searches the extracted strings for the flag pattern.

---

## Flag

```
picoCTF{more_than_m33ts_the_3y339140129}
```

---

## Key Takeaways

- A file can contain information that is not visible when the file is opened normally.
- **File extensions do not guarantee that a file contains only the expected type of data.** A JPEG can contain additional data after the normal image data.
- A hex editor can be useful when investigating the raw contents of a binary file.
- `strings` is useful for finding human-readable text embedded inside binary files.
- Combining `strings` with `grep` makes it possible to quickly search a binary file for a known pattern such as `picoCTF{...}`.
- This is a basic example of **digital forensics**, where the underlying data of a file is examined rather than relying only on what the file displays.

---

## References

- [https://hexed.it/](https://hexed.it/)
- [https://man7.org/linux/man-pages/man1/strings.1.html](https://man7.org/linux/man-pages/man1/strings.1.html)
- [https://man7.org/linux/man-pages/man1/grep.1.html](https://man7.org/linux/man-pages/man1/grep.1.html)

## Related Concepts

- Digital Forensics
- Binary Files
- Hexadecimal
- Hex Editors
- File Structure
- Data Hiding
- `strings`
- `grep`
- Regular Expressions
- JPEG File Format