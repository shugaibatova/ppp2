import pygame
import time
import sys
pygame.init()
size=(800,600)
screen = pygame.display.set_mode((size))
micky=pygame.image.load("body.jpg")
minutes=pygame.image.load("minutes.png")
seconds=pygame.image.load("seconds.png")

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.blit(micky,(0,0))
    now=time.localtime()

    m_angle=360-(now.tm_min * 6)
    m_rotation=pygame.transform.rotate(minutes,m_angle)
    m_position=((size[0]-m_rotation.get_width())/2,(size[1]-m_rotation.get_width())/2)
    screen.blit(m_rotation,m_position)

    s_angle=360-(now.tm_sec * 6)
    s_rotation=pygame.transform.rotate(seconds,s_angle)
    s_position=((size[0]-s_rotation.get_width())/2,(size[1]-s_rotation.get_width())/2)
    screen.blit(s_rotation,s_position)

    pygame.display.flip()

pygame.quit()
sys.exit()


