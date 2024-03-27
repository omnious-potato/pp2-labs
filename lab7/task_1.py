import pygame, datetime, math
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
clock = pygame.time.Clock()

def blitRotateZoomXY(surf, original_image, origin, pivot, angle, scale_x=1, scale_y=1):

    image_rect = original_image.get_rect(topleft = (origin[0] - pivot[0], origin[1]-pivot[1]))
    offset_center_to_pivot = pygame.math.Vector2(origin) - image_rect.center
    offset_center_to_pivot.x *= scale_x
    offset_center_to_pivot.y *= scale_y
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (origin[0] - rotated_offset.x, origin[1] - rotated_offset.y)
    scaled_image = pygame.transform.smoothscale(original_image, (image_rect.width * scale_x, image_rect.height * scale_y))
    rotozoom_image = pygame.transform.rotate(scaled_image, angle)
    rect = rotozoom_image.get_rect(center = rotated_image_center)

    surf.blit(rotozoom_image, rect)



bg = pygame.image.load("images/mickeyclock_decap.png")#background image

minute_hand_img = pygame.image.load('images/minute_hand.png')
minute_hand_img = pygame.transform.rotate(minute_hand_img, 180) #to correspond with measured pivot coordinates we rotate image

hour_hand_img = pygame.image.load('images/hour_hand.png')
hour_hand_img = pygame.transform.rotate(hour_hand_img, 180)

hour_angle, minute_angle = 0, 0

done = False
is_clock_synced = False


while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not is_clock_synced:
        current_time = datetime.datetime.now()

        current_hour = current_time.hour
        current_minute = current_time.minute
        current_second = current_time.second

        #hour_angle = -360.0 *  current_hour/ 60.0
        hour_angle = -180 - 360 * current_hour / 12.0 - 360 * current_minute / 60.0 / 12.0
        print(hour_angle)
        minute_angle = -360.0 *  current_minute / 60.0 - 182

        #possible improvements - sync once, then move with ticktime
        #is_clock_synced = True

    clock_center_pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.blit(bg, (0, 0))

    blitRotateZoomXY(screen, hour_hand_img, clock_center_pos, (70, 23), hour_angle)
    blitRotateZoomXY(screen, minute_hand_img, clock_center_pos, (40, 24), minute_angle)

    pygame.display.flip()


    
pygame.quit()
exit()