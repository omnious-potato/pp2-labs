import pygame
import random, time
from color_palette import *

def draw_grid(screen, width, height, cell):
    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colorGRAY, (i * cell, j * cell, cell, cell), 1)

def draw_grid_chess(screen, width, height, cell):
    colors = [colorWHITE, colorGRAY]

    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * cell, j * cell, cell, cell))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self, screen, cell):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * cell, head.y * cell, cell, cell))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * cell, segment.y * cell, cell, cell))


    #updated for list of foods rather than a single object
    def check_collision(self, foods):
        head = self.body[0]

        for food in foods:
            if head.x == food.pos.x and head.y == food.pos.y:
                print("Got food!")
                self.body.append(Point(head.x, head.y))
                return True, food.weight, food
        return False, 0, None
        
    def check_boundaries(self, config): #checks whether snake collides with game window boundary 
        
        #snake head coords
        head_x = self.body[0].x
        head_y = self.body[0].y

        #boundaries are measured in whole cells
        x_cells = config.width//30
        y_cells = config.height//30
        if head_x >= x_cells or head_x < 0 or head_y >= y_cells or head_y < 0: #boundaries are measured in whole cells
            print("Wall collision!")
            return True


class Food:
    def __init__(self, snake, foods=None):
        if foods:
            self.pos = self.generate_new_position(snake, foods)
        else:
            self.pos = self.generate_new_position(snake)

        
        self.weight, self.ttl = self.get_food_weight()
        self.spawn_time = pygame.time.get_ticks()

    #function to get random food weight with given distribution
    def get_food_weight(self):
        w_ttl = [(1, 15), (2, 10), (3, 5)] #weight and time-to-live (in seconds) for instance of food
        
        probabilities = [0.80, 0.18, 0.02]
        
        chosen_weight = random.choices(w_ttl, weights=probabilities)[0]

        return chosen_weight

    #generates proper position for food
    def generate_new_position(self, snake, foods=None): 
        while True:
            new_pos = Point(random.randint(2, 24), random.randint(2, 18))
            
            #checking if position coincides with snake body
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake.body):

                #checking if position coincide with other food positions
                if foods:
                    if not any(other_food.x == new_pos.x and other_food.y == new_pos.y for other_food in foods):
                        return new_pos
                else:
                    return new_pos
    
    #check whether food cell should be kept alive
    def check(self, snake):
        seconds_lived_so_far = (pygame.time.get_ticks() - self.spawn_time)/1000
        if seconds_lived_so_far >= self.ttl:
            #kill the cell (or rather re-init it)
            self.respawn(snake)


    def draw(self, screen, cell):

        if self.weight == 1:
            color = colorDARKGREEN
        if self.weight == 2:
            color = colorBLUE
        if self.weight == 3:
            color = colorGREEN
        
        pygame.draw.rect(screen, color, (self.pos.x * cell, self.pos.y * cell, cell, cell))


    def respawn(self, snake):
        self.__init__(snake)
