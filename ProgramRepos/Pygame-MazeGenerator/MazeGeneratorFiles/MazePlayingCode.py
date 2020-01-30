import pygame,MazeGeneratorCode, time#, MazeSetupCode

########################################################################################################################


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self,grid,xchange=0,ychange=0):
        current = grid[self.y][self.x]
        dict = {-1: 1, 1: 3}
        if xchange == 0: direction = dict[ychange]
        else: direction = dict[xchange * -1] + 1
        if not direction in current.walls:
            self.x = self.x + xchange
            self.y = self.y + ychange

    def drawSelf(self,grid,screen):
        cell = grid[self.y][self.x]
        quarter = int(cell.w/4)
        Rect = (cell.x * cell.w + quarter, cell.y * cell.w + quarter, quarter * 2, quarter * 2)
        pygame.draw.rect(screen, (MazeGeneratorCode.Colours.red), Rect)

########################################################################################################################


def drawFinish(grid,screen):
    finish = grid[len(grid)-1][len(grid[0])-1]
    fRect = (finish.x * finish.w+finish.d, finish.y * finish.w+finish.d, finish.w-finish.d*2, finish.w-finish.d*2)
    pygame.draw.rect(screen, (MazeGeneratorCode.Colours.green), fRect)

########################################################################################################################


def win(width,height,screen,grid,showPcnt,showMaze):

    if width <= height:
        tinyFont = pygame.font.Font("8-BIT WONDER.TTF", int(width / 20))
        smallFont = pygame.font.Font("8-BIT WONDER.TTF", int(width / 15))
        bigFont = pygame.font.Font("8-BIT WONDER.TTF", int(width / 8))
        xpadding = int(width/15)
        ypadding = int(width/40)
    else:
        tinyFont = pygame.font.Font("8-BIT WONDER.TTF", int(height / 20))
        smallFont = pygame.font.Font("8-BIT WONDER.TTF", int(height / 15))
        bigFont = pygame.font.Font("8-BIT WONDER.TTF", int(height / 8))
        xpadding = int(height/5)
        ypadding = int(height/25)

    labelWin = bigFont.render("You Win", 1, MazeGeneratorCode.Colours.blue)
    winPos = labelWin.get_rect()
    winPos.center = (int(width/2),int(height/5))
    screen.blit(labelWin,winPos)

    texts = ["Same","Easier","Harder"]
    colours = [MazeGeneratorCode.Colours.yellow, MazeGeneratorCode.Colours.green, MazeGeneratorCode.Colours.red]
    order = [2,1,3]
    Rects = []

    for i in range(0,3):
        label = smallFont.render(texts[i], 1, MazeGeneratorCode.Colours.white)
        pos = label.get_rect()
        pos.center = (width/2,height/5*(order[i]+1))

        if order[i] == 2:
            x = pos.x-xpadding
            w = pos.width+xpadding *2
            h = pos.height+ypadding*2
        Rect = (x,pos.y-ypadding,w,h)
        Rects.append(Rect)
        pygame.draw.rect(screen,colours[i],Rect)#(int(width/3.6),int(height/5*(i+0.75)),width/2.22,width/10))
        screen.blit(label,pos)

    label = tinyFont.render("Press S for setup", 1, MazeGeneratorCode.Colours.blue)
    pos = label.get_rect()
    pos.bottomleft = (width/40,height-width/40)
    screen.blit(label,pos)

    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > Rects[0][0] and x < Rects[0][0]+Rects[0][2]:
                    if y > Rects[0][1] and y < Rects[0][1] + Rects[0][3]:
                        change = 0
                        MazeGeneratorCode.main(change=change, height=height, width=width,cellWidth=grid[0][0].w,showPcnt=showPcnt,showMaze=showMaze)
                    if y > Rects[1][1] and y < Rects[1][1] + Rects[1][3]:
                        change = -1
                        MazeGeneratorCode.main(change=change, height=height, width=width,cellWidth=grid[0][0].w,showPcnt=showPcnt,showMaze=showMaze)
                    if y > Rects[2][1] and y < Rects[2][1] + Rects[2][3]:
                        change = 1
                        MazeGeneratorCode.main(change=change,height=height,width=width,cellWidth=grid[0][0].w,showPcnt=showPcnt,showMaze=showMaze)
            if event.type == pygame.KEYDOWN:
                if event.key == ord("s"):
                    MazeGeneratorCode.setup()


########################################################################################################################


def main(grid,showPcnt,showMaze):
    width = grid[0][0].w * len(grid[0])
    height = grid[0][0].w * len(grid)
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Maze Game")
    current = [0,0]
    for row in grid:
        for cell in row:
            cell.playing = True
    player = Player()

    while True:
        MazeGeneratorCode.drawGrid(grid, screen)
        drawFinish(grid, screen)
        player.drawSelf(grid,screen)
        pygame.display.update()

        if player.x == len(grid[0])-1 and player.y == len(grid)-1:
            win(width,height,screen,grid,showPcnt,showMaze)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: player.move(grid,xchange=1)
                elif event.key == pygame.K_LEFT: player.move(grid,xchange=-1)
                elif event.key == pygame.K_UP: player.move(grid,ychange=-1)
                elif event.key == pygame.K_DOWN: player.move(grid,ychange=1)

########################################################################################################################


if __name__ == "__main__":
    MazeGeneratorCode.main()
