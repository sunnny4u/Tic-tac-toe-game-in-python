# Tic Tac Toe (Python, Terminal)

A two-player tic tac toe game that runs in the command line. I wrote it early on while learning Python, mainly to practice loops, functions, lists and handling user input.

## How it works

Both players enter their names at the start. Player 1 plays `X` and goes first, Player 2 plays `O`. The board is numbered like a phone keypad, and on your turn you type the number of the spot you want:

```
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

The board is printed again after every move. If you pick a spot that's already taken, the game tells you and asks again. After each move the game checks all eight winning lines (three rows, three columns, two diagonals). The first player to complete a line wins. If all nine spots fill up with no winner, it's a tie.

## Running it

You need Python 3.6 or newer (the code uses f-strings). No external packages.

```bash
git clone <repository-url>
cd <repository-folder>
python tic_tac_toe.py
```

## Example

```
Welcome to sunny's tic tac toe game.!!
Enter player 1 name: Alice
Enter player 2 name: Bob
...
Alice: 5

     |   |
  ---|---|---
     | X |
  ---|---|---
     |   |
```

## Known limitations

This was one of my first Python projects, and I've left the code as it was to show where I started. Looking back at it now, these are the problems I'd fix:

- Typing something that isn't a number (like `a`) crashes the game with a `ValueError`, because the input goes straight into `int()` without a `try/except`.
- Typing `10` crashes it with an `IndexError`. The range check is `0 <= x < 10` after subtracting 1, so it should be `< 9`.
- The win check is one long chain of `or` conditions, written out once for `X` and again for `O`. A list of the eight winning lines and a loop would be shorter and easier to read.
- The board and the list of used spots are global variables, so the game can't be restarted without rerunning the script.
- The on-screen instructions say all 9 spots must be filled to get a result, but the game actually ends as soon as someone wins.
- The game exits with `quit()` from inside the result check instead of returning control to the main loop.

## Possible improvements

- Validate input properly and re-prompt on bad values
- Rewrite the win check using a list of winning combinations
- Wrap the game state in a class or pass it between functions instead of using globals
- Add a "play again" option
- Add a simple computer opponent (random moves first, then minimax)
- Add unit tests for the win and tie logic

