# PyPassword Generator 🔐

A command-line tool that generates a random, customizable password based on user-specified counts of letters, symbols, and numbers.

## How It Works

- The user specifies how many letters, symbols, and numbers they want in their password.
- The program randomly selects characters from predefined pools for each category.
- All selected characters are combined into one list, then shuffled to avoid predictable patterns (e.g., all letters first, then symbols, then numbers).
- The final password is printed character by character.

## Features

- Customizable password length via separate counts for letters, symbols, and numbers
- Uses `random.choice()` to pick random characters from each pool
- Uses `random.shuffle()` to randomize the order of the final password
- Includes both uppercase and lowercase letters for stronger passwords

## Files

| File      | Purpose                  |
|-----------|---------------------------|
| `main.py` | Core password generator logic |

## How to Run

```bash
python main.py
```

You'll be prompted to enter:
1. Number of letters
2. Number of symbols
3. Number of numbers

