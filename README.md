# Password Generator with GUI and Export

A simple and user-friendly password generator with a Python GUI.  
Supports password generation, numbering for easy parsing, multi-language interface, master password-based generation, and exporting passwords in Markdown, TXT, JSON, and HTML formats.

---

## Features

- Generate random passwords or passwords based on a master password
- Numbering passwords for easy parsing
- Multi-language support (English, Russian)
- Export password lists to `.md`, `.txt`, `.json`, and `.html` formats
- Choose export file path and name
- Simple and clean GUI built with Tkinter

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/TurboSosiska304/password-generator.git
cd password-generator
Install dependencies (if any):

bash
pip install -r requirements.txt
Tkinter is used and usually comes pre-installed with Python.

Usage
Run the main program:

bash
python main.py
Enter a master password (optional, for generating passwords based on it)

Specify how many passwords to generate

Select the interface language

Generate passwords

Export them to your preferred format and location

Project Structure
main.py — main GUI and logic

generator.py — password generation functions

format.py — exporting passwords in different formats

.gitignore — ignored files list

Planned Improvements
More languages support

Password encryption

Import passwords from files

Enhanced GUI design
