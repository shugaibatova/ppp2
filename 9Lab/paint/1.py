import pygame
pygame.init()

w = 800
h = 600
active_size = 0
active_color = 'white'

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

painting = []  # list

active_shape = pygame.draw.circle(screen, 'white', (10, 10), 5)

def draw_menu(size, color):
    pygame.draw.rect(screen, 'gray', (0, 0, w, 70))  # поле инструментов
    pygame.draw.line(screen, 'black', (0, 70), (w, 70), 3)
    xl_brush = pygame.draw.rect(screen, 'black', (10, 10, 50, 50))  # очень большой размер кисти
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', (70, 10, 50, 50))  # большой размер кисти
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', (130, 10, 50, 50))  # средний размер кисти
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', (190, 10, 50, 50))  # маленький размер кисти
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]  # список размеров

    if size == 20:
        pygame.draw.rect(screen, 'green', (10, 10, 50, 50),
                         3)  # зеленый контур
    elif size == 15:
        pygame.draw.rect(screen, 'green', (70, 10, 50, 50), 3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', (130, 10, 50, 50), 3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', (190, 10, 50, 50), 3)

    pygame.draw.circle(screen, color, (650, 35), 30)  # показывает какой цвет мы выбрали
    pygame.draw.circle(screen, 'dark gray', (650, 35), 30, 3)

    rect_rect = pygame.draw.rect(screen, 'white', (400, 10, 60, 50))
    pygame.draw.rect(screen, 'dark gray', (400, 10, 60, 50), 3)
    circle_rect = pygame.draw.circle(screen, 'white', (490, 35), 25)
    pygame.draw.circle(screen, 'dark gray', (490, 35), 25, 3)
    shapes = [rect_rect, circle_rect]

    # все имеющиеся цвета
    blue = pygame.draw.rect(screen, (0, 0, 255), (w - 35, 10, 25, 25))
    red = pygame.draw.rect(screen, (255, 0, 0), (w - 35, 35, 25, 25))
    green = pygame.draw.rect(screen, (0, 255, 0), (w - 60, 10, 25, 25))
    yellow = pygame.draw.rect(screen, (255, 255, 0), (w - 60, 35, 25, 25))
    teal = pygame.draw.rect(screen, (0, 255, 255), (w - 85, 10, 25, 25))
    purple = pygame.draw.rect(screen, (255, 0, 255), (w - 85, 35, 25, 25))
    white = pygame.draw.rect(screen, (0, 0, 0), (w - 110, 10, 25, 25))
    black = pygame.draw.rect(screen, (255, 255, 255), (w - 110, 35, 25, 25))
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 0),
                (255, 255, 255)]  # список где хранится все цвета

    return brush_list, color_rect, rgb_list, shapes
# функция отвечает за рисовку круга
def draw_painting_circle(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
# функция отвечает за рисовку прямоугольника
def draw_painting_rect(paints):
    for i in range(len(paints)):
        pygame.draw.rect(screen, paints[i][0], (paints[i][1][0], paints[i][1][1], paints[i][2] * 2, paints[i][2]))

run = True
while run:
    screen.fill('white')
    mouse = pygame.mouse.get_pos()  # получаем позицию мыши
    left_click = pygame.mouse.get_pressed()[0]  # левая кнопка мыши

    if left_click and mouse[1] > 70:  # чтобы мы не рисовали на поле инструментов
        painting.append((active_color, mouse, active_size))  # передаем текущий цвет, размер, позицию в главный список

    brushes, colors, rgbs, shapes = draw_menu(active_size, active_color)

    if active_shape == shapes[1]:  # если это круг
        draw_painting_circle(painting)  # рисует
    if active_shape == shapes[0]:  # если это прямоугольник
        draw_painting_rect(painting)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):  # если мы выбрали размер
                    active_size = 20 - (i * 5)

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):  # если мы выбрали цвет
                    active_color = rgbs[i]

            for i in range(len(shapes)):
                if shapes[i].collidepoint(event.pos):  # какую фигуру выберем
                    active_shape = shapes[i]

    clock.tick(120)
    pygame.display.update()