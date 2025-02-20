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
```

### Arguments
- -w / --words
Required: The characters to use for password generation.
Example: "01234" or "abcdefg".

- -r / --repeat
Required: The length of the generated password.
Example: 2 for generating 2-character passwords.

- -o / --output
Required: The output file where the generated passwords will be saved.
Example: 1.txt.

### Example
To generate a dictionary of all 2-character passwords using the characters "01234" and save it to 1.txt, run:
```bash
python your_script.py -w "01234" -r 2 -o 1.txt
```
This will create the following passwords:
```
00
01
02
03
04
10
11
12
13
14
20
21
22
23
24
30
31
32
33
34
40
41
42
43
44
```
The passwords will be saved to the 1.txt file.

example:
![屏幕截图(833)](https://github.com/user-attachments/assets/5c4eda4f-d7bb-4284-811c-b0067e93acaf)


### Help
For more information on how to use the script, run:
```bash
python your_script.py -h
```
This will display a description of the available arguments and their usage.
example:
![屏幕截图(831)](https://github.com/user-attachments/assets/0d5bc334-81d4-44d3-8345-c756631a900f)

