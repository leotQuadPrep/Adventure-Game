import GlobalContanor
import pygame


class InputBox:
    def __init__(self, x, y, w, h, return_text, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.pos = (x+10, y+5)
        self.size = (w, h)
        self.y = y
        self.x = x
        self.w = w
        self.h = h
        self.color = (100, 100, 100)
        self.text = text
        self.txt_surface = GlobalContanor.FONT.render(text, True, self.color)
        self.active = False
        self.return_text = return_text

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (255, 255, 255) if self.active else (100, 100, 100)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    GlobalContanor.player_input = self.text
                    GlobalContanor.player_inputted = True
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = GlobalContanor.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        # screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        width, height = GlobalContanor.blit_text(self.text, self.pos, self.color, self.size)
        self.w = width
        self.h = height
        # Blit the rect.
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.pos = self.x+10, self.y+5
        pygame.draw.rect(screen, self.color, self.rect, 2)
