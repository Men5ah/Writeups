# where are the robots

Category: #Web_Exploitation 
Level: #Easy 
Author: #zaratec/danny 
Tags: None

---

## Challenge

> Can you find the robots?

[http://fickle-tempest.picoctf.net:56006](http://fickle-tempest.picoctf.net:56006/)

## Files

- None

## Hints

1. What part of the website could tell you where the creator doesn't want you to look?

---

## Initial Observations

I wonder what robots have to do with websites. They probably refer to web crawlers, not physical robots.

---

## Analysis

After starting the instance and visiting the web page, I am presented with this.
![[Pasted image 20260801192200.png]]
It doesn't seem like there clickable elements on the page. I'll check the Inspector. There doesn't seem to be anything hidden in the HTML code. Il check the Sources panel and see there is any CSS or JavaScript. There is only one other file, CSS, and that also has nothing in it that could point me to the flag.

After considering the title of the challenge, I searched online to find out how robots and websites are related to each other. I came across a [Google Developers](https://developers.google.com/search/docs/crawling-indexing/robots/intro) article that is an introduction to `robots.txt`.

> [!quote] `robots.txt`
> A robots.txt file tells search engine crawlers which URLs the crawler can access on your site.

After another search to find where this file may be located, I found out that it should be located in your project's root. It doesn't show up in the Sources panel because the browser did not load/request it automatically. I also saw that I can use `sitename.com/robots.txt` to find it, so I'll try that.

After accessing the robots file, I can see that it is preventing robots from scraping `/cc6b1.html`, the flag is most likely in that file.

---

## Solution

1. Visit the site provided
2. In the url bar, add `/robots.txt` to the end of the url. (http://fickle-tempest.picoctf.net:56006/robots.txt)
3. Find the hidden html file in the list
4. Visit the page with the html file (http://fickle-tempest.picoctf.net:56006/cc6b1.html) and find the flag.
### Other Tools

- DevTools

---

## Flag

```
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}
```

---

## Key Takeaways

- `robots.txt` is a file used by websites to provide instructions to search engine crawlers about which pages should or should not be indexed.
- Disallowed paths in `robots.txt` are not actually protected; they are only suggestions for well-behaved crawlers. Anyone can still manually access those URLs if they know the path.
- Web CTF challenges often use `robots.txt` to reveal hidden files or directories that developers do not want search engines to discover.
- Not every useful file on a website appears in the browser Developer Tools because only resources requested by the page are loaded there.
- When performing web reconnaissance, checking common files such as `/robots.txt` and `/sitemap.xml` is a useful first step.

---

## References

- picoCTF - Where Are The Robots Challenge
- https://developers.google.com/search/docs/crawling-indexing/robots/intro
- https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
- https://www.robotstxt.org/

## Related Concepts

- Web Reconnaissance
- `robots.txt`
- Web Crawlers
- Search Engine Optimization (SEO)
- Hidden Files and Directories
- Client-Side vs Server-Side Resources
- Directory Enumeration