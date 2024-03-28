import pygame
from enum import Enum

class Tool(Enum):
    Selector = 1
    Brush = 2
    Rectangle = 3
    Circle = 4
    Eyedropper = 5
    Eraser = 6

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
eydropper_layer = pygame.Surface((WIDTH, HEIGHT))


colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)


colorBG = colorBLACK


clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0

prevX = 0
prevY = 0

global currentTool
currentTool = Tool.Circle

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


done = False


color_wheel = pygame.image.load("images/color.png")
color_wheel = pygame.transform.scale(color_wheel, (335, 335))

while not done:
    
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
            eydropper_layer = base_layer
            if currentTool == Tool.Eyedropper:
                base_layer.blit(color_wheel, (0,0))#should introuduce additional layer for eyedropper
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            currX = event.pos[0]
            currY = event.pos[1]
            if LMBpressed: 
                if currentTool == Tool.Rectangle:    
                    pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.Circle:
                    pygame.draw.ellipse(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.Brush:
                    pygame.draw.rect(screen, colorRED, (currX, currY, THICKNESS, THICKNESS))
                    base_layer.blit(screen, (0, 0))
                elif currentTool == Tool.Eraser:
                    pygame.draw.rect(screen, colorBG, (currX, currY, THICKNESS * 2, THICKNESS * 2))
                    base_layer.blit(screen, (0, 0))
                elif currentTool == Tool.Eyedropper:
                    picked_color = pygame.Surface.get_at(base_layer, (currX, currY))
                    pygame.draw.rect(screen, picked_color, (currX + 20, currY+20, 20, 20), 10)
                    
            else:#this part draws crosshair and tool shape where applicable
                if currentTool == Tool.Eraser:
                    pygame.draw.rect(screen, colorRED, (currX, currY, THICKNESS * 2, THICKNESS * 2), 1)


        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if currentTool == Tool.Rectangle:
                pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif currentTool == Tool.Circle:
                pygame.draw.ellipse(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_b:
                print("brush tool equipped")
                currentTool = Tool.Brush
            if event.key == pygame.K_r:
                print("rectangle tool equipped")
                currentTool = Tool.Rectangle
            if event.key == pygame.K_c:
                print("circle (ellipse) tool equipped")
                currentTool = Tool.Circle
            if event.key == pygame.K_v:
                print("tool unequipped")
                currentTool = Tool.Selector
            if event.key == pygame.K_e:
                print("eraser tool equipped")
                currentTool = Tool.Eraser
            if event.key == pygame.K_i:
                print("eydropper equipped")
                currentTool = Tool.Eyedropper

            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1
                if THICKNESS <= 0:
                    THICKNESS = 1

    # pygame.draw.line(screen, colorRED, (prevX, prevY), (currX, currY), THICKNESS)

    pygame.display.flip()
    clock.tick(60)