import pygame
import pygame_menu
from pygame_menu import themes
from level import Level
from gameloop import GameLoop
from eventqueue import EventQueue
from renderer import Renderer
from clock import Clock
from initialize_database import initialize_database
from database_connection import get_database_connection

initialize_database()
connection = get_database_connection()

LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 7, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 1, 4, 4, 4, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 4, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
             [1, 7, 0, 0, 0, 0, 2, 0, 0, 0, 0, 7, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

CELL_SIZE = 50

HEIGHT = len(LEVEL_MAP)
WIDTH = len(LEVEL_MAP[0])
DISPLAY_HEIGHT = HEIGHT * CELL_SIZE
DISPLAY_WIDTH = WIDTH * CELL_SIZE

DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.init()
pygame.display.set_caption("Main menu")

def main():
    pygame.display.set_caption("Pacman")
    
    clock = Clock()
    level = Level(LEVEL_MAP, CELL_SIZE, clock)
    event_queue = EventQueue()
    renderer = Renderer(DISPLAY, level)
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE, player_name.get_value())
    game_loop.start()

def start_the_game():
    main()

def score_menu():
    mainmenu._open(scores)
    get_scores()

def get_scores():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC;")
    rows = cursor.fetchall()

    o = 1
    for i in rows:
        if o == 11:
            break
        score_text = f"{o}. {i['player']} | Score: {i['score']} | Date: {i['date']}\n"
        scores.add.label(score_text, max_char=-1, font_size=20)
        o += 1

mainmenu = pygame_menu.Menu("Pacman", DISPLAY_WIDTH, DISPLAY_HEIGHT, theme=themes.THEME_ORANGE)
player_name = mainmenu.add.text_input("Your name: ", default="username", maxchar=14)
mainmenu.add.button("Play", start_the_game)
mainmenu.add.button("Scoreboard", score_menu)
mainmenu.add.button("Quit", pygame_menu.events.EXIT)

scores = pygame_menu.Menu("High scores", DISPLAY_WIDTH, DISPLAY_HEIGHT, theme=themes.THEME_BLUE)


mainmenu.mainloop(DISPLAY)
