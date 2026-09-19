---
publish: true
---

# vault-door-training

Category: #Reverse_Engineering
Level: #Easy 
Author: #Mark_E_Haase
Tags:

---

## Challenge

> Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility.

## Files

- The source code for the training vault is here: [VaultDoorTraining.java](https://challenge-files.picoctf.net/c_fickle_tempest/f2743327a75583885f4aa22e3c9856618fd0e95dbfa56f1bf889bd322a45f1a2/VaultDoorTraining.java)

## Hints

1. None

---

## Initial Observations

This challenge involves Java, a shift from Python.

---

## Analysis

Since the challenge provides Java source code rather than a compiled binary, this is a static analysis task.

Similar to how I would start in the Password Crack series, I will open the provided `.java` file in an IDE for inspection. Having some experience with Java, I can understand the code that has been provided.

It looks like there is one class which has the main method inside it. It creates an instance of the class called `vaultDoor` and there is a scanner to take input, a password in the form of the flag, from the user. Next, the program is creating a substring by extracting the portion between '{' and '}'.

Lastly there is an if statement that checks the input against the password in the boolean method at the end of the file, which has the password in plaintext.

In my solution I also closed the scanner which is best practice to avoid issues like memory leaks.

---

## Solution

### Java

```java
// The password is below. Is it safe to put the password in the source code?

// What if somebody stole our source code? Then they would know what our

// password is. Hmm... I will think of some ways to improve the security

// on the other doors.

//

// -Minion #9567

public boolean checkPassword(String password) {

return password.equals("w4rm1ng_Up_w1tH_jAv4_000iPnsaWOY");

```

### Other Tools

- VS Code which was used for inspecting the code.

---

## Flag

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_000iPnsaWOY}
```

---

## Key Takeaways

- Hardcoding secrets (passwords, keys, tokens) directly in source code is a serious vulnerability if that source is ever leaked, decompiled, or otherwise exposed.
- Static analysis is often enough to solve reverse engineering challenges when the logic is simple and the secret is stored in plaintext.
- Understanding basic string operations (`substring()`, `.equals()`) is enough to trace how user input maps to a validation check.
- The developer's own in-code comment was a deliberate hint pointing at the vulnerability being demonstrated, comments in provided source are worth reading closely, not skipping.

---

## References

- https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html
- https://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-
- https://en.wikipedia.org/wiki/Security_through_obscurity

## Related Concepts

- Static Code Analysis
- Reverse Engineering
- Hardcoded Credentials
- Java String Methods
- Source Code Exposure Risk