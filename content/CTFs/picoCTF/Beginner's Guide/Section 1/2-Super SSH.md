---
publish: true
---

# Super SSH

Category: #General_Skills
Level: #Easy
Author: #Jeffrey_John
Tags: #shell #ssh #browser_webshell_solvable

## Challenge

Using a Secure Shell (SSH) is going to be pretty important.

Can you `ssh` as `ctf-player` to `titan.picoctf.net` at port `49173` to get the flag?

You'll also need the password `84b12bae`. If asked, accept the fingerprint with `yes`.

If your device doesn't have a shell, you can use: [](https://webshell.picoctf.org/)[https://webshell.picoctf.org](https://webshell.picoctf.org/)

If you're not sure what a shell is, check out our Primer: [](https://primer.picoctf.com/#_the_shell)[https://primer.picoctf.com/#_the_shell](https://primer.picoctf.com/#_the_shell)

### Hints

1. https://linux.die.net/man/1/ssh
2. You can try logging in 'as' someone with `<user>`@titan.picoctf.net
3. How could you specify the port?
4. Remember, passwords are hidden when typed into the shell


## Approach

For this challenge I have to use ssh, which I have seen before but I do not know the syntax. By using the first hint, I am taken to a page that teaches me how to use it.

After checking it out, I'm more lost... so I'm going to use a trusted source, GeeksforGeeks.

After visiting [GFG](https://www.geeksforgeeks.org/linux-unix/ssh-command-in-linux-with-examples/) , I now have the syntax for ssh and I can begin the challenge. The syntax to use ssh, in this capacity at least is:
```bash
ssh [username]@[hostname or IP address]
```
That's the basics of using it at least. In the challenge, a port is also provided which means I will have to use the `-p` option with ssh to complete it, resulting in:

```bash
ssh -p 49173 ctf-player@titan.picoctf.net
```

Running this is the web shell results in
![[Pasted image 20260720165955.png]]

Flag: picoCTF{s3cur3_c0nn3ct10n_07a987ac}

This is the end of the challenge. On to the next.