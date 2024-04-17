# Pong Game

This is a simple implementation of the classic Pong game in Python using the Pygame library.

## Requirements

- Python 3.x
- Pygame

You can install the required Python package using pip:

```bash
pip install -r requirements.txt
```

How to Run
To play the game, simply run the pong.py script:

```bash
python pong.py
```

### Game Rules
- Player A uses the W and S keys to move their paddle up and down.
- Player B (the AI) moves its paddle automatically to align with the ball.
- The ball starts at the center of the screen and moves in a random direction.
- If the ball hits a player's edge of the screen, the other player scores a point.
- The scores are displayed at the top corners of the screen.

### Game AI
The AI for Player B uses a simple strategy: it always tries to align its paddle with the ball. This makes the AI unbeatable. To make the game more interesting, you could introduce some randomness or delay in the AI's reactions.

### Future Improvements
- Add a menu to start the game and select difficulty.
- Improve the AI to make the game more challenging.
- Add sound effects and music.
