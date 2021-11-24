import pygame
import os
import sizes
offsetButonx,offsetButony=100,100
ButtonDimx,ButtonDimy=400, 150
NumDx,NumDy=44,76
BoxD=sizes.BoxDim1

def update():
    global BoxD
    global Boxx
    global Flag
    global badFlag
    global Button
    global Mediu
    global Expert
    global Text
    global Custom
    global Explode
    global Safe
    BoxD=sizes.BoxDim1
    Boxx = pygame.transform.scale(Boxx, (BoxD,BoxD))
    Flag = pygame.transform.scale(Flag, (BoxD,BoxD))
    badFlag = pygame.transform.scale(badFlag, (BoxD,BoxD))
    Box[0] = pygame.transform.scale(Box[0], (BoxD,BoxD))
    Box[1] = pygame.transform.scale(Box[1], (BoxD,BoxD))
    Box[2] = pygame.transform.scale(Box[2], (BoxD,BoxD))
    Box[3] = pygame.transform.scale(Box[3], (BoxD,BoxD))
    Box[4] = pygame.transform.scale(Box[4], (BoxD,BoxD))
    Box[5] = pygame.transform.scale(Box[5], (BoxD,BoxD))
    Box[6] = pygame.transform.scale(Box[6], (BoxD,BoxD))
    Box[7] = pygame.transform.scale(Box[7], (BoxD,BoxD))
    Box[8] = pygame.transform.scale(Box[8], (BoxD,BoxD))
    Button = pygame.transform.scale(Button, (ButtonDimx,ButtonDimy))
    Mediu = pygame.transform.scale(Mediu, (ButtonDimx,ButtonDimy))
    Expert = pygame.transform.scale(Expert, (ButtonDimx,ButtonDimy))
    Text = pygame.transform.scale(Text, (ButtonDimx,ButtonDimy))
    Custom = pygame.transform.scale(Custom, (ButtonDimx,ButtonDimy))
    Explode = pygame.transform.scale(Explode, (BoxD,BoxD))
    Safe = pygame.transform.scale(Safe, (BoxD,BoxD))


Boxx = pygame.image.load(os.path.join('images', 'empty_block.png'))
Boxx = pygame.transform.scale(Boxx, (BoxD,BoxD))

Box=[]
Num=[]

Flag = pygame.image.load(os.path.join('images', 'flag.png'))
Flag = pygame.transform.scale(Flag, (BoxD,BoxD))
badFlag = pygame.image.load(os.path.join('images', 'bad_flag.png'))
badFlag = pygame.transform.scale(badFlag, (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '0.png')))
Box[0] = pygame.transform.scale(Box[0], (BoxD,BoxD))
Box.append( pygame.image.load(os.path.join('images', '1.png')))
Box[1] = pygame.transform.scale(Box[1], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '2.png')))
Box[2] = pygame.transform.scale(Box[2], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '3.png')))
Box[3] = pygame.transform.scale(Box[3], (BoxD,BoxD))
Box.append( pygame.image.load(os.path.join('images', '4.png')))
Box[4] = pygame.transform.scale(Box[4], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '5.png')))
Box[5] = pygame.transform.scale(Box[5], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '6.png')))
Box[6] = pygame.transform.scale(Box[6], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '7.png')))
Box[7] = pygame.transform.scale(Box[7], (BoxD,BoxD))
Box.append(pygame.image.load(os.path.join('images', '8.png')))
Box[8] = pygame.transform.scale(Box[8], (BoxD,BoxD))
Button = pygame.image.load(os.path.join('images', 'buton.png'))
Button = pygame.transform.scale(Button, (ButtonDimx,ButtonDimy))
Mediu = pygame.image.load(os.path.join('images', 'mediu.png'))
Mediu = pygame.transform.scale(Mediu, (ButtonDimx,ButtonDimy))
Expert = pygame.image.load(os.path.join('images', 'expert.png'))
Expert = pygame.transform.scale(Expert, (ButtonDimx,ButtonDimy))
Text = pygame.image.load(os.path.join('images', 'text.png'))
Text = pygame.transform.scale(Text, (ButtonDimx,ButtonDimy))
Custom = pygame.image.load(os.path.join('images', 'custom.png'))
Custom = pygame.transform.scale(Custom, (ButtonDimx,ButtonDimy))
Explode = pygame.image.load(os.path.join('images', 'explode.png'))
Explode = pygame.transform.scale(Explode, (BoxD,BoxD))

Num.append(pygame.image.load(os.path.join('images', 'count0.png')))
Num[0] = pygame.transform.scale(Num[0], (NumDx,NumDy))
Num.append( pygame.image.load(os.path.join('images', 'count1.png')))
Num[1] = pygame.transform.scale(Num[1], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count2.png')))
Num[2] = pygame.transform.scale(Num[2], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count3.png')))
Num[3] = pygame.transform.scale(Num[3], (NumDx,NumDy))
Num.append( pygame.image.load(os.path.join('images', 'count4.png')))
Num[4] = pygame.transform.scale(Num[4], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count5.png')))
Num[5] = pygame.transform.scale(Num[5], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count6.png')))
Num[6] = pygame.transform.scale(Num[6], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count7.png')))
Num[7] = pygame.transform.scale(Num[7], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count8.png')))
Num[8] = pygame.transform.scale(Num[8], (NumDx,NumDy))
Num.append(pygame.image.load(os.path.join('images', 'count9.png')))
Num[9] = pygame.transform.scale(Num[9], (NumDx,NumDy))

Safe = pygame.image.load(os.path.join('images', 'safe.png'))
Safe = pygame.transform.scale(Safe, (BoxD,BoxD))
