import pygame
from level import Level
from gameloop import GameLoop
from eventqueue import EventQueue
from renderer import Renderer
from clock import Clock

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


def menu():
    while True:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH/2 <= mouse[0] <= WIDTH/2+150 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+50:
                    main()

        DISPLAY.fill((0, 0, 0))

        if WIDTH/2 <= mouse[0] <= WIDTH/2+150 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+50:
            pygame.draw.rect(DISPLAY, (170, 170, 170), [
                             WIDTH/2, HEIGHT/2, 150, 50])

        else:
            pygame.draw.rect(DISPLAY, (100, 100, 100), [
                             WIDTH/2, HEIGHT/2, 150, 50])

        font = pygame.font.SysFont("Arial", 36)
        DISPLAY.blit(font.render("New game", True,
                     (255, 255, 255)), (WIDTH/2 + 10, HEIGHT/2 + 10))

        pygame.display.update()


def main():
    pygame.display.set_caption("Pacman")

    clock = Clock()
    level = Level(LEVEL_MAP, CELL_SIZE, clock)
    event_queue = EventQueue()
    renderer = Renderer(DISPLAY, level)
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    game_loop.start()


if __name__ == "__main__":
    menu()
