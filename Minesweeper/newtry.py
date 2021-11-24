import pygame
import os

from pygame import key
import elements
import bakkk
import sizes
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()

width, height = sizes.WIDTH1, sizes.HEIGHT1
howmany= sizes.HOWMANY1
BoxRows=sizes.BoxRows1
BoxDim=sizes.BoxDim1
startx,starty= sizes.startx1, sizes.starty1
FlagsLeft=howmany

def readVar():
    global width, height
    global howmany
    global BoxRows
    global BoxDim
    global WIN
    global GAMEOVER
    global GAMEWON
    global BACKGROUND
    global COUNTERBG
    global FlagsLeft
    elements.update()
    width, height = sizes.WIDTH1, sizes.HEIGHT1
    howmany= sizes.HOWMANY1
    BoxRows=sizes.BoxRows1
    BoxDim=sizes.BoxDim1
    WIN = pygame.display.set_mode((width,height))
    BACKGROUND = pygame.transform.scale(BACKGROUND, (width,height))
    GAMEOVER = pygame.transform.scale(GAMEOVER, ((width//2),(height//2)))
    GAMEWON = pygame.transform.scale(GAMEWON, ((width//2),(height//2)))
    COUNTERBG = pygame.transform.scale(COUNTERBG, (200,100))
    FlagsLeft=howmany




WIN = pygame.display.set_mode((width,height))
pygame.display.set_caption("MineSweepy")
lBoxx,lBoxy=startx+(BoxRows*BoxDim),starty+(BoxRows*BoxDim)
WHITE=(255, 255,255)
FPS=120
BACKGROUND = pygame.image.load(os.path.join('images', 'bg.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (width,height))
COUNTERBG = pygame.image.load(os.path.join('images', 'counter_bg.png'))
COUNTERBG = pygame.transform.scale(COUNTERBG, (200,100))
MENUBG = pygame.image.load(os.path.join('images', 'MenuBg.png'))
MENUBG = pygame.transform.scale(MENUBG, (width,height))

GAMEOVER= pygame.image.load(os.path.join('images', 'done.png'))
GAMEOVER = pygame.transform.scale(GAMEOVER, ((width//2),(height//2)))
GAMEWON= pygame.image.load(os.path.join('images', 'win.png'))
GAMEWON = pygame.transform.scale(GAMEWON, ((width//2),(height//2)))

def checkGameWon():
    count=0
    for i in range(0,BoxRows):
        for j in range(0,BoxRows):
            if bakkk.GridVizibil[i][j]==bakkk.unknown or bakkk.GridVizibil[i][j]==bakkk.flag:
                count+=1
    if count==howmany:
        return False
    return True    

def checkGameOver(x,y,action):
    if not checkGameWon():
        return False

    if action==1:
        for i in range(0,BoxRows):
            for j in range(0,BoxRows):
                if x in range(startx+(i*BoxDim),startx+((i+1)*BoxDim)) and y in range(starty+(j*BoxDim),starty+((j+1)*BoxDim)):
                    if(bakkk.GridVizibil[j][i]==bakkk.mine): return False
                    
    return True

def check(x, y):
        if(bakkk.Count(x,y)==0):
            bakkk.Click(x,y)
            minusuri =((-1,-1),(-1,0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
            for minus in minusuri:
                mrow=x+minus[0]
                mcol=y+minus[1]
                if(mrow>=0 and mrow<BoxRows) and (mcol>=0 and mcol<BoxRows):
                    if bakkk.Count(mrow,mcol)>0 and bakkk.grid[mrow][mcol]!=bakkk.mine and bakkk.GridVizibil[mrow][mcol]==bakkk.unknown:
                        bakkk.Click(mrow,mcol)
                    elif bakkk.Count(mrow,mcol)==0 and bakkk.grid[mrow][mcol]!=bakkk.mine and bakkk.GridVizibil[mrow][mcol]==bakkk.unknown:
                        bakkk.Click(mrow,mcol)
                        check(mrow,mcol)
  


def updateBoxes(x,y,action):
    global FlagsLeft
    if action==1:
        for i in range(0,BoxRows):
            for j in range(0,BoxRows):
                if x in range(startx+(i*BoxDim),startx+((i+1)*BoxDim)) and y in range(starty+(j*BoxDim),starty+((j+1)*BoxDim)):
                    bakkk.Click(j,i)
    elif action==3:
        for i in range(0,BoxRows):
            for j in range(0,BoxRows):
                if x in range(startx+(i*BoxDim),startx+((i+1)*BoxDim)) and y in range(starty+(j*BoxDim),starty+((j+1)*BoxDim)):
                    if FlagsLeft>0:
                        test=bakkk.Atentie(j,i)
                        if test==0:
                            FlagsLeft-=1
                        elif test==1:
                            FlagsLeft+=1
                    elif bakkk.GridVizibil[j][i]==bakkk.flag:
                        FlagsLeft+=1
                        bakkk.newAtentie(j,i)

                    
def freeTilBomb():
    for i in range(BoxRows):
        for j in range(BoxRows):
            if bakkk.GridVizibil[i][j]==0:
                x=i
                y=j
    check(x,y)

    
def Which(x,y):
    if x>=startx and y>=starty and x<width-startx and y<height:    
        for i in range(0,BoxRows):
            for j in range(0,BoxRows):
                if x in range(startx+(i*BoxDim),startx+((i+1)*BoxDim)) and y in range(starty+(j*BoxDim),starty+((j+1)*BoxDim)):
                    return [j,i]
    return [-1,-1]


def printBoxes():
    decay=0
    decaydown=0
    for i in range(0,BoxRows):
        for j in range(0, BoxRows):
            if bakkk.GridVizibil[i][j] == -1:
                value=elements.Boxx
            elif bakkk.GridVizibil[i][j] == -2:
                value=elements.Flag
            elif bakkk.GridVizibil[i][j]== -3:
                value=elements.Explode
            elif bakkk.GridVizibil[i][j]== -4:
                value=elements.Safe
            elif bakkk.GridVizibil[i][j]== -5:
                value=elements.badFlag
            else:
                value=elements.Box[bakkk.GridVizibil[i][j]]
            WIN.blit(value, (startx+decay, starty+decaydown))
            decay+=elements.BoxD 
        decaydown+=elements.BoxD
        decay=0

def showAll():
        for i in range(0,BoxRows):
            for j in range(0,BoxRows):
                if bakkk.GridVizibil[i][j]==-1 and bakkk.grid[i][j]!=bakkk.mine:
                    bakkk.GridVizibil[i][j]=bakkk.Count(i,j)
                elif bakkk.grid[i][j]==bakkk.mine and bakkk.GridVizibil[i][j]==bakkk.unknown:
                    bakkk.GridVizibil[i][j]=bakkk.safe
                elif bakkk.GridVizibil[i][j]==bakkk.mine:
                    bakkk.GridVizibil[i][j]=bakkk.mine
                elif bakkk.GridVizibil[i][j]==bakkk.flag and bakkk.grid[i][j]!=bakkk.mine:
                    bakkk.GridVizibil[i][j]=bakkk.badFlag

currentTime=0

def counter():
    WIN.blit(COUNTERBG, (width-200-startx,2*startx))
    tm=currentTime//1000

    if(tm<10):
        WIN.blit(elements.Num[tm], (width-elements.NumDx-9-startx,2*startx+11))
    elif(tm<100):
        var2=tm//10
        var=tm%10
        WIN.blit(elements.Num[var], (width-elements.NumDx-9-startx,2*startx+11))
        WIN.blit(elements.Num[var2], (width-elements.NumDx-elements.NumDx-2-startx-9,2*startx+11))
    elif(tm<1000):
        var2=tm//10
        var3=var2//10
        var2=var2%10
        var=tm%10
        WIN.blit(elements.Num[var], (width-elements.NumDx-9-startx,2*startx+11))
        WIN.blit(elements.Num[var2], (width-elements.NumDx-elements.NumDx-2-startx-9,2*startx+11))
        WIN.blit(elements.Num[var3], (width-elements.NumDx-2*(elements.NumDx+2)-startx-9,2*startx+11))
    elif(tm>=1000):
        var2=tm//10
        var3=var2//10
        var4=var3//10
        var4=var4%10
        var3=var3%10
        var2=var2%10
        var=tm%10

        WIN.blit(elements.Num[var], (width-elements.NumDx-9-startx,2*startx+11))
        WIN.blit(elements.Num[var2], (width-elements.NumDx-elements.NumDx-2-startx-9,2*startx+11))
        WIN.blit(elements.Num[var3], (width-elements.NumDx-2*(elements.NumDx+2)-startx-9,2*startx+11))
        WIN.blit(elements.Num[var4], (width-elements.NumDx-3*(elements.NumDx+2)-startx-9,2*startx+11))



def HFlags():
    WIN.blit(COUNTERBG, (startx,2*startx))
    global FlagsLeft
    if(FlagsLeft<10):
        WIN.blit(elements.Num[FlagsLeft], (3*(elements.NumDx+2)+startx+9,2*startx+11))
    elif FlagsLeft<100:
        var2=FlagsLeft//10
        var=FlagsLeft%10
        WIN.blit(elements.Num[var], (3*(elements.NumDx+2)+startx+9,2*startx+11))
        WIN.blit(elements.Num[var2], (2*(elements.NumDx+2)+startx+9,2*startx+11))
    elif FlagsLeft<1000:
        var2=FlagsLeft//10
        var3=var2//10
        var2=var2%10
        var=FlagsLeft%10
        WIN.blit(elements.Num[var], (3*(elements.NumDx+2)+startx+9,2*startx+11))
        WIN.blit(elements.Num[var2], (2*(elements.NumDx+2)+startx+9,2*startx+11))
        WIN.blit(elements.Num[var3], (elements.NumDx+2+startx+9,2*startx+11))


    elif FlagsLeft>=1000:
        var2=FlagsLeft//10
        var3=var2//10
        var4=var3//10
        var4=var4%10
        var3=var3%10
        var2=var2%10
        var=FlagsLeft%10
        WIN.blit(elements.Num[var4], (startx+9,2*startx+11))
        WIN.blit(elements.Num[var3], (elements.NumDx+2+startx+9,2*startx+11))
        WIN.blit(elements.Num[var2], (2*(elements.NumDx+2)+startx+9,2*startx+11))
        WIN.blit(elements.Num[var], (3*(elements.NumDx+2)+startx+9,2*startx+11))


def playTheGaem():
    clock=pygame.time.Clock()
    no=True
    run=True
    bakkk.alocMatrix()
    screen()
    while no:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                no=False
                continue
            mx,my=pygame.mouse.get_pos()
            if event.type==MOUSEBUTTONDOWN:
                if mx>=startx and my>=starty and mx<width-startx and my<height-startx and event.button==1:    
                    updateBoxes(mx,my,event.button)
                    x=Which(mx,my)[0]
                    y=Which(mx,my)[1]
                    bakkk.randBomb(howmany, x, y)
                    no=False
                    freeTilBomb()
    screen()
    if event.type== pygame.QUIT:
        pygame.quit()

        
    if event.type!=pygame.QUIT:

        while run:
            clock.tick(FPS)
            global currentTime
            currentTime=pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:                               
                    run=False
                    continue
                mx,my=pygame.mouse.get_pos()
                if event.type==MOUSEBUTTONDOWN:
                    x=Which(mx,my)[0]
                    y=Which(mx,my)[1]
                    if bakkk.Count(x,y)==0 and event.button==1 and (bakkk.GridVizibil[x][y]==bakkk.unknown or bakkk.GridVizibil[x][y]==elements.Box[0]):
                        check(x,y)
                            
                    else:
                        updateBoxes(mx,my,event.button)
                    run=checkGameOver(mx,my,event.button)
            screen()

        if run==False:
            if checkGameWon()==False:
                displayGameWon()
            else:
                displayGameOver()

        end=True
        while end:
            for event in pygame.event.get():

                if event.type==MOUSEBUTTONDOWN:
                    end=False
                elif event.type == pygame.QUIT:                               
                    end=False
                else: end=True

        pygame.quit()

def playMenu():
    clock=pygame.time.Clock()
    no=True
    menu()
    while no:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                no=False
            mx,my=pygame.mouse.get_pos()
            if event.type==MOUSEBUTTONDOWN:
                if mx>elements.offsetButonx and my>elements.offsetButony:
                    if mx<(elements.offsetButonx+elements.ButtonDimx) and  my<(elements.offsetButony+elements.ButtonDimy):
                        if event.button==1:
                            return 1    #BASIC
                if mx>elements.offsetButonx and my>(elements.offsetButony+elements.ButtonDimy+20):
                    if mx<(elements.offsetButonx+elements.ButtonDimx) and  my<((elements.offsetButony+elements.ButtonDimy+20)+elements.ButtonDimy):
                        if event.button==1:
                            return 2    #MEDIU
                if mx>elements.offsetButonx and my>(elements.offsetButony+(2*(elements.ButtonDimy+20))):
                    if mx<(elements.offsetButonx+elements.ButtonDimx) and  my<((elements.offsetButony+(2*(elements.ButtonDimy+20)))+elements.ButtonDimy):
                        if event.button==1:
                            return 3    #EXPERT
                if mx>elements.offsetButonx and my>(elements.offsetButony+(3*(elements.ButtonDimy+20))):
                    if mx<(elements.offsetButonx+elements.ButtonDimx) and  my<((elements.offsetButony+(3*(elements.ButtonDimy+20)))+elements.ButtonDimy):
                        if event.button==1:
                            return 4    #CUSTOM
                          
        menu()
    pygame.quit()
    return 0



def screen():
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND, (0,0))
    HFlags()
    counter()

    printBoxes()
    pygame.display.update()

def LimiteAtinse():
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont('Impact', 32)
    text=myfont.render("Datele introduse au fost eronate,", True,(255,0,0))
    textrect=text.get_rect()
    textrect.center=(width//2,height//2-100)
    text2=myfont.render("vor fi ajustate la cea mai apropiata", True,(255,0,0))
    textrect2=text2.get_rect()
    textrect2.center=(width//2,height//2-50)
    text3=myfont.render("valoare corecta!", True,(255,0,0))
    textrect3=text3.get_rect()
    textrect3.center=(width//2,height//2)
    text4=myfont.render("Apasa orice tasta pentru a continua!", True,(0,0,0))
    textrect4=text4.get_rect()
    textrect4.center=(width//2,height//2+50)

    maybe=True
    while maybe:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                maybe=False
            if event.type==MOUSEBUTTONDOWN:
                maybe = False
            elif event.type == pygame.KEYDOWN:
                maybe = False

        WIN.fill(WHITE)
        WIN.blit(BACKGROUND, (0,0))
        WIN.blit(text,textrect)
        WIN.blit(text2,textrect2)
        WIN.blit(text3,textrect3)
        WIN.blit(text4,textrect4)
        pygame.display.update()


def displayGameOver():
    showAll()
    printBoxes()
    WIN.blit(GAMEOVER, ((width//2)-(width//4),(height//2)-(height//4)))
    pygame.display.update()

def displayGameWon():
    showAll()
    printBoxes()
    WIN.blit(GAMEWON, ((width//2)-(width//4),(height//2)-(height//4)))
    pygame.display.update()

def menu():
    WIN.fill(WHITE)
    WIN.blit(MENUBG, (0,0))
    WIN.blit(elements.Text,(elements.offsetButonx,-elements.offsetButony//3))
    WIN.blit(elements.Button,(elements.offsetButonx,elements.offsetButony))
    WIN.blit(elements.Mediu,(elements.offsetButonx,(elements.offsetButony+elements.ButtonDimy+20)))
    WIN.blit(elements.Expert,(elements.offsetButonx,(elements.offsetButony+(2*(elements.ButtonDimy+20)))))
    WIN.blit(elements.Custom,(elements.offsetButonx,(elements.offsetButony+(3*(elements.ButtonDimy+20)))))
    pygame.display.update()


def customMenu(new):

    myfont = pygame.font.SysFont('Times New Roman', 32)
    clock = pygame.time.Clock()
    txt = ""
    input_box = pygame.Rect(elements.offsetButonx,elements.offsetButony+50, 40, 50)
    optiune='Introdu numarul de '+new+':'
    text=myfont.render(optiune, True,(0,0,0))
    textrect=text.get_rect()
    textrect.x,textrect.y=elements.offsetButonx,elements.offsetButony
    yems=True
    while yems:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                               
                yems=False
            # mx,my=pygame.mouse.get_pos()
            if event.type==MOUSEBUTTONDOWN:
                yems = True
                txt = ""            
            elif event.type == pygame.KEYDOWN and yems:
                if event.key == pygame.K_RETURN:
                    yems = False
                    return txt
                elif event.key == pygame.K_BACKSPACE:
                    txt =  txt[:-1]
                elif event.key==pygame.K_0 or event.key==pygame.K_1 or event.key==pygame.K_2 or event.key==pygame.K_3 or event.key==pygame.K_4 or event.key==pygame.K_5 or event.key==pygame.K_6 or event.key==pygame.K_7 or event.key==pygame.K_8 or event.key==pygame.K_9:
                    txt += event.unicode

        WIN.blit(MENUBG, (0,0))
        WIN.blit(elements.Text,(elements.offsetButonx,-elements.offsetButony//3))
        text_surf = myfont.render(txt, True, (0, 0, 0))
        width = max(200, text_surf.get_width()+10)
        input_box.w = width
        pygame.draw.rect(WIN, (0, 0, 0), input_box, 7)
        pygame.Surface.fill(WIN,WHITE,input_box)
        WIN.blit(text_surf, (input_box.x+5, input_box.y+5))
        pygame.Surface.fill(WIN,WHITE,textrect)
        WIN.blit(text,textrect)

        pygame.display.update()

    pygame.quit()
    return 0

    


def main():
    sizes.initDim(600,800,9,10,60)
    readVar()
    menu()
    choice=False
    choice=playMenu()

    if choice!=0:
        if choice==1:#BASIC
            sizes.initDim(600,770,9,9,60)
            readVar()
            playTheGaem()
        if choice==2:#MEDIU
            sizes.initDim(700,870,16,40,40)
            readVar()
            playTheGaem()
        if choice==3:#HARD
            sizes.initDim(760,930,20,99,35)
            readVar()
            playTheGaem()
        if choice==4:#CUSTOM
            Boxes=int(customMenu('randuri'))
            Bombs=int(customMenu('mine'))
            ok=1

            if Boxes<3:
                LimiteAtinse()
                Boxes=4
                Bombs=2
                ok=0

            elif Bombs<=0:
                LimiteAtinse()
                Bombs=2
                ok=0

            if((Boxes**2)//2<Bombs):
                LimiteAtinse()
                Bombs=(Boxes**2)//2
                ok=0

            if(Boxes>140):
                LimiteAtinse()
                Boxes=140
                ok=0
            if Boxes>32 and Bombs<Boxes**2//10:
                if(ok==1):
                    LimiteAtinse()
                Bombs=(Boxes**2//10)
            if(Boxes<=10):
                Bs=60
            elif(Boxes<=16):
                Bs=40
            else:

                Bs=max(5,min(35,700//Boxes))
    
            
            W=max(470,60+Boxes*Bs)
            H=230+Boxes*Bs
            sizes.initDim(W,H,Boxes,Bombs,Bs)
            readVar()
            playTheGaem()

    
main()    
