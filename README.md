# Password Generator

This project is a simple password generator that creates a password by selecting random words and a hexadecimal number, then combining them into a single string. The password is designed to be both memorable and secure.

## Features

- Reads words from a file (`words_alpha.txt`).
- Filters words to include only those with 4 to 8 characters.
- Selects 5 random words from the filtered list.
- Randomly selects a number `X` (between 1 and 4) and changes `X` words to uppercase.
- Generates a random hexadecimal number between 0001 and FFFF.
- Combines the selected words and the hexadecimal number into a single string, separated by dashes.
- Displays the generated password.

## Language Used

- **Python**: The script is written in Python, a versatile and widely-used programming language known for its readability and ease of use.

## How It Was Created

### Tools

- **Python 3.x**: The script is developed using Python 3.x, which provides the necessary libraries and functions for random selection and file handling.
- **Cursor Composer**: Used as the text editor/IDE to write and edit the Python script.

### Prompt

The project was created based on a set of specifications provided in a markdown file (`SPECS.md`). The specifications outlined the requirements for the password generator, including the steps for reading words, selecting random words, changing words to uppercase, generating a hexadecimal number, and displaying the result. The script was generated with the assistance of AI.

### Steps

- **Step 1**: Defined the project specifications and outlined the features in `SPECS.md`.
- **Step 2**: Developed the initial version of the Python script (`pwgen.py`) to implement the specified features.
- **Step 3**: Tested the script, made necessary adjustments, and completed the documentation in `SPECS.md`.
- **Step 4**: Created the `README.md` file to provide an overview of the project, including the language used, tools, and creation process.

## Resources

- [words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt): A comprehensive list of English words used for generating the password.

## Usage

To use the password generator, ensure you have Python 3.x installed and the `words_alpha.txt` file available in the same directory as the script. Run the script using one of the following commands:

```bash
$ pwgen.py -h
usage: pwgen.py [-h] [count]

Generate random passwords.

positional arguments:
  count       Number of passwords to generate

options:
  -h, --help  show this help message and exit
  
$ python3.12 pwgen.py

SHITTING-empiry-TENSES-dashy-BIFIDITY-1629
nelumbos-sparidae-CREDAL-nigher-ebriety-A016
THIMBLED-JOCOQUE-SAUSAGES-enwisen-DODGES-41B7
SCOURING-amyclas-BARDILY-exaudi-MYSOST-CBAD
gamasid-lowrie-lukan-ORIBI-cunner-44E4
```

To generate a specific number of passwords, use:

```bash
$ python3.12 pwgen.py 2

blanche-CHARITES-vocate-peastick-SINAEAN-CE7D
CHABER-gweduck-ANYPLACE-BREED-boti-37F8
```

### Example Output

When you run the script, you might see an output like this:

```
aker-AUNTLY-spinout-doctress-actifier-C676
```

The script will output a randomly generated password based on the specifications.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.
