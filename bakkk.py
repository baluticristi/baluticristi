from elements import Flag
import random
import sizes
#conditii
def readVar():
    global  WIDTH1, HEIGHT1
    global HOWMANY1
    global BoxRows1

    WIDTH1, HEIGHT1 = sizes.WIDTH1, sizes.HEIGHT1
    HOWMANY1= sizes.HOWMANY1
    BoxRows1=sizes.BoxRows1

WIDTH1, HEIGHT1 = sizes.WIDTH1, sizes.HEIGHT1
HOWMANY1= sizes.HOWMANY1
BoxRows1=sizes.BoxRows1
startx1,starty1= sizes.startx1, sizes.starty1

#this is me game

empty =0
mine =-3
safe = -5
unknown =-1
flag=-2
safe= -4
badFlag=-5




def randBomb(howMany,n1,n2):

    while howMany:
        ok=1
        x=random.randint(0,(BoxRows1-1))
        y=random.randint(0,(BoxRows1-1))
        if grid[x][y]==mine or GridVizibil[x][y]==empty:
            continue
        minusuri =((-1,-1),(-1,0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        for minus in minusuri:
            mrow=n1+minus[0]
            mcol=n2+minus[1]
            if y==mcol and x==mrow:
                ok=0
        if ok==0:
            continue
        grid[x][y]=mine
        howMany-=1
        
        
def alocMatrix():
    readVar()
    global grid
    global GridVizibil
    grid=[[0 for i in range(BoxRows1)]for j in range(BoxRows1)]    
    GridVizibil=[[(-1) for i in range(BoxRows1)]for j in range(BoxRows1)]





def Click(row, col):
    if grid[row][col]==mine and GridVizibil[row][col]==unknown:
        GridVizibil[row][col]=mine
    elif GridVizibil[row][col]==unknown:
        GridVizibil[row][col]=Count(row, col)    


def Atentie(row, col):
    if GridVizibil[row][col]==unknown:
        GridVizibil[row][col]=flag
        return 0
    elif GridVizibil[row][col]==flag:
        GridVizibil[row][col]=unknown
        return 1
    return -1
def newAtentie(row,col):
    if GridVizibil[row][col]==flag:
        GridVizibil[row][col]=unknown
        
def Count(row,col):
    minusuri =((-1,-1),(-1,0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    count=0
    if grid[row][col]!=mine:
        for minus in minusuri:
            mrow=row+minus[0]
            mcol=col+minus[1]
            if(mrow>=0 and mrow<=(BoxRows1-1)) and (mcol>=0 and mcol<=(BoxRows1-1)):
                if(grid[mrow][mcol])==mine:
                    count+=1
        return count
