# shark on wire 1

Category: #Forensics 
Level: #Medium 
Author: #Danny 
Tags:

---

## Challenge

> We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/134d2a2cf6ec5b7e757effc9b32977af7cc324b8e99a5ddb64737794a14dc18d/capture.pcap). Recover the flag.

## Files

- None 

## Hints

1. Try using a tool like Wireshark, What are streams?

---

## Initial Observations

Checking the packet streams in Wireshark

---

## Analysis

The challenge is asking to recover a flag from a packet capture. The hint provided implies to check some kind of stream.

An [online search](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html) points to Wireshark's **Follow Stream** feature. This allows an analyst to reconstruct and inspect the data exchanged within a particular TCP or UDP stream.

To follow a stream, select a relevant packet and choose **Analyze → Follow → UDP Stream**. Wireshark reconstructs the data belonging to that particular stream and displays it in sequence.

>[!Quote] Protocol Streams
>The stream content is displayed in the same sequence as it appeared on the network. Non-printable characters are replaced by dots. Traffic from the client to the server is colored red, while traffic from the server to the client is colored blue.

Since the hint specifically mentions streams, I inspected the TCP and UDP traffic to see whether either contained readable data. The TCP streams did not contain anything useful, but the UDP streams contained readable data. After checking the UDP streams, I found two strings that appeared to be flags. Stream 6 contained the likely flag, while Stream 7 contained a deliberately misleading value.

```
picoCTF{StaT31355_636f6e6e} - Stream 6
picoCTF{N0t_a_fLag} - Stream 7
```

Since there are 2 flags, both of them will be submitted to see which is right.

---

## Solution

- Open the packet capture file in Wireshark.
- Select a UDP packet from the list.
- Select Analyze - Follow - Follow UDP Stream
- Go through streams until you find the flag.


## Other Tools

- Wireshark

---

## Flag

```
picoCTF{StaT31355_636f6e6e}
```

---

## Key Takeaways

- Packet captures (`.pcap` files) contain network traffic that can be inspected to recover information transmitted over a network.
- **Wireshark streams** allow related packets to be reconstructed into a continuous conversation, making it easier to inspect the actual data being transmitted.
- UDP traffic can contain useful application data even though UDP does not establish a connection like TCP.
- Not every piece of text that looks like a flag is necessarily the correct flag. In this challenge, `picoCTF{N0t_a_fLag}` was intentionally misleading.

---

## References

- [Wireshark User's Guide — Following Protocol Streams](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html)
- [Wireshark](https://www.wireshark.org/)

## Related Concepts

- Packet capture (`.pcap`)
- Network traffic analysis
- Wireshark
- UDP streams
- TCP streams
- Protocol analysis
- Network forensics
- Packet inspection