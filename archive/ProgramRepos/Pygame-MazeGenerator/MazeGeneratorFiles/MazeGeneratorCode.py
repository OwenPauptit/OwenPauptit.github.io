import pygame, time, random,MazePlayingCode

########################################################################################################################


class Cell:
    def __init__(self,x,y,cellWidth,wallDepth):
        self.x = x
        self.y = y
        self.w = cellWidth
        self.walls = [1,2,3,4] #[above,right,below,left]
        self.d = wallDepth
        self.playing = False

        self.visited = False

    def drawSelf(self,screen):
        if self.visited and not self.playing:
            Rect = (self.x*self.w, self.y*self.w, self.w, self.w)
            pygame.draw.rect(screen,Colours.green,Rect)
        Rects = []
        if 1 in self.walls:
            Rects.append((self.x*self.w               , self.y*self.w               , self.w , self.d))
        if 2 in self.walls:
            Rects.append((self.x*self.w +self.w-self.d, self.y*self.w               , self.d , self.w))
        if 3 in self.walls:
            Rects.append((self.x*self.w               , self.y*self.w +self.w-self.d, self.w , self.d))
        if 4 in self.walls:
            Rects.append((self.x*self.w               , self.y*self.w               , self.d , self.w))
        for Rect in Rects:
            pygame.draw.rect(screen,Colours.white,Rect)


    def neighbours(self,grid):
        unvisited = []
        yArr = [self.y-1, self.y  , self.y+1, self.y  ]
        xArr = [self.x  , self.x+1, self.x  , self.x-1]
        for index,(x,y) in enumerate(zip(xArr,yArr),start=0):
            if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
                if not grid[y][x].visited:
                    unvisited.append(index)
        if len(unvisited) > 0:
            i = random.choice(unvisited)
            return xArr[i],yArr[i],i+1,len(unvisited)
        else:
            return -1,-1,-1,0

    def highlight(self,screen):
        if not self.playing:
            Rect = (self.x * self.w+self.d, self.y * self.w+self.d, self.w-self.d*2, self.w-self.d*2)
            pygame.draw.rect(screen, Colours.highlight, Rect)


########################################################################################################################


class Colours:
    white = (255,255,255)
    black = (0,0,0)
    green = (66, 161, 94)
    highlight = (43, 217, 116)
    red = (217, 48, 53)
    blue = (9, 52, 181)#(23, 95, 212)#(9, 37, 150)
    yellow = (230, 183, 16)
    cream = (247, 246, 208)

########################################################################################################################


def drawGrid(grid,screen):
    screen.fill(Colours.black)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x].drawSelf(screen)

########################################################################################################################


def removeWalls(current,grid,stack,counter=None,showPcnt=False,showMaze=False):
    x, y, direction, unvisited = current.neighbours(grid)
    if x != -1:
        del current.walls[current.walls.index(direction)]
        direction = direction - 2
        if direction < 1: direction = direction + 4
        current = grid[y][x]
        stack.append(current)
        del current.walls[current.walls.index(direction)]
        if counter:
            counter += 1
    elif len(stack) > 0:
        current = stack[len(stack)-1]
        del stack[len(stack)-1]
    else:
        MazePlayingCode.main(grid,showPcnt,showMaze)
    if counter:
        if showPcnt:
            print(counter, "/", len(grid) * len(grid[0])," = " + str(int(round(counter / (len(grid) * len(grid[0])) * 100, 2))) + "%")
        return current,grid,stack,counter
    else:
        return current, grid, stack

########################################################################################################################


def setup():
    import MazeSetupCode
    MazeSetupCode.main()

########################################################################################################################

def displayPcnt(counter,grid,screen):
    bitwonder = pygame.font.Font("8-BIT WONDER.TTF",54)
    digital = pygame.font.Font("digital-7.ttf",45)
    loading = bitwonder.render("Loading",1,Colours.black)
    loadpos = loading.get_rect()
    loadpos.center = (200,170)
    pc = round(counter/ (len(grid)*len(grid[0]*100)))
    pcnt = digital.render((str(round(counter*100/(len(grid)*len(grid[0])),1))+"%"),1,Colours.black)
    pcpos = pcnt.get_rect()
    pcpos.center = (205,240)
    screen.fill(Colours.cream)
    screen.blit(pcnt,pcpos)
    screen.blit(loading,loadpos)


def main(height=400,width=400,cellWidth=40,wallDepth=1,showMaze=False,showPcnt=False,change=0):

    if change == 1:
        width = width+5*cellWidth
        height = height+5*cellWidth
        if height > 1000:
            height = 1000
            cellWidth = cellWidth-1
            if cellWidth < 5:
                cellWidth = 5
            while height%cellWidth!=0 or width%cellWidth!=0:
                cellWidth = cellWidth - 1
        if width > 1800:
            width = 1800
            cellWidth = cellWidth -1
            if cellWidth < 5: cellWidth = 5
            while width%cellWidth!=0 or height%cellWidth!=0:
                cellWidth = cellWidth-1
    elif change == -1:
        width = width-5*cellWidth
        height = height-5*cellWidth
        if width < 10*cellWidth: width = 10*cellWidth
        if height < 10*cellWidth: height = 10*cellWidth
    pygame.init()
    if showMaze:
        screen = pygame.display.set_mode((width,height))
    else:
        screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption("Maze Generating...")
    rows = int(height/cellWidth)
    cols = int(width/cellWidth)



    grid = []
    for y in range(0,rows):
        temp = []
        for x in range(0,cols):
            temp.append(Cell(x,y,cellWidth,wallDepth))
        grid.append(temp)

    stack = []
    current = grid[0][0]
    stack.append(current)
    counter = 1
    while True:
        if not current.visited:
            current.visited = True
        if current.playing: break
        if showMaze:
            drawGrid(grid, screen)
            current.highlight(screen)
        else:
            displayPcnt(counter,grid,screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if showPcnt or not showMaze:
            current,grid,stack,counter = removeWalls(current,grid,stack,counter,showPcnt=showPcnt,showMaze=showMaze)
        else:
            current, grid, stack,counter = removeWalls(current, grid, stack,counter,showPcnt=showPcnt,showMaze=showMaze)

        #time.sleep(0.2)

########################################################################################################################


if __name__ == "__main__":
    main()
