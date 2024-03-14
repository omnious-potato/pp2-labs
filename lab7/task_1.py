import pygame, datetime, math

pygame.init()
w_width = 1400
w_height = 1050
screen = pygame.display.set_mode((w_width, w_height))

bg = pygame.image.load("yep.bmp")#TODO: Edit bg and clock arms correctly


done = False

center = (w_width/2, w_height/2)

clock = pygame.time.Clock()


print(pygame.colordict)



def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True


        current_time = datetime.datetime.now()

        current_minute = current_time.minute
        current_second = current_time.second

        second_phi = 360.0 *  current_second / 60.0
        print(second_phi)

        screen.blit(bg, (0, 0))
        
        
        rect_long = pygame.Rect(center[0], center[1], 350, 15)
        blitRotateCenter(rect_long)


        pygame.display.flip()
        clock.tick(60)