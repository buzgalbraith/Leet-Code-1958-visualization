import pygame
import sys
WHITE = (255, 255, 255)
BLUE = (64,135,255)
BLACK = (0, 0, 0)
GREY=(96,96,96)
YELLOW = (204, 204, 0)
WIDTH = 800
D={".":BLUE, "B": BLACK, "W":WHITE}
class Node: 
    def __init__(self, row, col, width):
        self.row=row
        self.col=col
        self.x=int(col*width) ## in the original code i referenced self.x and self.y are swapped. 
        self.y=int(row*width)
        self.color=BLUE
    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y,WIDTH / 8, WIDTH / 8))
def make_grid(rows,width, game_state=None):
    ## here we are making an initial board that is all blue 
    ## once we have this piece working we can optimize this 
    grid=[]
    gap=WIDTH//rows
    print(gap)
    board=game_state[0]
    rMove =game_state[1]
    cMove =game_state[2]
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node=Node(i,j,gap)
            grid[i].append(node)
            if(game_state!=None):
                grid[i][j].color = D[board[i][j]]
    if(game_state!=None):
        grid[rMove][cMove].color = YELLOW
    return grid
def draw_gird(win,rows, width):
    gap=width//8
    for i in range(rows):
        pygame.draw.line(win,GREY,(0, i * gap), (width, i * gap) )
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
def update_display(win,grid,rows,width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_gird(win, rows, width)
    pygame.display.update()        
def main(WIN, WIDTH, game_state=None):
    grid=make_grid(8,WIDTH, game_state)
    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        update_display(WIN, grid, 8, WIDTH)
game_state=([[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."
]], 4,3, "B")

pygame.display.set_caption("{0} to move".format(game_state[3]))
WIN = pygame.display.set_mode((WIDTH, WIDTH))
main(WIN, WIDTH,game_state)
