# Blind Auction

A command-line blind auction program where multiple bidders enter their names and bids without seeing each other's offers. The highest bidder wins.

## How It Works

Each bidder enters their name and bid amount. After each entry, the screen is cleared using the `os` module so the next bidder can't see previous bids. Once all bidders have entered, the program calculates and displays the winner using `max()`.

## Features

- Blind bidding — the terminal clears between entries so bids stay private
- Cross-platform screen clearing (`cls` on Windows, `clear` on Mac/Linux)
- Dictionary-based storage mapping bidder names to their bids
- Automatically determines the highest bidder with `max()`

## Files

| File | Description |
|------|--------------|
| `main.py` | Main program logic |
| `art.py` | ASCII art logo displayed at program start |

## How to Run

1. Make sure `art.py` is in the same folder as `main.py`
2. Run the program:
   ```
   python main.py
   ```
3. Enter each bidder's name and bid when prompted
4. Type `yes` to continue adding bidders, or `no` to end the auction and reveal the winner

## What I Learned

- How to use dictionaries to store key-value pairs (name → bid)
- The `os` module and `os.system()` for running OS-level commands from Python
- Ternary conditional expressions (`value_if_true if condition else value_if_false`)
- Using `os.name` to detect the operating system (`'nt'` for Windows, `'posix'` for Mac/Linux)
- Using `max()` with a `key` argument to find the dictionary entry with the highest value

## Possible Improvements

- Validate bid input to prevent crashes on non-numeric entries
- Validate `yes`/`no` input instead of treating anything other than `"no"` as `"yes"`
- Handle duplicate bidder names so a second entry doesn't overwrite the first
