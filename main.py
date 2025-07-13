"""
Main project file - Car Road Simulation
Simple simulation of a car moving on a straight road with obstacles
"""
import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from car import Car
from road import Road
from obstacle import ObstacleManager
from text_renderer import TextRenderer

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
        pygame.display.set_caption("Car Road Simulation - Avoid the Obstacles!")
        
        # Setup OpenGL
        self.setup_opengl()
        
        # Create game objects
        self.car = Car()
        self.road = Road()
        self.obstacle_manager = ObstacleManager()
        self.text_renderer = TextRenderer()
        
        # Game state
        self.game_state = "menu"  # "menu", "playing", "game_over"
        self.score = 0
        self.game_over_timer = 0
        
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
                elif event.key == pygame.K_SPACE and self.game_state == "menu":
                    self.start_game()
                elif event.key == pygame.K_r and self.game_state == "game_over":
                    self.restart_game()
        return True
    
    def start_game(self):
        """
        Start a new game
        """
        self.game_state = "playing"
        self.score = 0
        self.car = Car()
        self.obstacle_manager.reset()
        
    def restart_game(self):
        """
        Restart the game after game over
        """
        self.start_game()
        
    def update(self):
        """
        Update game state
        """
        if self.game_state == "playing":
            # Get pressed keys state
            keys = pygame.key.get_pressed()
            
            # Update car
            self.car.update(keys)
            
            # Update road
            self.road.update()
            
            # Update obstacles
            self.obstacle_manager.update()
            
            # Check for collision
            if self.obstacle_manager.check_collision(self.car):
                self.game_state = "game_over"
                self.game_over_timer = 0
            
            # Check for score
            points = self.obstacle_manager.check_score(self.car)
            self.score += points
            
        elif self.game_state == "game_over":
            # Update game over timer
            self.game_over_timer += 1
    
    def render(self):
        """
        Render current frame
        """
        # Clear screen
        # glClear: clear color buffer
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Load identity matrix (reset transformations)
        glLoadIdentity()
        
        if self.game_state == "menu":
            # Draw road background
            self.road.draw()
            self.road.draw_buildings()
            
            # Draw car
            self.car.draw()
            
            # Draw menu text
            self.text_renderer.render_instructions()
            
        elif self.game_state == "playing":
            # Draw road and background
            self.road.draw()
            
            # Draw buildings (optional)
            self.road.draw_buildings()
            
            # Draw obstacles
            self.obstacle_manager.draw()
            
            # Draw car
            self.car.draw()
            
            # Draw score
            self.text_renderer.render_score(self.score)
            
        elif self.game_state == "game_over":
            # Draw road and background
            self.road.draw()
            
            # Draw buildings (optional)
            self.road.draw_buildings()
            
            # Draw obstacles
            self.obstacle_manager.draw()
            
            # Draw car
            self.car.draw()
            
            # Draw game over screen
            self.text_renderer.render_game_over(self.score)
        
        # Display frame on screen
        pygame.display.flip()
    
    def run(self):
        """
        Main game loop
        """
        print("=== Car Road Simulation - Obstacle Avoidance ===")
        print("Objective: Avoid the red obstacles!")
        print("Controls:")
        print("- LEFT/RIGHT arrow keys: Move car")
        print("- SPACE: Start game")
        print("- R: Restart after game over")
        print("- ESC: Quit game")
        print("==============================================")
        
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