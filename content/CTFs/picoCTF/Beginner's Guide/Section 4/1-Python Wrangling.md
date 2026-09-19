---
publish: true
---

# Python Wrangling

Category: #General_Skills 
Level: #Medium
Author: #Syreal 
Tags:

---

## Challenge

> Python scripts are invoked kind of like programs in the Terminal...
> Can you run [ende.py](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/ende.py) using [password.txt](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/password.txt) to get [flag.txt.en](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/flag.txt.en)?

## Files

- [ende.py](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/ende.py) 
- [password.txt](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/password.txt) 
- [flag.txt.en](https://challenge-files.picoctf.net/c_wily_courier/a4c97b512a4e6de24045ab3e8294651bcfc241ce571daa8afdad3c35885ffa60/flag.txt.en)

## Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget followed by a link to the script. The link can be copied from the details section.

2. man python

---

## Initial Observations

This challenge will most likely involve using some kind of IDE to make reading and parsing code easier. It will also include some file I/O.

---

## Analysis

Opening up the python file presents some fairly complicated code. From an initial pass of reading the code, I found the usage message and the help message at the top. Running the code output the following:

`Usage: path/to/file/ende.py (-e/-d) [file]`

Which is suggesting to run the file from the terminal in order to add some options and a file. To get some more help, it seems I can use `-h`.

```
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'
```

So that is the format that is expected. From reading the code again, it looks like a password is required, most likely its the one located inside `password.txt`. Instead of copying and pasting, and since I have experience programming in Python, I modified the decryption portion of the script to read the password without me having to copy and paste it into the terminal.

This means that I need to decrypt `flag.txt.en` to get the flag.

---

## Solution

### Commands

```
python ende.py -d flag.txt.en
```

### Python (if applicable)

```python
elif sys.argv[1] == "-d":

	if len(sys.argv) < 4:

		with open('password.txt','r') as pw:

			sim_sala_bim = pw.readline().strip()

	else:

		sim_sala_bim = sys.argv[3]

  

	ssb_b64 = base64.b64encode(sim_sala_bim.encode())

	c = Fernet(ssb_b64)

  

	with open(sys.argv[2], "r") as f:

		data = f.read()

		data_c = c.decrypt(data.encode())

		sys.stdout.buffer.write(data_c)
```

### Other Tools

- **Python 3** for script execution
- **Terminal/Shell** to invoke the script with command-line arguments.
- **`cryptography` library (Fernet)** for decryption
- **VS Code** to inspect and modify the source code.

---

## Flag

```
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

---

## Key Takeaways

- Reading the source code is often faster than blindly trying commands. The script clearly revealed how it expected to receive its password.
- Understanding command-line arguments (`sys.argv`) makes it much easier to use unfamiliar Python scripts.
- Instead of manually copying input every time, automating repetitive tasks (such as reading the password from a file) can simplify the workflow.
- Even when a challenge seems to be about cryptography, the intended skill may actually be understanding how to execute and modify a Python program.
- The help (`-h`/`--help`) and usage messages are valuable sources of information and should be checked before diving into the code.

---

## References

- Python Documentation – sys.argv
- [Python Documentation – base64 Module](https://docs.python.org/3/library/base64.html?utm_source=chatgpt.com)
- [cryptography Documentation – Fernet](https://cryptography.io/en/latest/fernet/?utm_source=chatgpt.com)
- Python Tutorial – Reading and Writing Files

## Related Concepts

- Python scripting
- Command-line arguments (`sys.argv`)
- File input/output (File I/O)
- Symmetric encryption
- Fernet encryption
- Base64 encoding
- Reading source code for reverse engineering
- Linux terminal basics
- Challenge analysis methodology