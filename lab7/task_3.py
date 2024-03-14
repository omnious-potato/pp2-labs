import pygame, datetime, math

pygame.init()
w_width = 1280 #px
w_height = 720 #px
screen = pygame.display.set_mode((w_width, w_height))
refresh_rate = 60
ball_step = 20 #px
step_cooldown = 50 # in milliseconds
ball_radius = 25 #px



done = False

center = (w_width/2, w_height/2)

clock = pygame.time.Clock()

print(pygame.colordict)

white = (255, 255, 255)
red = (255, 0, 0)

x = w_width // 2
y = w_height // 2


cooldown_tracker = 0


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        keys = pygame.key.get_pressed()

        
        cooldown_tracker += clock.get_time()
        if(cooldown_tracker > step_cooldown):
              cooldown_tracker = 0


        v_x, v_y = 0, 0
        
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and cooldown_tracker == 0:
            v_x += 1
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and cooldown_tracker == 0:
            v_x -= 1
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and cooldown_tracker == 0:
            v_y -= 1
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and cooldown_tracker == 0:
            v_y += 1

        # # Normalising components
        # v_length = math.sqrt(v_x**2 + v_y**2)
        # if(v_length != 0):
        #     v_x = v_x / v_length 
        #     v_y = v_y / v_length
        # if(cooldown_tracker == 0):
        #     print(v_x, v_y)

        new_x = x + v_x * ball_step
        new_y = y + v_y * ball_step
        
              
        x = max(ball_radius, min(new_x, w_width - ball_radius))
        y = max(ball_radius, min(new_y, w_height - ball_radius))
        
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, red, (x, y), ball_radius)

        pygame.display.flip()
        clock.tick(refresh_rate)