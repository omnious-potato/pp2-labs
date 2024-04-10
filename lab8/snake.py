import pygame
import random
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

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            return True
        
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
    def __init__(self, snake):
        self.pos = self.generate_new_position(snake)

    #generates proper position for food
    def generate_new_position(self, snake): 
        while True:
            new_pos = Point(random.randint(2, 24), random.randint(2, 18))
            
            #checking if position coincides with snake body
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake.body):
                return new_pos
        

    def draw(self, screen, cell):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * cell, self.pos.y * cell, cell, cell))


    def respawn(self, snake):
        self.__init__(snake)
