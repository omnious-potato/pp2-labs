import pygame, datetime, math, os
from enum import Enum

pygame.init()
w_width = 1280 #px
w_height = 720 #px
screen = pygame.display.set_mode((w_width, w_height))
refresh_rate = 60

done = False

clock = pygame.time.Clock()

bg_color = (26, 0, 8)
button_color = (255,166,77)
white = (255, 255, 255)
red = (255, 0, 0)

x = w_width // 2
y = w_height // 2


cooldown_tracker = 0

class PlayerState:
    NOINIT = -1
    PAUSED = 0
    PLAYING = 1


current_state = PlayerState.NOINIT


_sound_library = dict()
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()

    print(current_state)

    if keys[pygame.K_SPACE]:
        if current_state == PlayerState.NOINIT:
            play_sound("elevator.mp3")
            current_state = PlayerState.PLAYING
        elif current_state == PlayerState.PLAYING:
            pygame.mixer.pause()
            current_state = PlayerState.PAUSED
        else:
            pygame.mixer.unpause()
            current_state = PlayerState.PLAYING

    if keys[pygame.K_RIGHT]:
        #advance track 5 seconds
        pass
    if keys[pygame.K_LEFT]:
        # rewind track 5 seconds
        pass

    screen.fill(bg_color)


    triangle_points = [(0, 0), (50, 25), (0, 50)]
    offset_x = w_width / 2
    offset_y = w_height * 4/5
    pygame.draw.polygon(screen, button_color, [(x + offset_x - 25, y + offset_y) for (x, y) in triangle_points])


    
    offset_x += 50 + 20
    pygame.draw.polygon(screen, button_color, [(x + offset_x - 25, y + offset_y) for (x, y) in triangle_points])
    offset_x += 50
    pygame.draw.polygon(screen, button_color, [(x + offset_x - 25, y + offset_y) for (x, y) in triangle_points])


    pygame.display.flip()
    clock.tick(refresh_rate)