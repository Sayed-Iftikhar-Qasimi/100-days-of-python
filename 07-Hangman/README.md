# Hangman Game 🎮

A command-line Hangman game built in Python, where the player guesses letters to reveal a randomly chosen word before running out of lives.

## How It Works

- A random word is selected from a word list.
- The player guesses one letter at a time.
- Correct guesses reveal the letter's position(s) in the word.
- Incorrect guesses cost a life (6 total) and reveal the next stage of the hangman ASCII art.
- The game ends when the player either guesses the full word (**win**) or runs out of lives (**lose**).

## Features

- Random word selection using the `random` module
- Live tracking of guessed letters and remaining lives
- ASCII art hangman stages that update with each wrong guess
- Prevents repeated wrong guesses from being penalized twice (in progress / improvement area)

## Files

| File               | Purpose                                      |
|--------------------|-----------------------------------------------|
| `main.py`          | Core game logic                              |
| `hangman_words.py` | Contains the list of possible words to guess  |
| `hangman_art.py`   | Contains ASCII art for logo and hangman stages |

## How to Run

```bash
python main.py
```

## What I Learned

- Working with lists and string concatenation to build a dynamic display
- Using `random.choice()` to select from a word list
- Managing game state with boolean flags and loops (`while not game_over`)
- Indexing into a list (`stages[lives]`) to sync visuals with game state
- Debugging logic issues with repeated guesses and life deduction

## Possible Improvements

- Prevent life loss when guessing an already-guessed letter
- Add input validation (e.g., reject non-letter input or multi-character input)
- Track and display all guessed letters (correct + incorrect) separately