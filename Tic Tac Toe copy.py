import pygame
import random
import sys
from pygame import gfxdraw, Rect
import time as t
import math
""" Oct 5: Fix animations
    add animations for X and O"""

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font_size = 40
font_ = pygame.font.SysFont('calibri', int(font_size/2), True)
font1 = pygame.font.SysFont('calibri', font_size, True)

font2 = pygame.font.SysFont('calibri', int(font_size*1.3), True)
font3 = pygame.font.SysFont('calibri', 60, True)
font4 = pygame.font.SysFont('calibri', 80, True)
mid_points = [[(150,150),(250,150),(350,150)],
              [(150,250),(250,250),(350,250)],
              [(150,350),(250,350),(350,350)]]
grid = [[],[],[]]
pygame.display.set_caption('TIC TAC TOE')
#color
black = (50, 50, 50)
white = (255, 255, 255)
backcolor = (102, 205, 0)
grey = (142, 142, 142)
antiquewhite = (250,235,215)
background_color = antiquewhite
menu_color = black
size=500
box_size = (100,100)
screen = pygame.display.set_mode((size, size))
players = []
pi = math.pi

class Background():
    def __init__(self, color):
        self.color = color
        self.size = size
        

    def draw(self):
        screen.fill(self.color)
        
    def display_grid(self):
        pygame.draw.line(screen, black, (200,100), (200,400), 12)
        pygame.draw.line(screen, black, (300,100), (300,400), 12)
        pygame.draw.line(screen, black, (100,200), (400,200), 12)
        pygame.draw.line(screen, black, (100,300), (400,300), 12)        
        
    

class Player():
    def __init__(self, name, score, ptype):
        self.name = name
        self.score = score
        self.ptype = ptype # Make this as a boolean; if True X, else O.

    
    def display_score(self):
        text = self.name + ":" + str(self.score)
        scoreDis = font1.render(text, True, black)
        if self.ptype:
            screen.blit(scoreDis, (int(size*0.07), int(size*0.05)))
        else:
            screen.blit(scoreDis, (int(size*0.07), int(size*0.12)))

        return text


class Box(Rect):
    def __init__(self, center, size, position=(-1, -1)):
        left = center[0]-size[0]/2
        top = center[1]-size[1]/2
        width = size[0]
        height = size[1]
        Rect.__init__(self, left, top, width, height)
        self.status = 0 # 0-empty, 1: X, 2: O
        self.position = position

    def show_symbol(self):
        if self.status == 1:
            draw_X(self.center)
        elif self.status == 2:
            draw_O(self.center)

    def draw_symbol(self):   #Hmmmm I'm starting to wonder whether it is a good idea to put it in a function
        count = 0
        x = self.center[0]
        y = self.center[1]
        if self.status == 1: #X   
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                
                if count<3:
                    pygame.draw.line(screen, grey, (x-30,y-30), (x+(count+1)*10, y+(count+1)*10), 10)
                    print("count" + str(count))
                    #print((x+count*5, y+count*5))
                elif count<6:
                    pygame.draw.line(screen, grey, (x+30,y-30), (x-(count%3)*10, y+(count%3)*10), 10)
                    print("count1" + str(count%3))
                    print(count%3)
                    #print((x-(count%6)*5, y+(count%6)*5))
                    #print(count%6)
                else:
                    return
                count += 1
                clock.tick(60)
                pygame.display.update()
                
        elif self.status == 2: #O
            count = 0
            while True:
                print("counttttt: "+str(count))
                print(count*pi)
                print("trueee" + str(count<=2.1))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if count<=2.1:
                    pygame.draw.arc(screen, grey, (x-35, y-35, 70, 70), 0, pi*count, 8)
                    #print(pi*count)
                else:
                    return
                pygame.display.update()
                count += 0.1
                

    
    
            
            
            
            

    
            
            
class InputBox:
    def __init__(self, x, y, w, h, player=0, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.txt_surface = font2.render(text, True, white)
        self.active = False
        self.finished = False
        self.player = player
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousepos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print("HI " + self.text)
                    if self.player-1 == 0:
                        ptype = True
                    else:
                        ptype= False
                    #p = Player(self.text, 0, ptype)
                    #players.append(p)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font2.render(self.text, True, white)
                
    def draw(self):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, (100, 100, 100), self.rect, 8)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width
        
                
        
     
        
def draw_X(center):
    x = center[0]
    y = center[1]
    pygame.draw.line(screen, grey, (x-30,y-30), (x+30, y+30), 10)
    pygame.draw.line(screen, grey, (x+30,y-30), (x-30, y+30), 10)
        
    
    
    
def draw_O(center):
    pygame.draw.circle(screen, grey, center, 35, 6)
    gfxdraw.aacircle(screen, center[0], center[1], 35, grey)
    

def winDetection(ptype):
    for lst in grid:
        if lst[0].status ==  lst[1].status ==  lst[2].status == ptype:
            return True
    for col in range(3):
        if grid[0][col].status == grid[1][col].status == grid[2][col].status == ptype:
            return True
    if grid[1][1].status == grid[2][2].status == grid[0][0].status == ptype:
        return True
    if grid[1][1].status == grid[0][2].status == grid[2][0].status == ptype:
        return True

    
    return False
        

def victory(ptype):
    global round_
    round_= False
    if ptype==1:
        players[0].score += 10
    else:
        players[1].score += 10
    
    print(str(ptype) + "WINS!")
    
    

def display():
    playing_background.draw()
    playing_background.display_grid()
    players[1].display_score()
    players[0].display_score()
    for i in grid:
        for j in i:
            j.show_symbol()
    # Display whoever's turn
    # trying to slowly reveal the text

    

def display_turn(ptype=-1, won=False):
    i = 0
    
    if ptype == 0:
        text = "X's Turn"
        turn_display = font2.render(text, True, black)
        screen.blit(turn_display, (size-len(text)*(font_size*1.2/2), size*0.05))
        
        
    elif ptype == 1:
        text = "O's Turn"
        turn_display = font2.render(text, True, black)
        screen.blit(turn_display, (size-len(text)*(font_size*1.2/2), size*0.05))
        
    if won:
        if ptype == 0:
            text = "X WINS!"
            turn_display = font2.render(text, True, black)
            screen.blit(turn_display, (size-len(text)*(font_size*1.2/2), size*0.05))
        elif ptype == 1:
            ext = "O WINS!"
            turn_display = font2.render(text, True, black)
            screen.blit(turn_display, (size-len(text)*(font_size*1.2/2), size*0.05))
    
    
def reset():
    #global round_
    
    global moves
    moves = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].status = 0
'''
def reveal_screen():
    global count1
    if count1<50:
        pygame.draw.rect(screen, background_color, (0, count1*10, size, size))
    else:
        count1 = 0
    count1 += 1
    
'''


# MENU PAGE
# variable name menu_color
menu = True
l = 0.32
w = 0.4
start_x = int(size*l)
start_y = int(size*w)

def start_button(l, w):
    start_x = int(size*l)
    start_y = int(size*w)
    pygame.draw.rect(screen, (200, 200, 200), (start_x, start_y+50, size-start_x*2, size-start_y*2))
    pygame.draw.line(screen, (100, 100, 100), (start_x,start_y+50), (start_x, size-start_y+50), 10)
    pygame.draw.line(screen, (100, 100, 100), (start_x-4,start_y+50), (size-start_x+5, start_y+50), 10)
    pygame.draw.line(screen, (100, 100, 100), (start_x-4,size-start_y+50), (size-start_x+5, size-start_y+50), 10)
    pygame.draw.line(screen, (100, 100, 100), (size-start_x,start_y+50), (size-start_x, size-start_y+50), 10)
    
    

start_box = Box((size/2-10, size/2+50), (size-start_x*2+10, size-start_y*2+50), (-1, -1))
pygame.draw.rect(screen, (150, 150, 200), start_box)
header = font3.render("Welcome to Benny's", True, white)
header2 = font4.render("TIC TAC TOE", True, white)
start_words = font3.render("START", True, white)
X = font2.render("X", True, (90, 90, 80))
Y = font2.render("Y", True, (90, 90, 80))
press_reminder1 = font_.render("Don't forget to press return", True, (80, 100, 80))
press_reminder2 = font_.render("after entering the names", True, (80, 100, 80))
rgb_value = [80, 150, 170]
top = [False, False, False]
mouse_click = False
text_input1 = Box((100, 400),(120, 50))
text_input2 = Box((400, 400),(120, 50))

input1 = InputBox(40, 400, 130, 50, 1)
input2 = InputBox(350, 400, 130, 50, 2)
input_boxes = [input1, input2]

def menu_display():
    menu_background = Background((rgb_value[0], rgb_value[1], rgb_value[2])) 
    menu_background.draw()   
    start_button(0.32, 0.4)
    screen.blit(header, (20, 50))
    screen.blit(header2, (50, 120))
    screen.blit(start_words, (start_x+15, size-start_y-15))
    screen.blit(X, (95, 360))
    screen.blit(Y, (405, 360))
    screen.blit(press_reminder1, (size/2-90, size-40))
    screen.blit(press_reminder2, (size/2-80, size-20))
    
while menu: # locate
    menu_display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
            mousepos = pygame.mouse.get_pos()
        for box in input_boxes:
            box.handle_event(event)
                
    
    for box in input_boxes:
        box.update()
        box.draw()
            
    if mouse_click:
        mouse_click = False  # Perhaps create player object here instead
        if start_box.collidepoint(mousepos):
            p1 = Player(input_boxes[0].text, 0, True)
            players.append(p1)
            p2 = Player(input_boxes[1].text, 1, False)
            players.append(p2)
            menu = False
    

    for rgb in range(len(rgb_value)):
        if rgb_value[rgb] > 200:
            top[rgb] = True
        elif rgb_value[rgb] < 20:
            top[rgb] = False
        if top[rgb]:
            rgb_value[rgb] -= random.randint(1, 2)
        else:
            rgb_value[rgb] += random.randint(1, 2)
            
    pygame.display.update()
    clock.tick(60)
    
    







for i in range(len(mid_points)):
    for j in range(len(mid_points[i])):
        grid[i].append(Box(mid_points[i][j], box_size, (i,j)))
        

    
    
pygame.display.update()
playing_background = Background(background_color)
playing = True # Runs while the program is running
round_ = False # Runs everytime a new game starts
moves = 0
player_turn = moves % 2
mouse_click = False
count = 0
count1 = 0
display_turn(player_turn)
n = 0


while playing:
    display()
    display_turn(player_turn)
    
    if count < 60:
        pygame.draw.rect(screen, background_color, ((size-8*(font_size*1.2/2), size*0.05-count*5, 8*font_size/2, 6*font_size/4)))
        count += 1

    
        
    '''
    text = "I'm cool"
    
    print(count)
    if count < 60:
        scoreDis = font1.render(text, True, black)
        screen.blit(scoreDis, (250, 0))
        count += 1
    
    print(pygame.time.get_ticks())
    '''

    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # There is a thing called "VIDEORESIZE"   
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mouse_click = True
                
    if round_:
        if moves == 9:
            #do some display
            print("draw")
            round_ = False
        elif mouse_click:
            mouse_click = False
            for lst in grid:
                for box in lst:
                    if box.collidepoint(mousepos) and box.status == 0:
                        count = 0
                        if players[player_turn].ptype:
                            box.status = 1
                        elif not players[player_turn].ptype:
                            box.status = 2
                        if winDetection(player_turn+1):
                            victory(player_turn+1)
                            display_turn(player_turn) 
                        box.draw_symbol() # draws the symbols with animation
                        print(winDetection(player_turn))
                        moves += 1
                        player_turn = (player_turn+1)%2
                        print(player_turn)

                                                                   
    else:
        
        if count1<60:
            pygame.draw.rect(screen, background_color, (0,  count1*10 - 80, size, size))
            count1 += 1
            if count1 == 20:
                reset()
        else:
            count1 = 0
            round_ = True
                   
        # SWIPE TWICE first: slide down; clear everything; second: slide up
        
        # resets everything(box status)
        
    clock.tick(60)
    
    pygame.display.update()




""" Perhaps do some animation when the object get placed
    Or when everytime a new round starts"""                
        
            

                        
                

