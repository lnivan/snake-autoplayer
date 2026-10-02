<div align="center">

# Snake Autoplayer

*A screen-reading bot that plays an 11 × 11 browser Snake by alternating two 120-cell cycles that together cover every cell.*

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![pyKey](https://img.shields.io/badge/pyKey-30363D?style=flat-square)
![Pillow](https://img.shields.io/badge/Pillow-30363D?style=flat-square)
![Status](https://img.shields.io/badge/status-prototype-BF8700?style=flat-square)
![Year](https://img.shields.io/badge/year-2023-8250DF?style=flat-square)

</div>

## About

A bot that plays a browser Snake game on an 11 × 11 board without touching the game's code. It takes screenshots with Pillow, finds the snake and the apple by their exact RGB colours, and sends <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> presses through pyKey. The active strategy ignores the apple: it follows a fixed route through 120 of the 121 cells and switches to a second route every lap, so every cell is reached and the snake cannot hit itself until it is 119 cells long. Breadth-first search versions from earlier attempts are still in the file, unused. Written for Windows and one specific screen layout.

> [!WARNING]
> The bot sends real key presses to whichever window has focus and reads pixels at fixed screen coordinates. It starts pressing keys as soon as it sees the snake's green at the expected spot, and it has no stop key: switch to the terminal and press <kbd>Ctrl</kbd>+<kbd>C</kbd>, or close the terminal. `experiments/serpienteRecursiva/prueba.py` presses <kbd>W</kbd> a thousand times after a 2-second delay.

## Quick start

```bash
python -m pip install -r requirements.txt
python SerpienteAutomatica.py
```

Open the game first, so that its board covers screen pixels (1244, 98) to (1743, 597) on the main monitor.

## How it works

- **Reading the board.** The board is taken to be a 500 × 500 px square with its top-left corner at (1244, 98), so a cell is 500/11 ≈ 45.5 px wide. Cell $(c, r)$, column first and row counted downwards, is sampled around its centre:

  ```math
  (x,\,y) = \Bigl(1244 + \tfrac{500}{22} + c\,\tfrac{500}{11},\;\; 98 + \tfrac{500}{22} + r\,\tfrac{500}{11}\Bigr)
  ```

  A cell holds snake if one of four pixels near the centre is green (109, 255, 24), and the apple if one is red (238, 0, 0).

- **Keeping step with the game.** `avanzar` ("advance") grabs screenshots in a loop until the cell where it believes the head is turns green, which means the game has drawn the last move. It then holds the key for the next cell for 50 ms. The bot keeps its own copy of the body (`cuerpo`) and drops the tail only when the target cell was not red, so the copy grows with each apple. After every step it prints the number of apples eaten.

- **Why two routes.** Colour the cells like a chessboard by the parity of $c + r$. There are 61 even cells and 60 odd ones, and a cycle alternates colours, so no cycle can pass through all 121 cells: the 11 × 11 grid has no Hamiltonian cycle. Leaving out one even corner balances the count, and the bot uses two such 120-cell cycles. Route A skips the bottom-right corner (10, 10) and route B skips the top-right corner (10, 0). Columns 0 to 6 are swept down and up over rows 1 to 10, columns 7 and 8 over rows 2 to 10, columns 9 and 10 are climbed in a zig-zag, and row 0, with a small detour through (8, 1) and (7, 1), is the corridor back to the start at (0, 0). Each arrow shows where the head goes next, and `x` is the skipped cell:

  ```text
          Route A                     Route B
  v < < < < < < < v < <       v < < < < < < < v < x
  v > v > v > v ^ < > ^       v > v > v > v ^ < ^ <
  v ^ v ^ v ^ v > v ^ <       v ^ v ^ v ^ v > v > ^
  v ^ v ^ v ^ v ^ v > ^       v ^ v ^ v ^ v ^ v ^ <
  v ^ v ^ v ^ v ^ v ^ <       v ^ v ^ v ^ v ^ v > ^
  v ^ v ^ v ^ v ^ v > ^       v ^ v ^ v ^ v ^ v ^ <
  v ^ v ^ v ^ v ^ v ^ <       v ^ v ^ v ^ v ^ v > ^
  v ^ v ^ v ^ v ^ v > ^       v ^ v ^ v ^ v ^ v ^ <
  v ^ v ^ v ^ v ^ v ^ <       v ^ v ^ v ^ v ^ v > ^
  v ^ v ^ v ^ v ^ v > ^       v ^ v ^ v ^ v ^ v ^ <
  > ^ > ^ > ^ > ^ > ^ x       > ^ > ^ > ^ > ^ > > ^
  ```

- **Alternating.** One lap of route A followed by one lap of route B is queued whenever the queue runs empty. Each skipped corner is therefore visited every second lap, so an apple anywhere is reached within two laps (240 moves). The two routes differ only in columns 9 and 10. Stepping through the alternation offline shows that a snake of up to 118 cells never runs into its own body.

- **Opening.** The bot assumes the game starts with a three-cell snake in row 5, cells (2, 5) to (4, 5), with its head at (4, 5). A nine-step lead-in goes up column 4 and left along row 0 to (0, 0), where the first lap begins.

- **Unused search code.** `encontrarCamino` ("find path") is a breadth-first search from the head to the apple that treats the body as walls. `encontrarCamino2` lets the tail shorten as the path grows, so after $k$ moves the $k$ body cells nearest the tail no longer block. `encontrarCamino3` falls back to one safe step at a time when the apple is out of reach, and `encontrarManzana` ("find apple") scans the board for red. The active loop calls none of them; the loop that did is commented out.

## Code map

| Path | Role |
| --- | --- |
| `SerpienteAutomatica.py` | The bot: the `Serpiente` ("snake") class, the two hard-coded routes and the main loop |
| `experiments/serpienteRecursiva/serpienteRecursiva.py` | The earlier stage: the first BFS (`pathFinder2DGrid`), older screen calibrations, tick-timing tests at 1/7 s and pixel-reading benchmarks; the active part prints an M/S/N (apple/snake/nothing) map of the board |
| `experiments/serpienteRecursiva/prueba.py` | Times 1,000 presses of <kbd>W</kbd> through pyKey |

## Limitations

- The screen position, cell size and colours are hard-coded for one monitor, browser zoom and game. Any other setup needs new numbers in the source.
- The bot cannot win: the alternating routes are safe only up to 118 cells, three short of a full board. Ignoring the apple also makes it slow, up to two laps per apple.
- The waiting loop grabs screenshots as fast as it can, so it keeps one CPU core busy, and the console prints on every step.
- `encontrarCamino` and `encontrarCamino2` loop forever when no path to the apple exists, and the random fallback in `encontrarManzana` takes its x and y from two different free cells.
- In `serpienteRecursiva.py` the screenshot is taken once, before the loop, so it prints the same map forever.

## Background

Written in or before June 2023; the files come from a code backup made that month and were put under version control in 2026. `experiments/` holds the earlier stage, where the screen calibration went through several values before settling on the one the bot uses.

---

<div align="center"><sub>Part of <a href="https://github.com/lnivan">lnivan's projects</a> · <b>Tools</b></sub></div>
