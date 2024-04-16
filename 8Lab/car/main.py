# Imports
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
fps = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3  # скорость врага
MONEY = 0  # очко

# Шрифты
font = pygame.font.SysFont("Verdana", 60)  # шрифт гэйм овер
font_small = pygame.font.SysFont("Verdana", 20)  # шрифт коинс
game_over = font.render("Game Over", True, BLACK)  # "Game Over"
coin_font = font_small.render("Coins:", True, BLACK)  # "Coins"

background = pygame.image.load("AnimatedStreet.png") # фоновой рисунок
SCREEN = pygame.display.set_mode((400, 600)) #размер экрана
SCREEN.fill(WHITE) # залив
pygame.display.set_caption("Game") #название экрана

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()  # получения прямоугольника вокруг монеты
        self.rect.center = (
        random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 80))  # рандомные монеты


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()  # получаем прямоугольник вокруг машины врага
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # рандомнные машины врага

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # направление врага
        if (self.rect.top > 600):  # если враг вышел за границы
            SCORE += 1  # прибавляем единницу каждый раз когда враг выходит за границу
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # следующее появление красной машины


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()  # получаем прямоугольник вокруг машины игрока
        self.rect.center = (160, 520)  # позишейн игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()  # массив который хранит в себе каждое изображение красной и синей машины при каждом кадре
all_sprites.add(P1)
all_sprites.add(E1)
COIN = pygame.sprite.Group()
COIN.add(C1)

# новое событие
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждую секунду появляется машина врага

while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # скорость красной машины растет каждый раз при его новой появлении
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(background, (0, 0))  # появление на экране заднего фона
    SCREEN.blit(coin_font, (290, 10))  # появление на экране надписи Coins:
    coins = font_small.render(str(MONEY), True, BLACK)
    SCREEN.blit(coins, (350, 10))
    SCREEN.blit(C1.image, C1.rect)  # появлeние самой монеты и невидимого прямоугольника вокруг него

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image,
                    entity.rect)  # появление красной машины и синей машины и невидимых прямоугольников вокруг них
        entity.move()  # движение красной и синей машины

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('The Weekend-Reminder.mp3').play()
        time.sleep(0.5)

        SCREEN.fill(WHITE)  # экран закрашивается в белый цвет при столкновении двух машин
        SCREEN.blit(game_over, (30, 250))  # появляется надпись Game over!

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # при проигрыше, мы очищаем все данные с нашего якобы массива
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, COIN):
        MONEY += 1  # прибавляется одна монета
        C1.rect.center = (
        random.randint(40, SCREEN_WIDTH - 40), random.randint(100, SCREEN_HEIGHT - 80))  # рандомное появление монет

    pygame.display.update()
    FramePerSec.tick(fps)