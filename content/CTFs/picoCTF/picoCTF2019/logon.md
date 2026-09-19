# logon

Category: #Web_Exploitation 
Level: #Easy 
Author: #bobson
Tags: 

---

## Challenge

> The factory is hiding things from all of its users.
> 
> Can you login as Joe and find what they've been looking at? [http://fickle-tempest.picoctf.net:56533](http://fickle-tempest.picoctf.net:56533/)

## Files

- None

## Hints

1. Hmm it doesn't seem to check anyone's password, except for Joe's?

---

## Initial Observations

DevTools will most likely be useful

---

## Analysis

The challenge asks to find out what the factory has been hiding from its users. When on the challenge webpage, I am presented with a log in screen with username and password fields. Trying to log in as Joe returns an error essentially saying that the password can't be found via brute force methods.

The hint suggests that only Joe's password is checked, so logging in as a random user succeeds and the information provided is "Success: You logged in! Not sure you'll be able to see the flag though." Which means the flag has to found in a different way, maybe by inspecting the source code.

An inspection of the source code doesn't provide anything useful. An online search points to checking the Network tab within DevTools. The Network tab allows developers to monitor, inspect, and debug all network requests and responses made by a webpage.

With the Network tab open, I logged in as a random user again and found a `flag` entry. I checked the `Response` and found that the page was returned with the success message. Looking at the response headers, I found several cookies, including `username`, `password`, and `admin`. The `admin` cookie was set to `False`.

This is interesting because cookies are stored on the client side and can be modified by the user. If the application is using the value of the `admin` cookie to determine whether a user has administrative privileges, then changing it from `False` to `True` may bypass the application's access control.

An online search leads to the `Application` tab which allows developers to inspect, manage, and debug all aspects of a web app’s storage, service workers, cache, and background services directly from the browser. While logged in, I found the cookies and set the admin cookie to True and refreshed, which returned the flag.

**The vulnerability is not that the cookie can be edited. The vulnerability is that the server trusts the edited cookie.**

Users can always modify information stored on their own computer. A secure application must assume that client-side values such as cookies, form fields, and JavaScript variables can be manipulated and must verify authorization using trusted server-side state.

---

## Solution

1. Go to the Factory login page.
2. Login with a random username and password.
3. Open DevTools and open the Network and look in the headers and find the cookies for username, password, and admin
4. Go to the Application tab and find the cookies for the page and change the admin cookie from False to True and reload the page without logging out.
5. The flag is then displayed on the screen.

### Other Tools

- **Browser Developer Tools** — used to inspect network requests, response headers, and cookies.
- **Application/Storage panel** — used to view and modify cookies stored by the browser.

---

## Flag

```
picoCTF{th3_c0nsp1r4cy_l1v3s_4d184b0d}
```

---

## Key Takeaways

- **Never trust client-controlled data for authorization.** Cookies are stored on the user's machine and can be modified.
- Authentication and authorization are different concepts. Successfully logging in does not necessarily mean that the user has permission to access administrative resources.
- The `admin` cookie should not be trusted as proof that a user is an administrator. The server should determine the user's privileges using trusted server-side information.
- Browser Developer Tools can be used to inspect HTTP requests, responses, headers, cookies, and other information exchanged between the client and server.
- The Network tab is particularly useful when investigating how a web application communicates with its backend.
- An authorization vulnerability can allow a normal user to gain access to functionality intended for an administrator.

---

## References

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- https://developer.mozilla.org/en-US/docs/Tools
- https://owasp.org/www-community/attacks/Vertical_Privilege_Escalation

## Related Concepts

- Cookies
- HTTP Headers
- HTTP Requests and Responses
- Authentication
- Authorization
- Access Control
- Privilege Escalation
- Client-Side Data
- Web Application Security