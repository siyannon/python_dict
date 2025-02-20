# Password Dictionary Generator

This script generates a password dictionary based on the specified character set, password length, and output file. It utilizes `itertools.product` to generate all possible combinations of the given characters.

## Features

- Generate password combinations using a custom character set.
- Specify the password length.
- Output the generated passwords to a specified file.

## Requirements

- Python 3.x
- `argparse` (This module is part of Python's standard library, so no installation is needed.)

## Usage

### Command-line Arguments

To use the script, you can run the following command in the terminal:

```bash
python your_script.py -w "01234" -r 2 -o 1.txt


