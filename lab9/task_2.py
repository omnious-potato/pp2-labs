# The first half is just boiler-plate stuff...

import pygame
import os, sys, math
from color_palette import *
from snake import Point, Snake, Food, draw_grid_chess

#singleton class for storing various semi-persistent game parameters
class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance
            
    def __init__(self, width=800, height=600, fps=10):
        if not self.__initialized:
            self.width = width
            self.height = height
            self.fps = fps
            self.__initialized = True

    def set(self, key, value):
        #more deliberate choice would be dict with bunch of keys, but for now with 3 parameters it's implemented as is
        if key == "height":
            self.height = value
        if key == "width":
            self.width = value
        if key == "fps":
            self.fps = value


class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):

    current_config = Config(width, height, fps)

    pygame.init()
    screen = pygame.display.set_mode((current_config.width, current_config.height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        print(current_config.fps)
        clock.tick(current_config.fps)

# The rest is code where you implement your game using the Scenes model

class MenuScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.menu_items = ["Play", "Continue", "Options", "Quit"]
        self.active_index = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("sfpro", 60)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Move to the next scene when enter pressed
                    if self.active_index == 0:    
                        self.SwitchToScene(GameScene())

                    if self.active_index == 3:
                        pygame.quit()
                        sys.exit()
                    
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1

    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        for i, item in enumerate(self.menu_items):
            text = item
            if i == self.active_index:
                text = '+' + text

            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (60, i * 60 + 60))

class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.cell = 30
        self.snake = Snake()
        self.foods = [Food(self.snake), Food(self.snake)]
        self.requirement_to_next_level = 3

        #score, level text elements
        self.text_headers = ["Score:", "LVL"] #static part
        self.text_text = [0, 1] #respective initial values, 0 for score, 1 for level

        pygame.font.init()
        self.font = pygame.font.SysFont("sfpro", 60)

    def level_up(self):
        #making next level "harder" by increasing level up score cap and game speed
        self.requirement_to_next_level += 2
        
        config = Config()
        prev_fps = config.fps
        config.set("fps", prev_fps + 10) #increase game speed
        
        self.text_text[0] = 0 #erasing score for the next level
        self.text_text[1] += 1 #increase level indicator

    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.dx = 1
                    self.snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.dx = -1
                    self.snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.dx = 0
                    self.snake.dy = 1
                elif event.key == pygame.K_UP:
                    self.snake.dx = 0
                    self.snake.dy = -1
        
    def Update(self):
        for x in self.foods:
            x.check(self.snake)
        self.snake.move()

        #collision with window/cell boundary
        if self.snake.check_boundaries(Config()):
            #return fps to starting one
            config = Config()
            config.set("fps", 10)

            #switch to main menu
            self.SwitchToScene(MenuScene())
        
        #snake collides with food objects
        flag, weight, collided_obj = self.snake.check_collision(self.foods)
        if flag:
            self.text_text[0] += weight
            collided_obj.respawn(self.snake)
        
        #checking whether score is enough for the next level
        if self.text_text[0] >= self.requirement_to_next_level:
            self.level_up()
        
    
    def Render(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        draw_grid_chess(screen, width, height, self.cell)

        self.snake.draw(screen, self.cell)
        for x in self.foods:
            x.draw(screen, self.cell)

        for i, item in enumerate(self.text_headers):
            text = item + " " + str(self.text_text[i])

            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (30, i * 60 + 60))

run_game(Config().width, Config().height, Config().fps, MenuScene())