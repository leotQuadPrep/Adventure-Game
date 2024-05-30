import pygame
from Door import Door
from Inventory import Inventory
from PersonalityTraits import PersonalityTraits
Player_Inventory = Inventory(10)
Compare_Door1 = Door(True, True, "", "", "Compare door 1", "", "", "")
pygame.init()
COLOR_INACTIVE = pygame.Color(100, 100, 100)
COLOR_ACTIVE = pygame.Color(255, 255, 255)
FONT = pygame.font.Font(None, 32)
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
time = 24
article_list = ["a", "the", "an"]
action_list = ["go", "take", "open", "drop", "close", "attack", "bar", "unbar", "lock", "unlock", "pick", "up"]
player_input = ""
player_inputted = False
action_show_text = ""
level_show_text = ""
gameTime = 0
location = ""
location_changed = True
input_char = '''abcdefghijklmnopqrstuvwxyz '''


def remove_article(string_list):
    for i in article_list:
        while i in string_list:
            string_list.remove(i)


def remove_action(string_list):
    for i in action_list:
        while i in string_list:
            string_list.remove(i)


def blit_text(text, pos, color, size):
    if text != "":
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = FONT.size(' ')[0]  # The width of a space.
        x, y = pos
        max_width, max_height = WIDTH-x, HEIGHT
        width = 0
        height = 10
        for line in words:
            for word in line:
                word_surface = FONT.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    if x > width:
                        width = x
                    height = height + word_height
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            if x > width:
                width = x
            height = height + word_height
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
        return width, height
    else:
        return size


def contains(container, containee):
    j_index = 0
    i_index = 0
    for i in container:
        i_index += 1
        j_index = 0
        if i_index != len(container):
            for j in containee:
                j_index += 1
                if j == i:
                    if j_index < len(containee):
                        if containee[j_index] == container[i_index]:
                            return True
                else:
                    break
