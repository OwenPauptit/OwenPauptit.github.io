import pygame, MazeGeneratorCode
########################################################################################################################


class Coords:
    #middleright,topleft,bottomright
    colsText = (296,32,203,17,295,47)
    rowsText = (colsText[0],118,colsText[2],colsText[3]+(118-colsText[1]),colsText[4],colsText[5]+(118-colsText[1]))
    cellText = (colsText[0], 193, colsText[2], colsText[3] + (193 - colsText[1]), colsText[4], colsText[5] + (193 - colsText[1]))
    wallText = (colsText[0], 257, colsText[2], colsText[3] + (257 - colsText[1]), colsText[4], colsText[5] + (257 - colsText[1]))
    #topleft,bottomright of buttons
    colsbtns = [(309,16,346,49),(356,16,393,49)]
    rowsbtns = [(colsbtns[0][0],102,colsbtns[0][2],colsbtns[0][3]+(102-colsbtns[0][1])),(colsbtns[1][0],102,colsbtns[1][2],colsbtns[1][3]+(102-colsbtns[1][1]))]
    cellbtns = [(colsbtns[0][0],177,colsbtns[0][2],colsbtns[0][3]+(177-colsbtns[0][1])),(colsbtns[1][0],177,colsbtns[1][2],colsbtns[1][3]+(177-colsbtns[1][1]))]
    wallbtns = [(colsbtns[0][0],241,colsbtns[0][2],colsbtns[0][3]+(241-colsbtns[0][1])),(colsbtns[1][0],241,colsbtns[1][2],colsbtns[1][3]+(241-colsbtns[1][1]))]

    mazebtns = [(210,314,279,350),(303,314,372,350)]
    pcntbtns = [(210,395,279,431),(303,395,372,431)]
    #topleft,bottomleft
    applybtn = (40,475,173,519)
    defbtn = (40,537,173,581)
    finbtn = (228,537,361,581)

########################################################################################################################



class TextBox():
    def __init__(self,coords,value,screen,bg,min,ref):
        x,y,x1,y1,x2,y2 = coords
        self.coords = coords
        self.midright = (x-4,y)
        self.text = str(value)
        self.value = value
        self.background = bg
        self.line = 0
        self.min = min
        self.ref = ref
        self.writing = False
        self.write(screen)

    def write(self,screen,condition=False):
        if not condition:
            text = str(self.value)
        else:
            text = self.text
        font = pygame.font.Font("digital-7.ttf",36)
        label = font.render(text, 1, MazeGeneratorCode.Colours.black)
        pos = label.get_rect()
        pos.midright = self.midright
        screen.blit(label,pos)

        if self.writing and condition:
            if self.line < 100:
                Rect = (pos.right,pos.y,2,pos.height)
                pygame.draw.rect(screen, MazeGeneratorCode.Colours.black, Rect)
            else:
                if self.line == 200:
                    self.line = 0
            self.line = self.line + 1

    def isValid(self,boxes,text=False):
        if text:
            if self.text == "":
                return False
            value = int(self.text)
        else:
            value = self.value
        if value >= self.min:
            cols = boxes[0].value
            rows = boxes[1].value
            w = boxes[2].value
            d = boxes[3].value
            if text:
                if self.ref == 1: cols = int(boxes[0].text)
                elif self.ref == 2: rows = int(boxes[1].text)
                elif self.ref == 3: w = int(boxes[2].text)
                elif self.ref == 4: d = int(boxes[3].text)

            maxWidth = 1800
            maxHeight = 1000
            if self.ref == 1:
                if cols*w<=maxWidth: return True
            elif self.ref == 2:
                if rows*w<=maxHeight: return True
            elif self.ref == 3:
                if cols*w<=maxWidth and rows*w<=maxHeight: return True
            elif self.ref == 4:
                if d <= w/5: return True
        return False

    def capture(self,screen,boxes,buttons):
        self.text = ""
        condition = True
        self.writing = True
        while condition:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if chr(event.key).isdigit():
                        self.text = self.text + chr(event.key)
                    elif event.key == pygame.K_RETURN:
                        condition = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
            drawApplied(boxes,buttons,screen,condition)
            pygame.display.update()
        self.writing = False
        if self.isValid(boxes,text=True) and self.text != '':
            try:
                self.value = int(self.text)
            except ValueError:
                self.text = str(self.value)
        else:
            self.text = str(self.value)

    def isClicked(self,x,y):
        _,_,x1,y1,x2,y2 = self.coords
        if x > x1 and x < x2 and y > y1 and y < y2:
            return True

########################################################################################################################


class Button():
    def __init__(self,coords,slct,screen,bg,size,textbox=None,change=0,linked=None,ref=None):
        self.coords = coords
        self.selected = slct
        self.background = bg
        self.size = size
        if self.size=="Small":
            self.textbox = textbox
            self.change = change
            self.repeat = 0
        if self.size=="Medium" and linked:
            self.linked = linked
            self.linked.linked = self
        if self.size == "Large":
            self.ref = ref
            self.repeat=0
        if self.selected:
            self.highlight(screen)

    def highlight(self,screen):
        x,y,*_ = self.coords
        GreHigh = pygame.image.load("greenHighlight"+self.size+".png")
        screen.blit(GreHigh,(x-2,y-2))
        if self.size == "Large" or self.size == "Small":
            if self.repeat==20:
                self.selected = False
                self.repeat = 0
            else:
                self.repeat = self.repeat + 1

    def isClicked(self,x,y,boxes):
        x1, y1, x2, y2 = self.coords
        if x > x1 and x < x2 and y > y1 and y < y2:
            type = self.select(boxes)
            if self.size == "Medium":
                self.linked.unselect()
            return type

    def select(self,boxes):
        self.selected = True
        if self.size == "Small":
            pvalue = self.textbox.value
            self.textbox.value = self.textbox.value + self.change
            self.textbox.text = str(self.textbox.value)
            if not self.textbox.isValid(boxes):
                self.textbox.value = pvalue
                self.textbox.text = str(pvalue)
        if self.size == "Large":
            if self.ref == "apply":
                return 1
            elif self.ref == "default":
                return 2
            elif self.ref == "finish":
                return 3
        return 0

    def unselect(self):
        self.selected = False

########################################################################################################################


def applySettings(boxes,buttons):
    cols = boxes[0].value
    rows = boxes[1].value
    w = boxes[2].value
    d = boxes[3].value
    showMaze = buttons[8].selected
    showPCNT = buttons[10].selected
    return cols, rows, w, d, showMaze, showPCNT

########################################################################################################################



def drawApplied(boxes,buttons,screen,condition=False):
    screen.fill(MazeGeneratorCode.Colours.white)

    for button in buttons:
        if button.selected:
            button.highlight(screen)

    screen.blit(boxes[0].background,(0,0))
    for box in boxes:
        box.write(screen,condition)


    pygame.display.update()

########################################################################################################################

def main(cols=10,rows=10,w=40,d=1,showMaze=False,showPcnt=False,defslct=False):
    import MazeGeneratorCode
    pygame.init()
    screen = pygame.display.set_mode((400,600))
    pygame.display.set_caption("Maze Set-up")
    background = pygame.image.load("setupBackground.png")
    screen.fill(MazeGeneratorCode.Colours.white)
    screen.blit(background,(0,0))
    changedSettings = False

    colsBox = TextBox(Coords.colsText,10,screen,background,10,1)
    rowsBox = TextBox(Coords.rowsText,10,screen,background,10,2)
    cellBox = TextBox(Coords.cellText,40,screen,background,5,3)
    wallBox = TextBox(Coords.wallText,1,screen,background,1,4)
    boxes = [colsBox,rowsBox,cellBox,wallBox]

    colsbtnM = Button(Coords.colsbtns[0], False, screen, background, "Small", textbox=colsBox, change=-10)
    colsbtnP = Button(Coords.colsbtns[1], False, screen, background, "Small", textbox=colsBox, change=10)
    rowsbtnM = Button(Coords.rowsbtns[0], False, screen, background, "Small", textbox=rowsBox, change=-10)
    rowsbtnP = Button(Coords.rowsbtns[1], False, screen, background, "Small", textbox=rowsBox, change=10)
    cellbtnM = Button(Coords.cellbtns[0], False, screen, background, "Small", textbox=cellBox, change=-5)
    cellbtnP = Button(Coords.cellbtns[1], False, screen, background, "Small", textbox=cellBox, change=5)
    wallbtnM = Button(Coords.wallbtns[0], False, screen, background, "Small", textbox=wallBox, change=-1)
    wallbtnP = Button(Coords.wallbtns[1], False, screen, background, "Small", textbox=wallBox, change=1)

    mazebtnY = Button(Coords.mazebtns[0], False, screen, background, "Medium")
    mazebtnN = Button(Coords.mazebtns[1], True,  screen, background, "Medium",linked=mazebtnY)
    pcntbtnY = Button(Coords.pcntbtns[0], False, screen, background, "Medium")
    pcntbtnN = Button(Coords.pcntbtns[1], True,  screen, background, "Medium",linked=pcntbtnY)

    applybtn = Button(Coords.applybtn,    False, screen, background, "Large", ref="apply")
    defaultbtn = Button(Coords.defbtn,  defslct, screen, background, "Large", ref="default")
    finishbtn = Button(Coords.finbtn,     False, screen, background, "Large", ref="finish")

    buttons = [colsbtnM,colsbtnP,rowsbtnM,rowsbtnP,cellbtnM,cellbtnP,wallbtnM,wallbtnP,mazebtnY,mazebtnN,pcntbtnY,pcntbtnN,applybtn,defaultbtn,finishbtn]

    #pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()

                for box in boxes:
                    if box.isClicked(x,y):
                        box.capture(screen,boxes,buttons)
                for button in buttons:
                    if button.isClicked(x,y,boxes):
                        type = button.isClicked(x,y,boxes)
                        if type == 1:
                            changedSettings = True
                            cols,rows,w,d,showMaze,showPcnt  = applySettings(boxes,buttons)
                        elif type == 2:
                            if changedSettings:
                                main(cols,rows,w,d,showMaze,showPcnt,defslct=True)
                            else:
                                main(defslct=True)
                        elif type == 3:
                            import MazeGeneratorCode
                            if changedSettings:
                                MazeGeneratorCode.main(height=rows * w, width=cols * w, cellWidth=w, wallDepth=d, showMaze=showMaze, showPcnt=showPcnt)
                            else:
                                MazeGeneratorCode.main()


        drawApplied(boxes, buttons, screen)

########################################################################################################################


if __name__ == main():
    main()
