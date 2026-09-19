# dont-use-client-side

Category: #Web_Exploitation 
Level: #Easy 
Author: #Alex_Fulton #Danny
Tags:

---

## Challenge

> Can you break into this super secure portal
## Files

- None

## Hints

1. Never trust the client

---

## Initial Observations

This challenge will deal with the client side, the Inspector should prove useful here.

---

## Analysis

Once the instance is launched, I am presented with a website with a textbox asking for valid credentials. Since the hint provided said to not trust the client, the solution is possibly located in the client side of this application.

Using the Inspector, I can see the `html` and `js` code used on the page. Expanding the second `<script>` tag, there is a `js` function. Find the code below:

```javascript

  function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'eb02') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_2') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'b45}') {
                  alert("Password Verified")
                  }
                }
              }
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
    
  }

```

1. It stores the text entered in the textbox.
2. It then uses 8 nested if statements to verify separate parts of `checkpass` by checking 4 characters at a time using the split to set the start and end indices for the comparison.
3. If all of them are correct, an alert is shown on the screen that says "Password Verified".

By rearranging the checks in order of index, the flag can be assembled.

This is to emphasize that in a web application, the client is the user's browser. Any HTML, CSS or JavaScript sent to the browser can be inspected by the user. therefore, client-side JS should **never be responsible for enforcing security-sensitive operations.**

---

## Solution

1. Open the webpage
2. Go in the Inspector
3. Expand the second `script` tag
4. Rearrange the flag in order of index.
### Other Tools

- Browser Developer Tools / Inspector
- JavaScript

---

## Flag

```
picoCTF{no_clients_plz_2eb02b45}
```

---

## Key Takeaways

- Client-side code should not be trusted for security because users can inspect and modify it.
- JavaScript running in the browser is visible to the user, so sensitive information such as passwords or authentication logic should not be stored there.
- `substring(start, end)` extracts characters starting at `start` and stopping before `end`.
- When analyzing obfuscated or unordered checks, examining the indexes can reveal the intended order of the data.
- Authentication should be performed on the server rather than relying solely on client-side JavaScript.

---

## References

- https://developer.mozilla.org/en-US/docs/Web/API/Window/alert
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring

## Related Concepts

- Client-Side Security
- JavaScript
- Browser Developer Tools
- Authentication
- Input Validation
- Source Code Inspection
- `substring()`
- Web Security