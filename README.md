# Retro Snake Game

A classic 2D Snake game built in pure Python using `pygame-ce` and packaged as a standalone executable via PyInstaller.

## Features
- Smooth grid movement and self/wall collision detection
- Real-time score counter
- Bundled into a zero-dependency `.exe`

## Controls
- **Arrow Keys:** Move (Up, Down, Left, Right)
- **C:** Play Again (Game Over)
- **Q:** Quit (Game Over)

## Quickstart

```bash
# 1. Install dependencies
python -m pip install pygame-ce pyinstaller

# 2. Run the game
python snake.py

# 3. Build standalone .exe
pyinstaller --onefile --noconsole snake.py
