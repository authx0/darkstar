# DarkStar Fighter

A simple 2D fighter jet game built with Python and Pygame featuring custom graphics.

## Game Description

In DarkStar Fighter, you control a fighter jet that must destroy incoming enemy missiles while avoiding collisions. The game features:

- Simple controls (up/down arrows to move, spacebar to shoot)
- Enemy missiles that spawn from the right side of the screen
- Custom graphics with fighter jet and missile sprites
- Collision detection between your jet, missiles, and bullets
- Scoring system (10 points per enemy destroyed)
- Game over screen with restart option

## Requirements

- Python 3.x
- Pygame

## Installation

1. Make sure you have Python installed on your system
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```
   python3 game.py
   ```

2. Controls:
   - **Up Arrow:** Move jet up
   - **Down Arrow:** Move jet down
   - **Spacebar:** Shoot bullets
   - **R:** Restart game after game over

## Game Rules

- Destroy enemy missiles by shooting at them to earn 10 points per missile
- Avoid colliding with enemy missiles
- Game ends if your jet collides with an enemy missile

## Assets

The game uses the following image assets:
- `fighter_jet.png` - Player's fighter jet sprite
- `missile.png` - Enemy missile sprite