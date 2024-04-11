import pygame, math

from enum import Enum

class Tool(Enum): #enum for clarity
    Selector = 1
    Brush = 2
    Rectangle = 3
    Circle = 4
    Eyedropper = 5
    Eraser = 6
    Square = 7
    RightTriangle = 8
    EquilateralTriangle = 9
    Rhombus = 10

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
SKEWNESS = 1

#This used for 2-point tools tracking while dragging the mouse along the canvas
currX = None
currY = None

prevX = None
prevY = None

global currentTool
currentTool = Tool.Selector #by default, tool doing nothing is selected

global currentColor
currentColor = colorRED

#returns proper rectangle given unordered coords
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

#returns square rectangle under given coords
def calculate_square(x1, y1, x2, y2):
    side = min(abs(x1 - x2), abs(y1 - y2))
    return pygame.Rect(min(x1, x2), min(y1, y2), side, side)
    

#draws rombus using given points as the diagonal as assuming diagonals' ration as SKEWNESS
def draw_rhombus(surface, color, x1, y1, x2, y2, stroke):
    points = [(x2, y2)]

    diagonal= (x2 - x1, y2 - y1) #vector representing given diagonal
    half_diag = (diagonal[0]/2, diagonal[1]/2)

    midpoint = ((x1 + x2)/2,(y1+y2)/2) #center point of rombus
    #orthogonal vector to diagonal from midpoint
    side_one =(-diagonal[1] * abs(SKEWNESS) + midpoint[0], diagonal[0] * abs(SKEWNESS) + midpoint[1]) 
    side_two =(diagonal[1]  * abs(SKEWNESS) + midpoint[0], -diagonal[0] * abs(SKEWNESS) + midpoint[1])

    side_length = math.sqrt(side_one[0]**2 + side_one[1]**2)
    if side_length < 1:
        return
    
    #order of points is important here
    points.append(side_one)
    points.append((x1, y1))
    points.append(side_two)

    pygame.draw.polygon(surface, color, points, stroke)
    for x in points: #additional code to make thick figures look less chagged on vertices
        pygame.draw.circle(surface, color, x, int(0.6 * stroke / math.sqrt(2)))

#right triangle put on hypothenuse on given line with assumed SKEWNESS parameter
def draw_right_triangle(surface, color, x1, y1, x2, y2, stroke):
    points = [(x1, y1), (x2, y2)]

    #let skewness variable be parameter for angle ratio in right triangle
    angle_ratio = 1/SKEWNESS
    alpha_angle = math.pi/(2 * angle_ratio + 2)
    
    hypo_vector = (x2 - x1, y2 - y1)
    hypo_length = math.sqrt(hypo_vector[0]**2 + hypo_vector[1]**2)
    if hypo_length < 1:
        return

    side_length = hypo_length * math.cos(alpha_angle)

    #rotating vector along known angle
    side_vector = (hypo_vector[0] * side_length / hypo_length, hypo_vector[1] * side_length / hypo_length) #length-normalised
    side_vector = (side_vector[0] * math.cos(alpha_angle) - side_vector[1] * math.sin(alpha_angle), \
                   side_vector[0] * math.sin(alpha_angle) + side_vector[1] * math.cos(alpha_angle)) #angle-normalised
    
    points.append((side_vector[0] + x1, side_vector[1] + y1))

    pygame.draw.polygon(surface, color, points, stroke)
    for x in points: 
        pygame.draw.circle(surface, color, x, int(0.6 * stroke / math.sqrt(2)))


#draws equilateral triangle with any rotational orientation
def draw_equilateral_triangle(surface, color, x1, y1, x2, y2, stroke):
    points = [(x2, y2)]
    height = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    side = int(height /math.sin(math.radians(60)))
    
    #vector of height from point to base
    height_vector  = (x2 - x1, y2 - y1)
    if height < 1:
        return #subpixel heights aren't supported
    
    #two orthogonal vector from base intersection to side vertices
    side_vector = (-height_vector[1] /height * side / 2 + x1 , height_vector[0] / height * side / 2 + y1)
    opposite_vector = (height_vector[1] /height * side / 2 + x1 , -height_vector[0] / height * side / 2 + y1)
    
    points.append(side_vector)
    points.append(opposite_vector)

    pygame.draw.polygon(surface, color, points, stroke)
    for x in points: 
        pygame.draw.circle(surface, color, x, int(0.6 * stroke / math.sqrt(2)))


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
                #brush actions are here because even if no mouse movement is present point should be drawn under cursor
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
            if(currX != None): oldX = currX #old/new motion coordinates for brush
            if(currY != None): oldY = currY
            
            #updating to current mouse positions
            currX = event.pos[0]
            currY = event.pos[1]

            if LMBpressed: #action when LMB is held down
                if currentTool == Tool.Rectangle:    
                    pygame.draw.rect(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.Square:
                    pygame.draw.rect(screen, currentColor, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.Circle:
                    pygame.draw.ellipse(screen, currentColor, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                elif currentTool == Tool.EquilateralTriangle:
                    draw_equilateral_triangle(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
                elif currentTool == Tool.RightTriangle:
                    draw_right_triangle(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
                elif currentTool == Tool.Rhombus:
                    draw_rhombus(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
                elif currentTool == Tool.Eraser:
                    smartbrush_draw(screen, colorBG, oldX, oldY, currX, currY, THICKNESS * 2)
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
            elif currentTool == Tool.Square:
                pygame.draw.rect(screen, currentColor, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif currentTool == Tool.EquilateralTriangle:
                draw_equilateral_triangle(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif currentTool == Tool.RightTriangle:
                draw_right_triangle(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
                base_layer.blit(screen, (0, 0))
            elif currentTool == Tool.Rhombus:
                draw_rhombus(screen, currentColor, prevX, prevY, currX, currY, THICKNESS)
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
            if event.key == pygame.K_s:
                print("square tool equipped")
                currentTool = Tool.Square
            if event.key == pygame.K_t:
                print("equilateral triangle tool equipped")
                currentTool = Tool.EquilateralTriangle
            if event.key == pygame.K_y:
                print("right triangle tool equipped")
                currentTool = Tool.RightTriangle
            if event.key == pygame.K_p:
                print("rhombus tool equipped")
                currentTool = Tool.Rhombus


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


            if event.key == pygame.K_UP:
                print("skewness increased")
                SKEWNESS += 0.1
            if event.key == pygame.K_DOWN:
                print("skewness decreased")
                SKEWNESS -= 0.1
                
        # SKEWNESS = max(1, min(SKEWNESS, 10000000))        
        THICKNESS = max(1, min(THICKNESS, 512))

    # pygame.draw.line(screen, currentColor, (prevX, prevY), (currX, currY), THICKNESS)
    pygame.display.flip()
    clock.tick(FPS)