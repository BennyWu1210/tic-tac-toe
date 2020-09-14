# tic tac toe
import pygame
import random
import sys

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('calibri', 50, True)
layout = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 0 = unoccupied, 1 = circle, 2 = X
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE')
black = (50, 50, 50)
white = (255, 255, 255)
backcolor = (102, 205, 0)
grey = (143, 155, 155)
Xscore = 0
Oscore = 0
center_pos = (250 + 1, 250 + 1)  # adjust the pos
xando = 0

status = [False, False]  # first False is for o, second false is for x


def draw_grid(screen, black):
    # draw the four lines
    x = 200
    y = 200
    pygame.draw.line(screen, black, (x, y - 100), (x, y + 200), 10)
    pygame.draw.line(screen, black, (x + 100, y - 100), (x + 100, y + 200), 10)
    pygame.draw.line(screen, black, (x - 100, y), (x + 200, y), 10)
    pygame.draw.line(screen, black, (x - 100, y + 100), (x + 200, y + 100), 10)

    pygame.display.update()


# testing
# screen.fill(backcolor)
# draw_grid(screen,black)

def score_display(font, Xscore, Oscore):
    pscore_display = font.render("X score: " + str(Xscore), True, black)
    screen.blit(pscore_display, (20, 25))
    escore_display = font.render("O score: " + str(Oscore), True, black)
    screen.blit(escore_display, (275, 25))

    pygame.display.update()


def background():
    screen.fill(backcolor)
    draw_grid(screen, black)
    score_display(font, Xscore, Oscore)


def create_grid(width):
    l = width
    # center point of each block
    center_point = [[(l * 3 / 10, l * 3 / 10), (l * 5 / 10, l * 3 / 10), (l * 7 / 10, l * 3 / 10)],
                    [(l * 3 / 10, l * 5 / 10), (l * 5 / 10, l * 5 / 10), (l * 7 / 10, l * 5 / 10)],
                    [(l * 3 / 10, l * 7 / 10), (l * 5 / 10, l * 7 / 10), (l * 7 / 10, l * 7 / 10)]]


def draw_x(screen, width, white, center_pos):
    pygame.draw.line(screen, white, (center_pos[0] + 30, center_pos[1] + 30), (center_pos[0] - 30, center_pos[1] - 30),
                     12)
    pygame.draw.line(screen, white, (center_pos[0] + 30, center_pos[1] - 30), (center_pos[0] - 30, center_pos[1] + 30),
                     12)
    pygame.display.update()


def draw_o(screen, white, center_pos, width):
    pygame.draw.circle(screen, white, center_pos, 35, 7)
    pygame.display.update()


def winDetection(layout, status):
    for i in range(3):
        if layout[0][i] == layout[1][i] == layout[2][i] and layout[0][i] != 0:  # vertical check
            pygame.draw.line(screen, grey, (151 + i * 100, 70), (151 + i * 100, 430), 8)
            if layout[0][i] == 1:
                status[0] = True
            elif layout[0][i] == 2:
                status[1] = True
            pygame.display.update()

        if layout[i][0] == layout[i][1] == layout[i][2] and layout[i][0] != 0:  # Horizonal check
            pygame.draw.line(screen, grey, (70, 151 + i * 100), (430, 151 + i * 100), 8)
            if layout[i][0] == 1:
                status[0] = True
            elif layout[i][0] == 2:
                status[1] = True
            pygame.display.update()

    if layout[0][0] == layout[1][1] == layout[2][2] and layout[0][0] != 0:
        pygame.draw.line(screen, grey, (86, 86), (414, 414), 10)
        if layout[1][1] == 1:
            status[0] = True
        elif layout[1][1] == 2:
            status[1] = True
        pygame.display.update()

    if layout[2][0] == layout[1][1] == layout[0][2] and layout[2][0] != 0:
        pygame.draw.line(screen, grey, (414, 86), (86, 414), 10)
        if layout[1][1] == 1:
            status[0] = True
        elif layout[1][1] == 2:
            status[1] = True
        pygame.display.update()

    return (status)


masterloop = True
firstloop = True

while masterloop:

    xando = 0
    status = [False, False]  # first False is for o, second false is for x
    layout = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 0 = unoccupied, 1 = circle, 2 = X
    background()
    draw_grid(screen, black)
    score_display(font, Xscore, Oscore)
    create_grid(width)
    firstloop = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        while firstloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    firstloop = False
                    masterloop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())
                    mousepos = pygame.mouse.get_pos()

                    if (mousepos[0] > 110 and mousepos[0] < 190 and mousepos[1] > 110 and mousepos[1] < 190) and \
                            layout[0][0] == 0:

                        center_pos = (150, 150)
                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[0][0] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[0][0] = 1
                        xando += 1

                    if (mousepos[0] > 210 and mousepos[0] < 290 and mousepos[1] > 110 and mousepos[1] < 190) and \
                            layout[0][1] == 0:
                        center_pos = (250, 150)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[0][1] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[0][1] = 1
                        xando += 1

                    if (mousepos[0] > 310 and mousepos[0] < 390 and mousepos[1] > 110 and mousepos[1] < 190) and \
                            layout[0][2] == 0:
                        center_pos = (350, 150)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[0][2] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[0][2] = 1
                        xando += 1

                    if (mousepos[0] > 110 and mousepos[0] < 190 and mousepos[1] > 210 and mousepos[1] < 290) and \
                            layout[1][0] == 0:
                        center_pos = (150, 250)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[1][0] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[1][0] = 1
                        xando += 1

                    if (mousepos[0] > 210 and mousepos[0] < 290 and mousepos[1] > 210 and mousepos[1] < 290) and \
                            layout[1][1] == 0:
                        center_pos = (250, 250)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[1][1] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[1][1] = 1
                        xando += 1

                    if (mousepos[0] > 310 and mousepos[0] < 390 and mousepos[1] > 210 and mousepos[1] < 290) and \
                            layout[1][2] == 0:
                        center_pos = (350, 250)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[1][2] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[1][2] = 1
                        xando += 1

                    if (mousepos[0] > 110 and mousepos[0] < 190 and mousepos[1] > 310 and mousepos[1] < 390) and \
                            layout[2][0] == 0:
                        center_pos = (150, 350)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[2][0] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[2][0] = 1
                        xando += 1

                    if (mousepos[0] > 210 and mousepos[0] < 290 and mousepos[1] > 310 and mousepos[1] < 390) and \
                            layout[2][1] == 0:
                        center_pos = (250, 350)

                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[2][1] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[2][1] = 1
                        xando += 1

                    if (mousepos[0] > 310 and mousepos[0] < 390 and mousepos[1] > 310 and mousepos[1] < 390) and \
                            layout[2][2] == 0:
                        center_pos = (350, 350)
                        if xando % 2 == 0:
                            draw_x(screen, width, white, center_pos)
                            layout[2][2] = 2
                        else:
                            draw_o(screen, white, center_pos, width)
                            layout[2][2] = 1
                        xando += 1
            if (winDetection(layout, status)) == [True, False]:
                print("owins")
                Oscore += 1
                screen.fill(black)
                pygame.draw.circle(screen, white, (width - 30, width - 30), 35, 9)
                O_win = font.render("O WINS: ", True, white)
                screen.blit(O_win, (width - 30, width - 30))
                pygame.display.update()
                pygame.time.delay(1500)
                pygame.display.update()
                firstloop = False

            elif (winDetection(layout, status)) == [False, True]:

                print("xwins")
                Xscore += 1

                screen.fill(white)

                pygame.draw.line(screen, black, (width / 2 - 30, width / 2 - 30), (width / 2 + 30, width / 2 + 30), 15)
                pygame.draw.line(screen, black, (width / 2 + 30, width / 2 - 30), (width / 2 - 30, width / 2 + 30), 15)
                X_win = font.render("X WINS: ", True, black)
                screen.blit(X_win, (width - 30, width - 30))
                pygame.display.update()
                pygame.time.delay(1500)
                pygame.display.update()
                firstloop = False

            elif xando == 9:

                screen.fill(grey)
                print("draw")
                draw = font.render("DRAW: ", True, white)
                screen.blit(draw, (width - 30, width - 30))
                pygame.display.update()
                pygame.time.delay(1500)
                pygame.display.update()
                firstloop = False
pygame.quit()
sys.exit()





