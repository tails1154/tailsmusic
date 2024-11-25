
import pygame
import json
import threading
import time


print("TailsMusic Loading...")
# pygame setup
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("TailsMusic")
font = pygame.font.Font(None, 36)
text_surface = font.render("Loading Songs...", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(400, 300))
loadingsongs=True
songs=[]
songcount=-1
nowplaying=""
songplaying=int(0)
paused=False
WHITE=(255, 255, 255)
def music():
    global songs
    global songcount
    global nowplaying
    global paused
    global songplaying


    pygame.mixer.music.load(songs[songplaying])
    pygame.mixer.music.play()
    nowplaying=songs[int(songplaying)]
    while pygame.mixer.music.get_busy():
        1+1
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    songplaying=songplaying+1
    time.sleep(0.1)
    music()
def controls():
    time.sleep(0.1)
    controls()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    paused=False
                    pygame.mixer.music.unpause()
                else:
                    paused=True
                    pygame.mixer.music.pause()
            elif event.key == pygame.K_RIGHT:
                try:
                    if songs[songplaying+1]:
                        pygame.mixer.music.stop()
                except:
                    print("Can't go any further!")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    if loadingsongs:
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        # Open the file in read mode
        with open('music/music.txt', 'rt') as file:
            # Read each line in the file
            for line in file:
                songs.append('music/' + line)
        songs = [song.strip() for song in songs]
        screen.fill("black")

        text_surface=font.render("Creating playlist...", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)
        for item in songs:
            songcount=songcount+1
        nowplaying=songs[0]
        songplaying=0
        pygame.display.flip()

        screen.fill("black")
        thread1=threading.Thread(target=music, daemon=True)
        thread2=threading.Thread(target=controls, daemon=True)
        thread1.start()
        thread2.start()
        loadingsongs=False
    else:
        text_surface=font.render("Now playing: " + nowplaying, True, (255, 255, 255))
        text_rect=text_surface.get_rect(center=(400, 300))
        screen.blit(text_surface, text_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
thread1.exit()
thread2.exit()
pygame.quit()
