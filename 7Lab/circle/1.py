import pygame
import sys


pygame.init()


width = 800
height = 600

r = 25
d = r * 2

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")


ball_x = (width - d) // 2
ball_y = (height - d) // 2

done = True
while done:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), r)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(0, ball_y - 20)
            elif event.key == pygame.K_DOWN:
                ball_y = min(height - d, ball_y + 20)
            elif event.key == pygame.K_LEFT:
                ball_x = max(0, ball_x - 20)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(width - d, ball_x + 20)

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        done = False

    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
