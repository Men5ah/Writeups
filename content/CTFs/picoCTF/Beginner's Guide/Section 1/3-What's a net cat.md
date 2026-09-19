
# What's a Net Cat

Category: #General_Skills
Level: #Easy
Author: #Sanjay_C #Danny_Tunitis 
Tags: 


## Challenge

Using netcat (nc) is going to be pretty important. Can you connect to `fickle-tempest.picoctf.net` at `port 60128` to get the flag?

### Hint

1. nc tutorial



## Approach

For this challenge, I will have to use net cat as the title suggests. I have never used the net cat tool before so following the hint, I look for a [tutorial](https://www.geeksforgeeks.org/linux-unix/netcat-basic-usage-and-overview/).

> [!Quote] Netcat
> Netcat is a versatile Unix utility that facilitates reading and writing data across network connections using either TCP or UDP protocols. Often referred to as the "Swiss Army knife" of networking, Netcat can perform a wide range of tasks, including connecting to remote servers, listening for incoming connections, and transferring files.

### Syntax

```bash
nc [options] [hostname] [port]
```
This command establishes connections or listens for incoming connections, depending on the specified options.

For options, you can `man netcat` in your Linux terminal.

With that being said, type the command in terminal (assuming that you are connected to Cylab via your terminal). And the result is:
![[Pasted image 20260728193218.png]]

Flag: picoCTF{nEtCat_Mast3ry_aC66D475}

This is the end of the challenge. On to the next.

