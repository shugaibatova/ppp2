import pygame

import os
pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SPOTIFY')

musics = [os.path.join("C:\\ppp2\\7Lab\\music\\mysoongs", f) for f in os.listdir("C:\\ppp2\\7Lab\\music\\mysoongs") if f.endswith('.mp3')]
current_track = 0
paused = False
pygame.mixer.music.load(musics[current_track])

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(musics)
                pygame.mixer.music.load(musics[current_track])
                pygame.mixer.music.play()
                paused = False

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(musics)
                pygame.mixer.music.load(musics[current_track])
                pygame.mixer.music.play()
                paused = False

            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(musics[current_track])
                pygame.mixer.music.play()
                paused = False

    screen.fill((128,0,255))
    font = pygame.font.SysFont(musics, 30)
    filename = os.path.basename(musics[current_track])
    filename_without_mp3 = os.path.splitext(filename)[0]
    text = font.render(filename_without_mp3, True, (255, 255, 255))
    screen.blit(text, (50, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()