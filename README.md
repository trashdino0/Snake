<div align="center">
  <img src="https://img.icons8.com/color/96/000000/snake.png" alt="Snake Game Logo" width="96"/>
  <h1>Snake Game</h1>
  <p><strong>A Classic Arcade Snake Game built with Pygame & Turtle</strong></p>

  <p>
    <img src="https://img.shields.io/badge/python-3.8+-blue?logo=python&logoColor=white" alt="Python Version"/>
    <img src="https://img.shields.io/badge/pygame-2.0+-green?logo=pygame" alt="Pygame"/>
    <img src="https://img.shields.io/badge/license-MIT-yellow" alt="License"/>
  </p>
</div>

---

## Overview

A feature-rich Snake game where players navigate a growing snake to collect food while avoiding collisions with their own body. Built with **Pygame** for rendering and **Turtle** for the leaderboard UI. Includes a persistent leaderboard system that tracks the top 5 high scores.

## Features

- **Classic Snake Gameplay** – Navigate using arrow keys, eat food to grow and score points.
- **Customizable Food Count** – Choose how many apples (1–5) spawn at the start of the game.
- **High Score Leaderboard** – Top 5 scores are saved persistently to `leaderboard.txt` and displayed after each game.
- **Player Name Input** – Enter your name before playing; it appears on the leaderboard if you place in the top 5.
- **Game Over Screen** – Displays your final score with instructions to exit.
- **Wrap-Around Movement** – The snake wraps around the screen edges.

## How to Play

1. **Run the game:**
   ```bash
   python snake.py
   ```
2. **Enter your name** when prompted.
3. **Choose the number of apples** (1–5) that will appear on the board.
4. **Control the snake** using the arrow keys:
   - `↑` Move Up
   - `↓` Move Down
   - `←` Move Left
   - `→` Move Right
5. **Eat apples** to grow and increase your score.
6. **Avoid colliding** with your own tail.
7. After the game ends, check the **leaderboard** to see if you made the top 5.
8. Press `X` to exit the game over screen.

## Controls

| Key       | Action     |
|-----------|------------|
| ↑         | Move Up    |
| ↓         | Move Down  |
| ←         | Move Left  |
| →         | Move Right |
| X         | Exit Game  |

## Requirements

- Python 3.8+
- Pygame 2.0+

Install the required dependency:

```bash
pip install pygame
```

## File Structure

```
├── snake.py            # Main game script
├── leaderboard.txt     # Persistent top-5 leaderboard
└── README.md           # This file
```

## Leaderboard

The leaderboard is maintained in `leaderboard.txt` in CSV format (`name,score`). After each game, your score is compared against the stored top 5. If you qualify, your name and score are inserted at the correct rank.

## License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ and Python
</div>
