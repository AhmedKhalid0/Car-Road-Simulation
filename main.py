"""
Main project file - Car Road Simulation
Simple simulation of a car moving on a straight road
"""
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from car import Car
from road import Road

class GameWindow:
    def __init__(self, width=800, height=600):
        """
        Create game window and initialize Pygame and OpenGL
        """
        self.width = width
        self.height = height
        
        # Initialize Pygame
        pygame.init()
        
        # Setup Pygame window with OpenGL support
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Car Road Simulation")
        
        # Setup OpenGL
        self.setup_opengl()
        
        # Create game objects
        self.car = Car()
        self.road = Road()
        
        # Setup clock for frame rate control
        self.clock = pygame.time.Clock()
        
    def setup_opengl(self):
        """
        Initialize OpenGL settings
        """
        # Set viewport
        glViewport(0, 0, self.width, self.height)
        
        # Set projection type (orthographic projection)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        # Set viewing bounds
        # gluOrtho2D: create 2D orthographic projection
        gluOrtho2D(-10, 10, -6, 6)
        
        # Return to modelview mode
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Enable color blending for transparency
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Enable line smoothing
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        
    def handle_events(self):
        """
        Handle events (like key presses or window close)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        """
        Update game state
        """
        # Get pressed keys state
        keys = pygame.key.get_pressed()
        
        # Update car
        self.car.update(keys)
        
        # Update road
        self.road.update()
    
    def render(self):
        """
        Render current frame
        """
        # Clear screen
        # glClear: clear color buffer
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Load identity matrix (reset transformations)
        glLoadIdentity()
        
        # Draw road and background
        self.road.draw()
        
        # Draw buildings (optional)
        self.road.draw_buildings()
        
        # Draw car
        self.car.draw()
        
        # Display frame on screen
        pygame.display.flip()
    
    def run(self):
        """
        Main game loop
        """
        print("=== Car Road Simulation ===")
        print("Use LEFT and RIGHT arrow keys to control the car")
        print("Press ESC or close window to exit")
        print("================================")
        
        running = True
        while running:
            # Handle events
            running = self.handle_events()
            
            # Update game state
            self.update()
            
            # Render frame
            self.render()
            
            # Control frame rate (60 FPS)
            self.clock.tick(60)
        
        # Quit Pygame
        pygame.quit()
        sys.exit()

def main():
    """
    Main function to run the game
    """
    try:
        # Create and run game
        game = GameWindow(800, 600)
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        pygame.quit()
        sys.exit(1)

if __name__ == "__main__":
    main() 