# Car Road Simulation

A simple project to simulate a car moving on a straight road using Python, PyOpenGL, and Pygame.

## Project Description

This project is a simple simulation of a car moving on a straight road. Users can control the car using keyboard arrow keys (left and right only). The project uses:

- **Python**: Main programming language
- **PyOpenGL**: For 3D graphics rendering
- **Pygame**: For window management and events

## Features

- ✅ Simple controllable car
- ✅ Road with moving lines
- ✅ Background with trees and buildings
- ✅ Easy arrow key controls
- ✅ Simple and smooth graphics

## Project Structure

```
Car Road Simulation/
├── main.py          # Main project file
├── car.py           # Car class
├── road.py          # Road and background class
├── requirements.txt # Required libraries
├── README.md        # This file
└── assets/          # Folder for images and resources
```

## Installation and Running

### 1. Ensure Python is Installed

Make sure you have Python 3.7 or newer installed on your system.

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

Or you can install libraries manually:

```bash
pip install pygame PyOpenGL numpy
```

### 3. Run the Project

```bash
python main.py
```

## Game Controls

- **Right Arrow**: Move car right
- **Left Arrow**: Move car left
- **ESC**: Exit game
- **Close Window**: Exit game

## Code Explanation

### Main File (main.py)

- **GameWindow**: Main class that manages window and main loop
- **setup_opengl()**: Initialize OpenGL settings
- **handle_events()**: Handle keyboard events
- **update()**: Update game state
- **render()**: Render current frame

### Car Class (car.py)

- **Car**: Car class with movement and drawing functions
- **update()**: Update car position based on keys
- **draw()**: Draw car and wheels

### Road Class (road.py)

- **Road**: Road and background class
- **update()**: Update moving lines
- **draw()**: Draw road, background, and trees
- **draw_buildings()**: Draw buildings

## Concepts Used

### OpenGL Functions

- `glTranslatef()`: Move coordinate system
- `glColor3f()`: Set drawing color
- `glBegin()` and `glEnd()`: Start and end shape drawing
- `glVertex2f()`: Specify point in 2D space
- `glPushMatrix()` and `glPopMatrix()`: Save and restore matrix state

### Pygame Functions

- `pygame.init()`: Initialize Pygame
- `pygame.display.set_mode()`: Create display window
- `pygame.key.get_pressed()`: Get key states
- `pygame.time.Clock()`: Control frame rate

## Future Enhancements

The project can be developed by adding:

- Road obstacles
- Other cars
- Scoring system
- Sound effects
- Graphics improvements
- Multiple car options

## Requirements

- Python 3.7+
- pygame 2.5.2+
- PyOpenGL 3.1.7+
- numpy 1.24.3+

## Common Errors

### PyOpenGL Installation Error

If you encounter problems installing PyOpenGL, try:

```bash
pip install PyOpenGL-accelerate
```

### Pygame Runtime Error

Make sure SDL is installed on your system.

## Author

This project was created as an educational example for using PyOpenGL with Pygame in computer graphics.

---

**Note**: This project is intended for educational purposes and can be developed and improved as needed. 