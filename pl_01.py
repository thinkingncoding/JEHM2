import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    pygame.init()
    pygame.display.set_caption("Pygame 사용법")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)

    tmr = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((960,720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2:
                    screen = pygame.display.set_mode((960,720))


        screen.blit(img_galaxy, [0.0])
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__' :
    main()