 # 0x04. UTF-8 Validation

## Description

This directory contains the solution to the "0x04. UTF-8 Validation" project, part of the ALX - SE curriculum. The objective of this project is to implement a function that determines if a given data set represents a valid UTF-8 encoding.

UTF-8 (8-bit Unicode Transformation Format) is a variable-width character encoding used for electronic communication. It can encode all possible characters (code points) in Unicode and is backward-compatible with ASCII. The main goal of this project is to validate if a sequence of bytes is a correctly formatted UTF-8 encoding.

## Project Files

- '0-main.py': This script tests the validUTF8 function with predefined test cases.
- '0-validate_utf8.py': This module contains the validUTF8 function, which checks if a data set represents a valid UTF-8 encoding.
- 'README.md': This file provides an overview of the project, explaining its purpose, usage, and structure.

## Function Details

'validUTF8(data)'

Parameters:

- data (list of int): A list of integers representing the data bytes to be validated.

Returns:

- bool: Returns True if the data set represents a valid UTF-8 encoding, otherwise returns False.

Description:

The function 'validUTF8' iterates through the data list and checks if the bytes form valid UTF-8 characters. It verifies the following conditions:

1. Each byte must adhere to the rules of UTF-8 encoding:
- 1-byte character: 0xxxxxxx
- 2-byte character: 110xxxxx 10xxxxxx
- 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
- 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
2. The function ensures that the initial byte of a multi-byte character is followed by the correct number of continuation bytes.

## Usage

To test the function, run the '0-main.py' script:
 
       python3 0-main.py

This script will execute the validUTF8 function with predefined test cases and output the results.

## Example

         from 0-validate_utf8 import validUTF8

         data = [197, 130, 1]
         print(validUTF8(data))  # Output: True

         data = [235, 140, 4]
         print(validUTF8(data))  # Output: False

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Authors

- Your Name

