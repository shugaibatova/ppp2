
import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Setting up FPS
fps = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_width = 400
screen_height = 600
speed = 5  # скорость красной машины
score = 0  # счетчик
money = 0  # монеты

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)  # шрифт для надписи "GAME OVER"
font_small = pygame.font.SysFont("Verdana", 20)  # шрифт для надписи Coins:
game_over = font.render("Game Over", True, BLACK)  # надпись "Game Over"
coin_font = font_small.render("Coins:", True, BLACK)  # надпись Coins:

background = pygame.image.load("images/AnimatedStreet.png")  # загрузка заднего фона

# Create a white screen
SCREEN = pygame.display.set_mode((400, 600))  # установка размеров экрана
SCREEN.fill(WHITE)  # цвет экрана
pygame.display.set_caption("Game")  # заголовок игры


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/coin.png')
        self.rect = self.image.get_rect()  # получения прямоугольника вокруг монеты
        self.rect.center = (
            random.randint(40, screen_width - 40), random.randint(100, screen_height - 80))  # рандомное появление монет


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()  # получаем прямоугольник вокруг красной машины
        self.rect.center = (random.randint(40, screen_width - 40), 0)  # рандомное появление красной машины

    def move(self):
        global score
        self.rect.move_ip(0, speed)  # движение красной машины вниз
        if (self.rect.top > 600):  # если враг вышел за границы
            score += 1  # прибавляем единницу каждый раз когда враг выходит за границу
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)  # следующее появление красной машины


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()  # create rectangle of the same size as the image
        self.rect.center = (160, 520)  # позиция синей машины

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)  # движение вверх
        if self.rect.bottom < screen_height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)  # движение вниз
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # движение влево
        if self.rect.right < screen_width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # движение вправо


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()  # хранит в себе каждое изображение красной и синей машины при каждом кадре
all_sprites.add(P1)
all_sprites.add(E1)
COIN = pygame.sprite.Group()
COIN.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # каждую секунду появляется красная машина

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5  # скорость красной машины растет каждый раз при его новой появлении
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(background, (0, 0))  # появление на экране заднего фона
    scores = font_small.render(str(score), True, BLACK)
    SCREEN.blit(scores, (10, 10))  # появление на экране счетчика

    SCREEN.blit(coin_font, (290, 10))  # появление на экране надписи Coins:
    coins = font_small.render(str(money), True, BLACK)
    SCREEN.blit(coins, (350, 10))
    SCREEN.blit(C1.image, C1.rect)  # появлние самой монеты и невидимого прямоугольника вокруг него

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        SCREEN.blit(entity.image,
                    entity.rect)  # появление красной машины и синей машины и невидимых прямоугольников вокруг них
        entity.move()  # движение красной и синей машины

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('girls.mp3').play()
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
        money += 1  # прибавляется одна монета
        C1.rect.center = (
            random.randint(40, screen_width - 40), random.randint(100, screen_height - 80))  # рандомное появление монет

    pygame.display.update()
    FramePerSec.tick(fps)