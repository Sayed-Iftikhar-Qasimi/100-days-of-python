🔐 Caesar Cipher

A command-line program built in Python that encodes and decodes messages by shifting each letter along the alphabet.

How It Works
The user chooses to encode or decode a message.
The user enters the message and a shift number.
Each letter's position in the alphabet is shifted forward (encode) or backward (decode) by that amount.
If the shift goes past z or before a, it wraps around to the other end of the alphabet.
Non-letter characters (spaces, punctuation) are left unchanged.
The user can run the program again or quit after each round.
Features
Encoding and decoding using the same core logic (decode just negates the shift)
Wraparound handling using the modulo operator
Repeatable game loop until the user chooses to stop
Files
File	Purpose
main.py	Core cipher logic and program loop
art.py	Contains ASCII art for the logo
How to Run
bash
python main.py
What I Learned
Using list indexing (alphabet.index(), alphabet[position]) to map letters to shifted positions
Using the modulo operator (%) to wrap around the alphabet
Reusing one function for two opposite operations by flipping the sign of a variable
Looping through each character in a string to build a new output string
Managing repeated program execution with a while loop
Possible Improvements
Support uppercase letters (currently everything is lowercased)
Validate that the shift input is a number
Validate that the mode entered is encode or decode
Add a brute-force mode that tries all 26 shifts