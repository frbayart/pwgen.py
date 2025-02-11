# SPECS

## 1.0.0

- Initial release

### Features

- [x] read the data from words_alpha.txt
- [x] keep words with 4-8 characters
- [x] select 5 random words
- [x] select a number from 1 to 4 to define X
- [x] on selected 5 words, change X words to uppercase
- [x] generate a random hexa number from 1 to FFFF ensure to have 4 digits
- [x] join the 5 words and the hexa number with dashes, like this: word1-word2-word3-word4-word5-XXXX
- [x] display the result
- [x] add an optional argument to define the number of results to generate, default is 5

### Documentation

This script generates a password by performing the following steps:

1. **Read Words**: It reads words from a file named `words_alpha.txt` and filters them to include only those with 4 to 8 characters.
2. **Select Random Words**: It selects 5 random words from the filtered list.
3. **Change Words to Uppercase**: It randomly selects `X` words (where `X` is a random number between 1 and 4) and changes them to uppercase.
4. **Generate Hexadecimal Number**: It generates a random hexadecimal number between 0001 and FFFF.
5. **Generate Password**: It combines the selected words and the hexadecimal number into a single string, separated by dashes, and prints it.
6. **Multiple Passwords**: The script can generate multiple passwords by specifying the number of passwords as a command-line argument.

### Resources

- [words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt)

