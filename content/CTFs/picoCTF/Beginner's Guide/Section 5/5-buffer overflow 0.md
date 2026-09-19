# buffer overflow 0

Category: #Binary_Exploitation
Level: #Medium 
Author: #Alex_Fulton #Palash_Oswal
Tags: #gets

---

## Challenge

>Let's start off simple, can you overflow the correct buffer? The program is available [here](https://artifacts.picoctf.net/c/173/vuln). You can view source [here](https://artifacts.picoctf.net/c/173/vuln.c).

## Files

- In challenge description

## Hints

1. How can you trigger the flag to print
2. If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
3. Run `man gets` and read the BUGS section. How many characters can the program really read?

---

## Initial Observations

This is something completely new. I should start with doing some research on Buffer Overflows.

---
## Analysis

Since `vuln.c` is provided, static analysis is possible even without deep C fluency — the key is identifying the vulnerable buffer and the function that reads input into it.

```c
void vuln(char *input){
    char buf2[16];
    strcpy(buf2, input);
}
```

`buf2` is a 16-byte character buffer, so in theory 17+ bytes of input should overflow it. However, the more important detail — flagged directly by hint #3 — is *how* input reaches this buffer in the first place. Checking `main()`, input is read using `gets()`:

```c
gets(input);
```

`gets()` is a deprecated, unsafe C function because it performs **no bounds checking whatsoever**, it will keep reading characters from stdin until a newline is encountered, regardless of the size of the destination buffer. This means there's nothing stopping input from writing past the end of `buf2` and into adjacent memory on the stack, which is exactly what a classic stack buffer overflow relies on.

Locally, I first created a `flag.txt` file to compile and test against (the program checks for this file and creates a placeholder debug flag if one isn't present). Feeding the program short input (under 16 characters) behaved normally and the program exited. Feeding it 50 `A` characters, well beyond the 16-byte buffer, caused the debug flag to print, confirming that overflowing `buf2` overwrites something (likely adjacent stack memory controlling program flow) that ultimately triggers the flag-printing path.

With the mechanism confirmed locally, the same approach, providing an oversized input, was used against the remote CyLab Security Academy instance to retrieve the real flag.

---

## Solution

If you can run C code, first compile `vuln.c` and make sure that it's an older version of C since one of the methods here, `gets` has been deprecated, which is the reason why the overflow works in the first place.

1. Connect to the CyLab Security Academy instance.
2. When prompted for input, enter 50 characters
3. Copy the key and submit it

### Command for debugging

```bash
gcc -std=gnu89 vuln.c -o vuln  # to compile without error

./vuln # to run the compiled file.
```

### Other Tools

- `gcc` (specifically an older C standard, since `gets()` is removed in modern C standards and needs `-std=gnu89` to compile)
- `man` (to read the BUGS section of `gets()` documentation, per hint #3)
- A remote shell/netcat-style connection (to interact with the CyLab Security Academy instance and retrieve the actual flag)

---

## Flag

```
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}
```

---

## Key Takeaways

- `gets()` performs no bounds checking and is fundamentally unsafe , it reads input until a newline no matter how large the destination buffer is, making it a textbook cause of stack buffer overflows. It's deprecated in modern C for exactly this reason.
- A buffer overflow doesn't require exact precision to be useful — overflowing well past the buffer size (e.g., 50 bytes into a 16-byte buffer) can be enough to hit adjacent memory and trigger unintended behavior.
- Reading provided source code, even without full fluency in the language, can reveal the exact vulnerable function and buffer size — look for buffer declarations (`char buf[N]`) paired with unsafe input functions (`gets`, `strcpy`, `sprintf` without size limits).
- Testing locally with a placeholder flag file before connecting to the remote/live instance is a safe way to confirm an exploit mechanism works before using it against the real target.
- Compiling with an older C standard (`-std=gnu89`) may be necessary to reproduce vulnerable behavior from deprecated functions, since modern compilers may reject or alter it.

---

## References

- https://man7.org/linux/man-pages/man3/gets.3.html
- https://owasp.org/www-community/vulnerabilities/Buffer_Overflow
- https://en.wikipedia.org/wiki/Stack_buffer_overflow

## Related Concepts

- Stack Buffer Overflows
- Unsafe C Functions (`gets`, `strcpy`)
- Stack Memory Layout
- C Compilation Standards
- Binary Exploitation Fundamentals
- Bounds Checking (or lack thereof)