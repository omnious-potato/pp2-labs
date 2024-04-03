import pygame, random, time, sys

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("./images/AnimatedStreet.png")



def draw_polygon_alpha(surface, color, points): #this function allows to draw polygons with RGBA format
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)

#loading fonts
pygame.font.init()
font = pygame.font.SysFont("cantarell", 54)
font_smaller = pygame.font.SysFont("cantarell", 24)

game_over = font.render("Game Over", True, colorBLACK)
over_rect = game_over.get_rect(center=(WIDTH//2, HEIGHT//2))

score = font_smaller.render("Score:", True, colorBLACK)
score_rect = score.get_rect(topright = (WIDTH - 40, 0))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

        self.coin_score = 0 #stores coin score

    def move(self):
        pressed = pygame.key.get_pressed()
        
        #left-right movement
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)
    

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (35 + int((WIDTH - 60) * random.random()), 5)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT + 100:
            self.rect.move_ip(0, 5)
        else:
            self.rect.center = (35 + int((WIDTH - 60) * random.random()), 5)

class Coin(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./images/coin.jpg"), (40, 40))

        self.rect = self.image.get_rect()
        self.rect.center = (10 + int((WIDTH - 10) * random.random()), 5)

        self.price = 1 
    
    def respawn(self):
        self.rect.center = (10 + int((WIDTH - 10) * random.random()), 5)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT :
            self.rect.move_ip(0, 3)
        else:
            self.rect.center = (10 + int((WIDTH - 10) * random.random()), 5)

buffs = pygame.sprite.Group() #coins/pickups etc
enemies = pygame.sprite.Group() #oncoming cars/obstacles
all_sprites = pygame.sprite.Group() 

P1 = Player()
E1 = Enemy()
E2 = Enemy()
C1 = Coin()
C2 = Coin()

enemies.add(E1)
buffs.add(C1, C2)
all_sprites.add(C1, C2, E1, P1)

done = False

FPS = 60

#setting up BGM
pygame.mixer.init()
pygame.mixer.music.load("./audio/background.wav") 
pygame.mixer.music.play(-1,0.0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    #drawing score interface
    backlog_points = [(WIDTH, 0), (WIDTH, 40), (WIDTH - 100, 40), (WIDTH - 130, 0), (WIDTH, 0)] 
    draw_polygon_alpha(screen, (255, 255, 255, 150), backlog_points)
    screen.blit(score, score_rect)
    actual_score = font_smaller.render(f"{P1.coin_score}", True, colorBLACK)
    actual_score_rect = actual_score.get_rect(topright = (WIDTH - 10, 0))
    screen.blit(actual_score, actual_score_rect)


    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("./audio/crash.wav").play()
        time.sleep(0.5)
                    
        screen.fill(colorRED)
        screen.blit(game_over, over_rect)
        
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    collided_coin = pygame.sprite.spritecollideany(P1, buffs) 
    if collided_coin != None:
        P1.coin_score += collided_coin.price
        collided_coin.respawn() 
    
    pygame.display.flip()
    clock.tick(FPS)
