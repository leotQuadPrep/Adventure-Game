import GlobalContanor
import pygame


class DisplayBox:
    def __init__(self, x, y, w, h, text, r, g, b):
        self.rect = pygame.Rect(x, y, w, h)
        self.pos = (x+10, y+5)
        self.size = (w, h)
        self.y = y
        self.x = x
        self.w = w
        self.h = h
        self.color = (r, g, b)
        self.text = text
        self.txt_surface = GlobalContanor.FONT.render(text, True, self.color)

    def update(self, new_text):
        # Resize the box if the text is too long.
        self.text = new_text
        self.txt_surface = GlobalContanor.FONT.render(self.text, True, self.color)
        #width = max(200, self.txt_surface.get_width()+10)
        #self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        width, height = GlobalContanor.blit_text(self.text, self.pos, self.color, self.size)
        self.w = width
        self.h = height
        # Blit the rect.
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.pos = self.x+10, self.y+5
        pygame.draw.rect(screen, self.color, self.rect, 2)
