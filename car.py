"""
Car file - contains Car class for drawing and updating car position
"""
import math
from OpenGL.GL import *

class Car:
    def __init__(self, x=0, y=-3, width=1.5, height=0.8):
        """
        Create a car object
        x, y: car position in 3D space
        width, height: car width and height
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0.1  # car movement speed
        self.wheel_radius = 0.2  # wheel radius
        
    def update(self, keys):
        """
        Update car position based on pressed keys
        """
        import pygame
        
        # Move right and left using keyboard arrows
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            
        # Prevent car from going outside screen boundaries
        if self.x < -4:
            self.x = -4
        if self.x > 4:
            self.x = 4
    
    def draw(self):
        """
        Draw the car using OpenGL
        """
        # Save current matrix state
        glPushMatrix()
        
        # Move coordinate system to car position
        # glTranslate: moves all subsequent drawings to the specified location
        glTranslatef(self.x, self.y, 0)
        
        # Draw car body (blue rectangle)
        glColor3f(0.2, 0.4, 0.8)  # blue color for car
        glBegin(GL_QUADS)  # start drawing quadrilateral
        glVertex2f(-self.width/2, -self.height/2)  # bottom left point
        glVertex2f(self.width/2, -self.height/2)   # bottom right point
        glVertex2f(self.width/2, self.height/2)    # top right point
        glVertex2f(-self.width/2, self.height/2)   # top left point
        glEnd()  # end drawing polygon
        
        # Draw car window (small white rectangle)
        glColor3f(0.8, 0.9, 1.0)  # bluish white color for window
        glBegin(GL_QUADS)
        glVertex2f(-self.width/3, -self.height/4)
        glVertex2f(self.width/3, -self.height/4)
        glVertex2f(self.width/3, self.height/4)
        glVertex2f(-self.width/3, self.height/4)
        glEnd()
        
        # Draw left wheel
        self._draw_wheel(-self.width/2.5, -self.height/2 - 0.1)
        
        # Draw right wheel
        self._draw_wheel(self.width/2.5, -self.height/2 - 0.1)
        
        # Restore previous matrix state
        glPopMatrix()
    
    def _draw_wheel(self, x, y):
        """
        Draw a single wheel at the specified position
        """
        glColor3f(0.1, 0.1, 0.1)  # black color for wheel
        glBegin(GL_TRIANGLE_FAN)  # use triangles to draw circle
        glVertex2f(x, y)  # center point
        
        # Draw circle using points around the circumference
        for i in range(21):  # 20 triangles + center point = circle
            angle = 2 * math.pi * i / 20
            glVertex2f(x + self.wheel_radius * math.cos(angle), 
                      y + self.wheel_radius * math.sin(angle))
        glEnd()
        
        # Add wheel rim
        glColor3f(0.3, 0.3, 0.3)  # gray color for rim
        glBegin(GL_LINE_LOOP)
        for i in range(20):
            angle = 2 * math.pi * i / 20
            glVertex2f(x + self.wheel_radius * math.cos(angle), 
                      y + self.wheel_radius * math.sin(angle))
        glEnd() 