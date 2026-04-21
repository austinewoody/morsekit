# morsekit

A simple Python package for encoding and decoding Morse code.

## Features

- Encode plain text to Morse code
- Decode Morse code to plain text
- Supports letters, digits, and common punctuation
- Includes a command-line interface

## Installation

```bash
pip install morsekit


Usage

from morsekit import encode, decode

print(encode("HELLO WORLD"))
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..

print(decode(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))
# HELLO WORLD


CLI

morsekit encode "HELLO WORLD"
morsekit decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."


License

MIT


---

## 6) `LICENSE`

```text
MIT License

Copyright (c) 2026 Austine Onwubiko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...