import pygame
import random

pygame.init()
snake_color = (128, 0, 128)
back_color = (128, 128, 128)
tamaq = (255, 255, 0)
score_coun = (255, 0, 0)

# Screen size
width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 15

font_go = pygame.font.SysFont('bold', 50)  # надпись гэм овер
font_score = pygame.font.SysFont('bold', 50)  # очко
font_l = pygame.font.SysFont('bold', 25)


def print_score(score):
    text = font_score.render("score: " + str(score), True, tamaq)
    screen.blit(text, (0, 0))


def print_level(level_snake):
    level = font_l.render("level: " + str(level_snake), True, tamaq)
    screen.blit(level, (200, 0))


def draw_snake(snake_size, snake_pixels):  # snake_pixels is list with coordinates of every square
    for pixels in snake_pixels:  # x         # y
        pygame.draw.rect(screen, snake_color, (pixels[0], pixels[1], snake_size, snake_size))


def run_game():
    game_over = False  # when game is ended
    game_close = False  # when round is losed

    x = width / 2  # start position
    y = height / 2

    x_speed = 0  # change of coordinates while moving
    y_speed = 0

    snake_pixels = []
    snake_length = 1  # one block of snake

    food_x = round(random.randrange(0, width - snake_size) / 10) * 10
    food_y = round(random.randrange(0, height - snake_size) / 10) * 10

    count = 0  # количество съеденных фруктов
    level_snake = 0  # уровень

    snake_speed = 10

    while not game_over:
        while game_close:  # if round is losed
            screen.fill(back_color)
            game_over_message = font_go.render("Game Over!", True, score_coun)
            screen.blit(game_over_message, (width / 3, height / 3))
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # when key is pressed

                # change coordinates while moving
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        # if we hit boundary, then round is losed
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # change the position of snake
        x += x_speed
        y += y_speed

        screen.fill(back_color)  # background of screen
        pygame.draw.rect(screen, tamaq, (food_x, food_y, snake_size, snake_size))  # тамак

        snake_pixels.append((x, y))

        if len(snake_pixels) > snake_length:  #
            del snake_pixels[0]

        # когда змея коснется самого себя, то игра проиграна
        for pixel in snake_pixels[:-1]:
            if pixel == (x, y):
                game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)
        print_level(level_snake)

        if count == 3:  # съедая по 3 фрукта уровень растет на одну ступень
            level_snake += 1
            # print_level(level_snake)
            snake_speed += 2  # также растет скорость змеи с ростом уровня
            count = 0  # устанавливаем обратно исходное значение

        pygame.display.update()

        if x == food_x and y == food_y:  # если змея кушает фрукт
            food_x = round(
                random.randrange(0, width - snake_size) / 10) * 10  # только в этом случае появляется новый фрукт
            food_y = round(random.randrange(0, height - snake_size) / 10) * 10
            snake_length += 1  # длина змеи растет на один блок
            count += 1

        clock.tick(snake_speed)  # frequency of cycle
    pygame.quit()
run_game()