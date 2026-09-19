---
publish: true
---

# Insp3ct0r

Category: #Web_Exploitation
Level: #Easy 
Author: #zaratec/danny
Tags: None

---

## Challenge

> Kishor Balan tipped us off that the following code may need inspection:

## Files

- http://fickle-tempest.picoctf.net:50661/

## Hints

1. How do you inspect web code on a browser?
2. There's 3 parts

---

## Initial Observations

This is a web exploitation challenge so most likely will require me to use the inspector.

---

## Analysis

When the provided link is clicked, a simple website is presented with title "My First Website :)". There are 2 buttons labeled "What" and "How". The first one, when clicked displays "I made a website".
![[Pasted image 20260731221808.png]]

The second button, when clicked displays
![[Pasted image 20260731221858.png]]

Now to check the inspector by right clicking the page and selecting the `Inspector` button at the bottom. Now I can see the HTML code that makes up the page. By expanding the code blocks, I can see what HTML tags were used for various sections of the page. There is nothing in the `<head></head>` portion so I'll check the body. Hidden inside a `div` there is a comment that provides 1/3 of the flag.
```HTML
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

I'm going to assume that the rest of the flag can be found in the CSS and JavaScript(JS) files. In the `Sources` tab in the Developer Tools section, i can see all the files that make up this website. Checking in the CSS file, the second part of the flag can be found as a comment at the bottom.
```CSS
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```

So checking in the JS file gives me
```javascript
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?302945a7} */
```

---

## Solution

- Inspect the webpage.
- Go through the HTML file to find part 1/3 of the flag
- Go into the Sources tab within the developer tools window
- Find the CSS and JS files
- Get parts 2/3 and 3/3 of the flag.
### Other Tools

- 

---

## Flag

```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
```

---

## Key Takeaways

- Browser Developer Tools (DevTools) are invaluable for inspecting the structure and resources of a web page.
- HTML, CSS, and JavaScript files can contain comments, hidden text, or other information that is not visible when viewing the rendered page.
- The **Elements** (Inspector) tab allows you to inspect and modify the HTML of a page, while the **Sources** tab lets you view the website's source files.
- When a challenge mentions "inspection," checking the HTML, CSS, JavaScript, and page comments should be one of the first steps.
- CTF web challenges often distribute information across multiple resources, requiring you to inspect every file loaded by the page.

---

## References

- picoCTF - Insp3ct0r Challenge
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools
- https://developer.chrome.com/docs/devtools
- https://firefox-source-docs.mozilla.org/devtools-user/

## Related Concepts

- Browser Developer Tools (DevTools)
- HTML Comments
- CSS Comments
- JavaScript Comments
- Client-Side Source Code
- Web Reconnaissance
- HTML
- CSS
- JavaScript