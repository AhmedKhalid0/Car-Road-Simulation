"""
Obstacle file - contains Obstacle class for managing obstacles in the game
"""
import random
import math
from OpenGL.GL import *

class Obstacle:
    def __init__(self, x, y, width=0.8, height=0.8):
        """
        Create an obstacle object
        x, y: obstacle position in 3D space
        width, height: obstacle width and height
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0.15  # obstacle movement speed (moving downward)
        self.scored = False  # flag to track if this obstacle was already scored
        
    def update(self):
        """
        Update obstacle position - move downward
        """
        self.y -= self.speed
        
    def draw(self):
        """
        Draw the obstacle using OpenGL
        """
        # Save current matrix state
        glPushMatrix()
        
        # Move coordinate system to obstacle position
        glTranslatef(self.x, self.y, 0)
        
        # Draw obstacle main body (red rectangle)
        glColor3f(0.8, 0.2, 0.2)  # red color for obstacle
        glBegin(GL_QUADS)
        glVertex2f(-self.width/2, -self.height/2)  # bottom left
        glVertex2f(self.width/2, -self.height/2)   # bottom right
        glVertex2f(self.width/2, self.height/2)    # top right
        glVertex2f(-self.width/2, self.height/2)   # top left
        glEnd()
        
        # Draw obstacle border (black outline)
        glColor3f(0.0, 0.0, 0.0)  # black color for border
        glLineWidth(2)
        glBegin(GL_LINE_LOOP)
        glVertex2f(-self.width/2, -self.height/2)
        glVertex2f(self.width/2, -self.height/2)
        glVertex2f(self.width/2, self.height/2)
        glVertex2f(-self.width/2, self.height/2)
        glEnd()
        
        # Draw warning stripes on obstacle
        glColor3f(1.0, 1.0, 0.0)  # yellow color for stripes
        glLineWidth(1)
        for i in range(3):
            stripe_y = -self.height/2 + (i + 1) * self.height/4
            glBegin(GL_LINES)
            glVertex2f(-self.width/2 + 0.1, stripe_y)
            glVertex2f(self.width/2 - 0.1, stripe_y)
            glEnd()
        
        # Restore previous matrix state
        glPopMatrix()
    
    def is_off_screen(self):
        """
        Check if obstacle is off screen (below the visible area)
        """
        return self.y < -6
    
    def get_bounds(self):
        """
        Get obstacle bounds for collision detection
        Returns: (left, right, top, bottom)
        """
        left = self.x - self.width/2
        right = self.x + self.width/2
        top = self.y + self.height/2
        bottom = self.y - self.height/2
        return left, right, top, bottom

class ObstacleManager:
    def __init__(self):
        """
        Create obstacle manager to handle multiple obstacles
        """
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_interval = 120  # spawn obstacle every 2 seconds (120 frames at 60 FPS)
        self.road_width = 6  # same as road width
        
    def update(self):
        """
        Update all obstacles and spawn new ones
        """
        # Update spawn timer
        self.spawn_timer += 1
        
        # Spawn new obstacle if it's time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_obstacle()
            self.spawn_timer = 0
        
        # Update all obstacles
        for obstacle in self.obstacles:
            obstacle.update()
        
        # Remove obstacles that are off screen
        self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen()]
    
    def spawn_obstacle(self):
        """
        Spawn a new obstacle at random position on the road
        """
        # Random x position within road bounds
        road_left = -self.road_width/2 + 0.5
        road_right = self.road_width/2 - 0.5
        x = random.uniform(road_left, road_right)
        
        # Start from top of screen
        y = 6
        
        # Create new obstacle
        obstacle = Obstacle(x, y)
        self.obstacles.append(obstacle)
    
    def draw(self):
        """
        Draw all obstacles
        """
        for obstacle in self.obstacles:
            obstacle.draw()
    
    def check_collision(self, car):
        """
        Check collision between car and any obstacle
        Returns: True if collision detected, False otherwise
        """
        # Get car bounds
        car_left = car.x - car.width/2
        car_right = car.x + car.width/2
        car_top = car.y + car.height/2
        car_bottom = car.y - car.height/2
        
        for obstacle in self.obstacles:
            # Get obstacle bounds
            obs_left, obs_right, obs_top, obs_bottom = obstacle.get_bounds()
            
            # Check if rectangles overlap
            if (car_left < obs_right and car_right > obs_left and
                car_top > obs_bottom and car_bottom < obs_top):
                return True
        
        return False
    
    def check_score(self, car):
        """
        Check if car has passed any obstacles and award points
        Returns: number of points scored
        """
        points = 0
        
        for obstacle in self.obstacles:
            # If obstacle is below the car and hasn't been scored yet
            if (obstacle.y + obstacle.height/2 < car.y - car.height/2 and 
                not obstacle.scored):
                obstacle.scored = True
                points += 1
        
        return points
    
    def reset(self):
        """
        Reset obstacle manager (clear all obstacles)
        """
        self.obstacles = []
        self.spawn_timer = 0 