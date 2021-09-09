import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def main():
    pygame.init()
    pygame.display.set_caption("test")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)

        key = pygame.key.get_pressed()
        txt1 = font.render("UP{}  DOWN{}".format(key[pygame.K_UP], key[pygame.K_DOWN]), True, WHITE,GREEN)
        screen.blit(txt1,[200, 100])

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
