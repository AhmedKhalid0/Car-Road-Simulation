"""
Text Renderer file - contains functions for rendering text on screen
"""
import pygame
from OpenGL.GL import *

class TextRenderer:
    def __init__(self):
        """
        Initialize text renderer
        """
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
        
    def render_text(self, text, x, y, color=(1.0, 1.0, 1.0), font_size="normal"):
        """
        Render text at specified position
        text: text to render
        x, y: position on screen (-10 to 10 range)
        color: RGB color tuple (0.0 to 1.0)
        font_size: "normal" or "large"
        """
        # Choose font based on size
        font = self.large_font if font_size == "large" else self.font
        
        # Create text surface
        text_surface = font.render(text, True, 
                                  (int(color[0]*255), int(color[1]*255), int(color[2]*255)))
        
        # Get text dimensions
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        
        # Convert surface to OpenGL texture
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        
        # Generate texture
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        
        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        
        # Upload texture data
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, 
                    GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        
        # Enable texturing
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        
        # Set color to white (texture will provide color)
        glColor3f(1.0, 1.0, 1.0)
        
        # Calculate display size (scale down for game coordinates)
        display_width = text_width * 0.01
        display_height = text_height * 0.01
        
        # Draw textured quad
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex2f(x, y)
        glTexCoord2f(1, 0)
        glVertex2f(x + display_width, y)
        glTexCoord2f(1, 1)
        glVertex2f(x + display_width, y + display_height)
        glTexCoord2f(0, 1)
        glVertex2f(x, y + display_height)
        glEnd()
        
        # Disable texturing
        glDisable(GL_TEXTURE_2D)
        
        # Delete texture
        glDeleteTextures([texture_id])
        
    def render_score(self, score):
        """
        Render score in top-left corner
        """
        score_text = f"Score: {score}"
        self.render_text(score_text, -9, 5, (1.0, 1.0, 1.0), "normal")
        
    def render_game_over(self, score):
        """
        Render game over screen
        """
        # Draw semi-transparent overlay
        glColor4f(0.0, 0.0, 0.0, 0.7)
        glBegin(GL_QUADS)
        glVertex2f(-10, -6)
        glVertex2f(10, -6)
        glVertex2f(10, 6)
        glVertex2f(-10, 6)
        glEnd()
        
        # Render game over text
        self.render_text("GAME OVER", -3, 1, (1.0, 0.2, 0.2), "large")
        self.render_text(f"Final Score: {score}", -2.5, 0, (1.0, 1.0, 1.0), "normal")
        self.render_text("Press R to restart", -2.5, -1, (1.0, 1.0, 0.0), "normal")
        self.render_text("Press ESC to quit", -2.5, -2, (1.0, 1.0, 0.0), "normal")
        
    def render_instructions(self):
        """
        Render game instructions at startup
        """
        self.render_text("Avoid the obstacles!", -2.5, 3, (1.0, 1.0, 1.0), "normal")
        self.render_text("Use LEFT/RIGHT arrows", -2.5, 2, (1.0, 1.0, 0.0), "normal")
        self.render_text("Press SPACE to start", -2.5, 1, (1.0, 1.0, 0.0), "normal") 