# Static Site Generator 🚀

Welcome to my custom-built **Static Site Generator**, developed in Python as part of the [Boot.dev](https://www.boot.dev) curriculum. This project transforms Markdown content into a fully functional, high-performance static website, ready for deployment to the internet.

## 🌟 Features

- **Markdown to HTML Conversion**: Supports a wide range of Markdown syntax:
    - **Block Level**: Headings (h1-h6), Paragraphs, Code Blocks, Blockquotes, Unordered Lists, and Ordered Lists.
    - **Inline Level**: **Bold**, _Italic_, `Code`, [Links](https://google.com), and ![Images](https://images.com).
- **Template System**: Uses a centralized `template.html` for consistent site-wide branding and styling.
- **Recursive Generation**: Automatically crawls the `content/` directory to mirror its structure in the final build.
- **Asset Synchronization**: Recursively copies static assets (images, CSS) from `static/` to the build directory.
- **Path Rewriting**: Configurable `basepath` support for hosting in subdirectories (like GitHub Pages).
- **Local Development**: Built-in shell script to generate the site and start a local HTTP server instantly.

## 🛠️ Tech Stack

- **Language**: Python 3
- **Regex**: For high-speed inline Markdown parsing.
- **HTML/CSS**: For the generated frontend.
- **Shell Scripting**: For automation and local development.

## 📐 Architecture

The generator follows a modular, rule-based approach:

1.  **Node System**:
    *   `HTMLNode`: The base class for representing a nested tree structure of HTML elements.
    *   `LeafNode`: Handles tags with raw values (no children).
    *   `ParentNode`: Manages recursion by nesting other nodes.
    *   `TextNode`: An intermediate representation for inline text types before conversion to HTML.
2.  **Parsing Logic**:
    *   **Block Parser**: Breaks down full Markdown documents into distinct block types using specific syntax rules.
    *   **Inline Parser**: Uses Regular Expressions to extract and split text into sophisticated inline nodes (bold, italic, links, etc.).
3.  **Generation Pipeline**:
    *   Clears the destination directory to ensure a clean build.
    *   Syncs static assets from the `static/` folder.
    *   Crawls the `content/` folder and generates `.html` files for every `.md` file found, injecting them into the `template.html`.

## 🚀 How to Use

### Prerequisites
- Python 3.x installed on your machine.
- Git (optional, for deployment).

### Local Development
To build the site and start a local server at `http://localhost:8888`:
```bash
./main.sh
```

### Production Build
To build the site for a specific subdirectory (e.g., for GitHub Pages):
```bash
./build.sh
```
*Note: This script passes a custom base path to the generator to ensure all internal links work correctly on your hosted domain.*

## 📂 Project Structure

```text
.
├── content/          # Source Markdown files
├── docs/             # Final production build (generated)
├── src/              # Python source code
│   ├── block_markdown.py
│   ├── copystatic.py
│   ├── htmlnode.py
│   ├── main.py
│   └── textnode.py
├── static/           # Static assets (CSS, Images)
├── main.sh           # Dev server script
├── build.sh          # Production build script
└── template.html     # Base HTML structure
```

## 🌐 Deployment

This project is optimized for **GitHub Pages**:
1. Run `./build.sh` to generate the production-ready site in the `docs/` folder.
2. Commit and push your changes to GitHub.
3. In your repo settings under **Pages**, set the source to `main` branch and `/docs` folder.

---
Built with ⌨️ and ❤️ by Moaz Ahmed during the [Build a Static Site Generator](https://www.boot.dev/courses/build-static-site-generator-python) course.
