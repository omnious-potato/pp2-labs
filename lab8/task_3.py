import pygame, math

from enum import Enum

class Tool(Enum): #enum for clarity
    Selector = 1
    Brush = 2
    Rectangle = 3
    Circle = 4
    Eyedropper = 5
    Eraser = 6

pygame.init()

FPS = 60

#window size
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

colorBG = colorWHITE

screen.fill(colorBG)
base_layer = screen.copy()


clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = None
currY = None

prevX = None
prevY = None

global currentTool
currentTool = Tool.Selector #by default, tool doing nothing is selected

global currentColor
currentColor = colorRED


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


done = False


#color wheel asset
color_wheel = pygame.image.load("images/color.png")
color_wheel = pygame.transform.scale(color_wheel, (335, 335))

#procedure to draw line
def smartbrush_draw(surface, color, x1, y1, x2, y2, stroke):
    
    #currently unused
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    dt = 1/FPS
    v = (dx / dt, dy / dt)
    v_n = math.sqrt(v[0]**2 + v[1]**2)

    pygame.draw.line(screen, color, (x1, y1), (x2, y2), stroke) #better for faster mouse displacement
    pygame.draw.rect(screen, color, (x1, y1, stroke // 2, stroke // 2)) #slower mouse movement

while not done:
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
            if currentTool == Tool.Brush:
                smartbrush_draw(screen, currentColor, oldX, oldY, currX, currY, THICKNESS)
                base_layer.blit(screen, (0, 0))
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if currentTool == Tool.Eyedropper:
            screen.blit(color_wheel, (0,0))
            
        if event.type == pygame.MOUSEMOTION:
            # print("Position of the mouse:", event.pos)

            if(currX != None): oldX = currX #coordinates for brushes
            if(currY != None): oldY = currY
            
            currX = event.pos[0]
            currY = event.pos[1]

            if LMBpressed: 
                if currentTool == Tool.Rectangle:    
                    pygame.draw.rect(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.Circle:
                    pygame.draw.ellipse(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                # elif currentTool == Tool.Brush:
                    #pygame.draw.rect(screen, currentColor, (currX, currY, THICKNESS, THICKNESS))
                    # base_layer.blit(screen, (0, 0))
                elif currentTool == Tool.Eraser:
                    smartbrush_draw(screen, colorBG, oldX, oldY, currX, currY, THICKNESS * 2)
                    # pygame.draw.rect(screen, colorBG, (currX, currY, THICKNESS * 2, THICKNESS * 2))
                    base_layer.blit(screen, (0, 0))
                elif currentTool == Tool.Eyedropper:
                    #clamping values to avoid picking pixel color out of game window, otherwise, as it is crash occurs
                    normX = max(0, min(currX, WIDTH)) 
                    normY = max(0, min(currY, HEIGHT))
                    picked_color = pygame.Surface.get_at(screen, (normX, normY))
                    currentColor = picked_color
                    pygame.draw.rect(screen, picked_color, (currX + 20, currY+20, 20, 20), 10)             
                
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            if currentTool == Tool.Rectangle:
                pygame.draw.rect(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif currentTool == Tool.Circle:
                pygame.draw.ellipse(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
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
                if currentTool != Tool.Eyedropper:
                    print("increased thickness")
                else:
                    print("increased saturation")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                if currentTool != Tool.Eyedropper:
                    print("decreased thickness")
                else:
                    print("decreased saturation")
                THICKNESS -= 1
            
        THICKNESS = max(1, min(THICKNESS, 512))

    # pygame.draw.line(screen, currentColor, (prevX, prevY), (currX, currY), THICKNESS)
    pygame.display.flip()
    clock.tick(FPS)