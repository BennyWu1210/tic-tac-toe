import pygame
import random
import sys
from pygame import gfxdraw, Rect
import time as t
import math
""" Oct 15: Added button class and it works now
    Added background music
    Added a stupid computer player
    """


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font_size = 40
font_ = pygame.font.SysFont('calibri', int(font_size/2), True)
font1 = pygame.font.SysFont('calibri', font_size, True)

font2 = pygame.font.SysFont('calibri', int(font_size*1.3), True)
font60 = pygame.font.SysFont('calibri', 60, True)
font70 = pygame.font.SysFont('calibri', 70, True)
font80 = pygame.font.SysFont('calibri', 80, True)
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
songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
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
    def __init__(self, name, score, ptype, cpu=False):
        self.name = name
        self.score = score
        self.ptype = ptype # Make this as a boolean; if True X, else O.
        self.cpu = cpu
    
    def display_score(self):
        text = self.name + ":" + str(self.score)
        scoreDis = font1.render(text, True, black)
        if self.ptype:
            screen.blit(scoreDis, (int(size*0.07), int(size*0.05)))
        else:
            screen.blit(scoreDis, (int(size*0.07), int(size*0.12)))

        return text

    def cpu_move_easy(self, grid): # The easy version
        for rows in grid:
            for box in rows:
                pass
                
        
        r1 = random.randint(0,2)
        r2 = random.randint(0,2)
        b = grid[r1][r2]
        while b.status!=0:
            r1 = random.randint(0,2)
            r2 = random.randint(0,2)
            b = grid[r1][r2]
          
        return (r1, r2)

    def block_lastbox(self, grid, status):
        for rows in grid:
            for box in rows:
                 
                return index
                    
                    
                    
                    
                
                
                
        
        
        
        
    
        


class Box(Rect):
    def __init__(self, center, size, position=(-1, -1)):
        left = center[0]-size[0]/2 + 5
        top = center[1]-size[1]/2 + 5
        width = size[0] - 10
        height = size[1] - 10
        Rect.__init__(self, left, top, width, height)
        self.status = 0 # 0-empty, 1: X, 2: O
        self.position = position
 
    def show_symbol(self):
        if self.status == 1:
            draw_X(self.center)
        elif self.status == 2:
            draw_O(self.center)

    def draw_symbol(self):
        print("1")
        count = 0
        count1 = 0
        x = self.center[0]
        y = self.center[1]
        screenshot = pygame.Surface((200,60))
        screenshot.blit(screen, (-289,-15,160,60))
        pygame.image.save(screenshot, "turn.jpg")
        turn = pygame.image.load("turn.jpg")
        if self.status == 1:       #hh locate
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                
                if count<=3:
                    pygame.draw.line(screen, grey, (x-30,y-30), (x+(count)*10, y+(count)*10), 10)
                if 5<count<=8:
                    pygame.draw.line(screen, grey, (x+30,y-30), (x-(count%3+1)*10, y+(count%3+1)*10), 10) 
                if count1 < 30:
                    screen.blit(turn, (289,15))
                    pygame.draw.rect(screen, background_color, ((size-8*(font_size*1.2/2), size*0.05-count1*2-10, 8*font_size/2, 6*font_size/4+5)))
                else:
                    return
                count += 1
                count1 += 2
                clock.tick(60)
                pygame.display.update()
                
                
        elif self.status == 2: #O
            count = 0
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if count<=2.1:
                    pygame.draw.arc(screen, grey, (x-35, y-35, 70, 70), 0, pi*count, 8)
                if count1 < 30:  # Cannot update screen here so the animation disppears, how can I fix this? NVM I kinda fixed it but it took me 2 hours
                    screen.blit(turn, (289,15))
                    pygame.draw.rect(screen, background_color, ((size-8*(font_size*1.2/2), size*0.05-count1*2-10, 8*font_size/2, 6*font_size/4+5)))
                else:
                    return
                count += 0.2
                count1 += 2
                clock.tick(60)
                pygame.display.update()



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
        pygame.draw.rect(screen, (100, 100, 100), self.rect, 5)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width
      

class Button(Rect):
    def __init__(self, color, center, width, height, text='', font=font60, side=True):
        self.color = color
        
        self.width= width
        self.height = height
        self.x = center[0]-width/2
        self.y = center[1]-height/2
        Rect.__init__(self, self.x, self.y, width, height)
        self.text = text
        self.font = font
        self.side = side

        
    def draw_button(self, color=black, wid=10):
        
        x = self.x
        y = self.y
        h = self.height
        w = self.width
        font = self.font
        
        pygame.draw.rect(screen, self.color, (x, y, w, h))
        
        if self.side:
            pygame.draw.line(screen, color, (x-4, y), (x+w+5, y), wid)
            pygame.draw.line(screen, color, (x-4, y+h), (x+w+5, y+h), wid)
            pygame.draw.line(screen, color, (x, y), (x, y+h), wid)
            pygame.draw.line(screen, color, (x+w, y), (x+w, y+h), wid)
        
        
        start_words = font.render(self.text, True, white)
        screen.blit(start_words, ((w-start_words.get_rect().width)/1.7+x, (h-start_words.get_rect().height)/1.7+y))      
        
        
     
        
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
            text = "O WINS!"
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
menu = True
x = int(size/2)
y = int(size/1.6)
width = 200
height = 100
start_button = Button(grey, [x, y], width, height, "START")
x = start_button.x
y = start_button.y

header = font60.render("Welcome to Benny's", True, white)
header2 = font80.render("TIC TAC TOE", True, white)
X = font2.render("X", True, (90, 90, 80))
Y = font2.render("Y", True, (90, 90, 80))
rgb_value = [80, 150, 170]
top = [False, False, False]
mouse_click = False
mouse_on_start = False
mouse_motion = False
input1 = InputBox(40, 400, 130, 50, 1)
input2 = InputBox(335, 400, 130, 50, 2)
input_boxes = [input1, input2]
enlarged=False

def menu_display(enlarged=False):
    menu_background = Background((rgb_value[0], rgb_value[1], rgb_value[2])) 
    menu_background.draw()
    start_button.draw_button()
    screen.blit(header, (20, 50))
    screen.blit(header2, (50, 120))
    screen.blit(X, (95, 360))
    screen.blit(Y, (385, 360))
'''
menu_song = random.choice(songs)
pygame.mixer.music.load(menu_song)
pygame.mixer.music.play()
'''
while menu: # mm locate
    menu_display()
    for event in pygame.event.get():
        mousepos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
            
        for box in input_boxes:
            box.handle_event(event)
    
    if start_button.collidepoint(mousepos):
        start_button.x = x-10
        start_button.y = y-10
        start_button.width = width+20
        start_button.height = height+20
        start_button.font = font70
        
    else:
        start_button.x = x
        start_button.y = y
        start_button.width = width
        start_button.height = height
        start_button.font = font60
        
        
        


        
    
    for box in input_boxes:
        box.update()
        box.draw()
        
    if mouse_click:
        mouse_click = False  # Perhaps create player object here instead
        if start_button.collidepoint(mousepos):
            p1 = Player(input_boxes[0].text, 0, True, True)
            players.append(p1)
            p2 = Player(input_boxes[1].text+"robot" , 0, False, True)
            players.append(p2)
            menu = False
    

    for rgb in range(len(rgb_value)):
        if rgb_value[rgb] > 220:
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
t1 = -1
'''

playing_song = random.choice(songs)
pygame.mixer.music.load(playing_song)
pygame.mixer.music.play()
'''
while playing:
    display()
    display_turn(player_turn)
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
            
        elif not players[player_turn].cpu:
            if mouse_click:
                mouse_click = False
                for lst in grid:
                    for box in lst:
                        if box.collidepoint(mousepos) and box.status == 0:
                            if players[player_turn].ptype:
                                box.status = 1
                            elif not players[player_turn].ptype:
                                box.status = 2
                            if winDetection(player_turn+1):
                                victory(player_turn+1)
                            
                            moves += 1
                            player_turn = (player_turn+1)%2
                            box.draw_symbol() # draws the symbols with animation

        else:
            if t1 == -1:
                t1 = pygame.time.get_ticks()
                
            if pygame.time.get_ticks()>300+t1:
                t1 = -1
                coords = players[player_turn].cpu_move_easy(grid)
                box = grid[coords[0]][coords[1]]
                if players[player_turn].ptype:
                    box.status = 1
                elif not players[player_turn].ptype:
                    box.status = 2
                if winDetection(player_turn+1):
                    victory(player_turn+1)
                moves += 1
                player_turn = (player_turn+1)%2
                box.draw_symbol() # draws the symbols with animation
            
                    
                        
                        
                        
                        

                                                                   
    else:
        
        if count1<60:
            pygame.draw.rect(screen, background_color, (0,  count1*10 - 80, size, size))
            count1 += 1
            if count1 == 20:
                reset()
        else:
            count1 = 0
            count = 0
            round_ = True
                
        # resets everything(box status)
        
    clock.tick(60)
    
    pygame.display.update()
    




""" Perhaps do some animation when the object get placed
    Or when everytime a new round starts"""                
        
            

                        
                

