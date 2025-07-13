"""
Road file - contains Road class for drawing road and background
"""
from OpenGL.GL import *

class Road:
    def __init__(self):
        """
        Create a road object
        """
        self.road_width = 6  # road width
        self.line_positions = []  # positions of dashed road lines
        self.line_speed = 0.2  # speed of moving lines to give sense of motion
        
        # Create dashed line positions
        for i in range(8):
            self.line_positions.append(i * 2 - 8)
    
    def update(self):
        """
        Update road line positions to give sense of motion
        """
        # Move lines downward
        for i in range(len(self.line_positions)):
            self.line_positions[i] -= self.line_speed
            
            # If line goes off screen, reset it to top
            if self.line_positions[i] < -10:
                self.line_positions[i] = 8
    
    def draw(self):
        """
        Draw road and background
        """
        # Draw background (blue sky)
        glColor3f(0.5, 0.7, 1.0)  # light blue color for sky
        glBegin(GL_QUADS)
        glVertex2f(-10, -10)
        glVertex2f(10, -10)
        glVertex2f(10, 10)
        glVertex2f(-10, 10)
        glEnd()
        
        # Draw side ground (green grass)
        glColor3f(0.2, 0.8, 0.2)  # green color for grass
        # Left side
        glBegin(GL_QUADS)
        glVertex2f(-10, -10)
        glVertex2f(-self.road_width/2, -10)
        glVertex2f(-self.road_width/2, 10)
        glVertex2f(-10, 10)
        glEnd()
        
        # Right side
        glBegin(GL_QUADS)
        glVertex2f(self.road_width/2, -10)
        glVertex2f(10, -10)
        glVertex2f(10, 10)
        glVertex2f(self.road_width/2, 10)
        glEnd()
        
        # Draw main road (gray)
        glColor3f(0.4, 0.4, 0.4)  # gray color for road
        glBegin(GL_QUADS)
        glVertex2f(-self.road_width/2, -10)
        glVertex2f(self.road_width/2, -10)
        glVertex2f(self.road_width/2, 10)
        glVertex2f(-self.road_width/2, 10)
        glEnd()
        
        # Draw road side lines (white)
        glColor3f(1.0, 1.0, 1.0)  # white color for lines
        glLineWidth(3)  # line thickness
        
        # Left line
        glBegin(GL_LINES)
        glVertex2f(-self.road_width/2, -10)
        glVertex2f(-self.road_width/2, 10)
        glEnd()
        
        # Right line
        glBegin(GL_LINES)
        glVertex2f(self.road_width/2, -10)
        glVertex2f(self.road_width/2, 10)
        glEnd()
        
        # Draw dashed line in middle of road
        glColor3f(1.0, 1.0, 0.0)  # yellow color for dashed line
        glLineWidth(2)
        
        for line_y in self.line_positions:
            glBegin(GL_LINES)
            glVertex2f(0, line_y)
            glVertex2f(0, line_y + 1)
            glEnd()
        
        # Draw trees on sides
        self._draw_trees()
    
    def _draw_trees(self):
        """
        Draw simple trees on road sides
        """
        tree_positions = [
            (-5, 3), (-4, -2), (-6, 0), (-5, -4),
            (5, 2), (4, -1), (6, 1), (5, -3)
        ]
        
        for x, y in tree_positions:
            # Draw tree trunk (brown rectangle)
            glColor3f(0.5, 0.3, 0.1)  # brown color
            glBegin(GL_QUADS)
            glVertex2f(x - 0.1, y - 0.5)
            glVertex2f(x + 0.1, y - 0.5)
            glVertex2f(x + 0.1, y + 0.5)
            glVertex2f(x - 0.1, y + 0.5)
            glEnd()
            
            # Draw tree leaves (green triangle)
            glColor3f(0.1, 0.6, 0.1)  # dark green color
            glBegin(GL_TRIANGLES)
            glVertex2f(x, y + 1.0)      # top point
            glVertex2f(x - 0.5, y + 0.3) # left point
            glVertex2f(x + 0.5, y + 0.3) # right point
            glEnd()
    
    def draw_buildings(self):
        """
        Draw simple buildings in background
        """
        building_positions = [
            (-8, 2, 1.5, 3), (-7, 1, 1, 2), (-6, 0.5, 0.8, 1.5),
            (6, 1.5, 1.2, 2.5), (7, 0.8, 1, 1.8), (8, 2.2, 1.5, 3.2)
        ]
        
        for x, y, width, height in building_positions:
            # Draw building
            glColor3f(0.6, 0.6, 0.7)  # light gray color
            glBegin(GL_QUADS)
            glVertex2f(x - width/2, y)
            glVertex2f(x + width/2, y)
            glVertex2f(x + width/2, y + height)
            glVertex2f(x - width/2, y + height)
            glEnd()
            
            # Draw building windows
            glColor3f(0.8, 0.8, 0.2)  # yellow color for windows
            for i in range(int(height)):
                for j in range(int(width * 2)):
                    window_x = x - width/2 + 0.2 + j * 0.3
                    window_y = y + 0.3 + i * 0.8
                    if window_x < x + width/2 and window_y < y + height:
                        glBegin(GL_QUADS)
                        glVertex2f(window_x, window_y)
                        glVertex2f(window_x + 0.15, window_y)
                        glVertex2f(window_x + 0.15, window_y + 0.2)
                        glVertex2f(window_x, window_y + 0.2)
                        glEnd() 