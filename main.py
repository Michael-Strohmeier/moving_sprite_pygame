import pygame
from player import Player


# https://stackoverflow.com/questions/35617246/setting-a-fixed-fps-in-pygame-python-3

def main():
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 600
    FPS = 60  # frame rate

    clock = pygame.time.Clock()
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # background = pygame.image.load(os.path.join("assets", "background.png"))
    # background_rect = screen.get_rect()

    player = Player()

    while main:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord("q"):
                    pygame.quit()
                if event.key == ord("w"):
                    player.move()

        # screen.blit(background, background_rect)
        screen.fill((230, 230, 230))

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(FPS)

        player.update(dt)


if __name__ == "__main__":
    main()
