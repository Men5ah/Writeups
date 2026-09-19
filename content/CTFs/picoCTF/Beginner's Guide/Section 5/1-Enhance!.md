---
publish: true
---

# Enhance!

Category: #Forensics
Level: #Medium 
Author: #Syreal 
Tags: #svg

---

## Challenge

> Download this image file and find the flag.

## Files

- https://artifacts.picoctf.net/c/100/drawing.flag.svg

## Hints

1. No hints

---

## Initial Observations

It's an SVG file, which opens in a web browser, it can probably be inspected using the DevTools window.

---

## Analysis

First some preliminary research about SVGs. According to Wikipedia,

> [!quote] Scalable Vector Graphics
> **Scalable Vector Graphics** (**SVG**) is an [XML](https://en.wikipedia.org/wiki/XML "XML")-based [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics "Vector graphics") format for defining [two-dimensional](https://en.wikipedia.org/wiki/Plane_\(mathematics\) "Plane (mathematics)") graphics, having support for interactivity and animation.

>[!quote] More Info
>SVG images are defined in a vector graphics format and stored in XML text files. SVG images can thus be [scaled](https://en.wikipedia.org/wiki/Scale_\(ratio\) "Scale (ratio)") in size without loss of quality, and SVG files can be [searched](https://en.wikipedia.org/wiki/Search_algorithm "Search algorithm"), [indexed](https://en.wikipedia.org/wiki/Subject_indexing "Subject indexing"), [scripted](https://en.wikipedia.org/wiki/Scripting_language "Scripting language"), and [compressed](https://en.wikipedia.org/wiki/Data_compression "Data compression"). ==The XML text files can be created and edited with [text editors](https://en.wikipedia.org/wiki/Text_editor "Text editor") or [vector graphics editors](https://en.wikipedia.org/wiki/Vector_graphics_editor "Vector graphics editor"), and are rendered by most [web browsers](https://en.wikipedia.org/wiki/Web_browser "Web browser").== SVG can include [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript"), potentially leading to [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting "Cross-site scripting").

An important line has been highlighted above, that the files can be opened with a text editor and is rendered by most web browsers. This means I can use `cat` to see the code inside of the svg or I can just inspect the code in the browser.

Since SVG is just XML text, the file can be read directly with `cat` or opened in a text editor — no special rendering tool needed to inspect it.

Running `cat drawing.flag.svg` reveals the underlying markup, mostly `<text>` and `<tspan>` elements used to position and style the visible drawing. Skimming through, the flag isn't sitting in one obvious chunk of text — it's broken apart, with individual characters wrapped in their own `<tspan>` tags scattered throughout the file. Visually, in a browser, these render seamlessly as sitting next to each other, but in the raw source, each character is presumably split up and interleaved with the rest of the drawing's other tags.

This is a common way to hide text in plain sight inside an SVG or HTML file: split a string into individual elements so that a simple text search (like `Ctrl+F` for "picoCTF") won't find it, while still letting the rendering engine display it as continuous, readable text.

To recover the flag, I went through each `<tspan>` in document order and pulled out the single character inside, reconstructing the string one character at a time until the full flag emerged.

---

## Solution

### Commands

```bash
cat drawing.flag.svg
```

### Python (if applicable)

```python
pass
```

### Other Tools

- Web browser DevTools (Elements/Inspector panel) 
- `grep` (optional)  to help filter down to just the `<tspan>` lines instead of scrolling through the whole file

---

## Flag

```
picoCTF{3nh4nc3d_aab729dd}
```

---

## Key Takeaways

- SVG files are plain XML text, so basic tools like `cat` or any text editor are often enough for forensic inspection — no special image tools required.
- Text can be intentionally split across multiple elements (e.g., one character per `<tspan>`) to defeat simple text search while still rendering normally to a viewer.
- When a flag "looks" complete visually but isn't findable by searching, check whether the underlying markup fragments the text into smaller pieces.
- Reading raw markup line-by-line, in document order, was enough to manually reconstruct the split string.

---

## References

- https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
- https://developer.mozilla.org/en-US/docs/Web/SVG/Element/tspan

## Related Concepts

- SVG/XML Structure
- Steganography (text-splitting as a lightweight obfuscation technique)
- Browser DevTools Inspection
- Plaintext Forensics
- Data Hiding in Markup Languages