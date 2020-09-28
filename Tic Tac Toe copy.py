import pygame
import random
import sys
from pygame import gfxdraw, Rect
import time as t
""" Sept 28: display fonts in different lines"""

pygame.init()
pygame.font.init()
font1 = pygame.font.SysFont('calibri', 40, True)
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
size=500
box_size = (100,100)
screen = pygame.display.set_mode((size, size))

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
        return text


class Box(Rect):
    def __init__(self, center, size, position):
        left = center[0]-size[0]/2
        top = center[1]-size[1]/2
        width = size[0]
        height = size[1]
        Rect.__init__(self, left, top, width, height)
        self.status = 0 # 0-empty, 1: X, 2: O
        self.position = position

    def draw_symbol(self):
        if self.status == 1:
            draw_X(self.center)
        elif self.status == 2:
            draw_O(self.center)
        
     
        
def draw_X(center):
    x = center[0]
    y = center[1]
    pygame.draw.line(screen, grey, (x,y), (x+30, y+30), 10)
    pygame.draw.line(screen, grey, (x,y), (x-30, y-30), 10)
    pygame.draw.line(screen, grey, (x,y), (x+30, y-30), 10)
    pygame.draw.line(screen, grey, (x,y), (x-30, y+30), 10)
                     

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
    round_= False
    print(str(ptype) + "WINS!")
    
    
    
    

def display():
    background.draw()
    background.display_grid()
    player_1.display_score()
    player_2.display_score()
    '''
    grid[5].status = 1
    grid[4].status = 2
    '''
    for i in grid:
        for j in i:
            j.draw_symbol()
    # Display score
    txt = ''
    for obj in players:
        txt += obj.display_score() + ' ' #Need to calculate a constant to balance the space out
    scoreDis = font1.render(txt, True, black)
    pos = (box_size[0])/2
    screen.blit(scoreDis, (pos, 50))
    '''
    print(pos)
    print(txt)
    '''
    


player_1 = Player("B", 100, True)
player_2 = Player("Yic", 100, False)
players = [player_1, player_2]

background = Background(antiquewhite)
display()
for i in range(len(mid_points)):
    for j in range(len(mid_points[i])):
        grid[i].append(Box(mid_points[i][j], box_size, (i,j)))


pygame.display.update()

playing = True # Runs while the program is running
round_ = False # Runs everytime a new game starts

while playing:
    display()
    
    #print("BYEEE")
    if round_:
        for event in pygame.event.get():
            #print("hi")
            if event.type==pygame.QUIT: # There is a thing called "VIDEORESIZE"   
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                for lst in grid:
                    for box in lst:
                        if box.collidepoint(mousepos) and box.status == 0:
                            if players[player_turn].ptype:
                                box.status = 1
                            elif not players[player_turn].ptype:
                                box.status = 2
                            if winDetection(player_turn+1):
                                victory(player_turn+1) # do all the things inside this function
                            print(winDetection(player_turn+1))
                            moves += 1
                            player_turn = moves % 2
                            # box.draw_symbol()
                            print(player_turn)
                            
                                
    else:
        moves = 0
        player_turn = moves % 2
        round_ = True
        # resets everything(box status)
        
                    
    
    pygame.display.update()
    

                        

""" Perhaps do some animation when the object get placed
    Or when everytime a new round starts"""                
        
            

                        
                

