import pygame
pygame.init()

from vars import *
ss=square_size
screen=pygame.display.set_mode((square_size*8,square_size*8))

from pieces import *
key=pygame.key.get_pressed()
BLACK=(0,0,0)
WHITE = (255,255,255)
r1=rook(0*ss,7*ss,screen,True)
r2=rook(7*ss,7*ss,screen,True)
r3=rook(0*ss,0*ss,screen,False)
r4=rook(7*ss,0*ss,screen,False)
q1=queen(3*ss,7*ss,screen,True)
q2=queen(3*ss,0*ss,screen,False)
k1=king(4*ss,0*ss,screen,False)
k2=king(4*ss,7*ss,screen,True)
n1=knight(1*ss,0*ss,screen,False)
n2=knight(1*ss,7*ss,screen,True)
n3=knight(6*ss,0*ss,screen,False)
n4=knight(6*ss,7*ss,screen,True)
b1=bishop(2*ss,7*ss,screen,True)
b2=bishop(2*ss,0*ss,screen,False)
b3=bishop(5*ss,7*ss,screen,True)
b4=bishop(5*ss,0*ss,screen,False)
p1=pawn(0*ss,6*ss,screen,True)
p2=pawn(1*ss,6*ss,screen,True)
p3=pawn(2*ss,6*ss,screen,True)
p4=pawn(3*ss,6*ss,screen,True)
p5=pawn(4*ss,6*ss,screen,True)
p6=pawn(5*ss,6*ss,screen,True)
p7=pawn(6*ss,6*ss,screen,True)
p8=pawn(7*ss,6*ss,screen,True)
pb1=pawn(0*ss,1*ss,screen,False)
pb2=pawn(1*ss,1*ss,screen,False)
pb3=pawn(2*ss,1*ss,screen,False)
pb4=pawn(3*ss,1*ss,screen,False)
pb5=pawn(4*ss,1*ss,screen,False)
pb6=pawn(5*ss,1*ss,screen,False)
pb7=pawn(6*ss,1*ss,screen,False)
pb8=pawn(7*ss,1*ss,screen,False)
dummy=pawn(10*ss,1*ss,screen,False)

def castle():
    if key['k']:
        print("king side")
        if white_turn:
            k=k1
            r=r2
        else:
            k=k2
            r=r4
        for piece in pieces:
            if k.firstmove and r.firstmove:
                if piece.rules(k.rect.x,k.rect.y,pieces) and piece.restrict(k.rect.x,k.rect.y,pieces) and piece.white!=k.white:
                    cas=False
                elif piece.rules(k.rect.x+1*ss,k.rect.y,pieces) and piece.restrict(k.rect.x+1+ss,k.rect.y,pieces) and piece.white!=k.white:
                    cas=False
                elif piece.rules(k.rect.x+2+ss,k.rect.y,pieces) and piece.restrict(k.rect.x+2+ss,k.rect.y,pieces) and piece.white!=k.white:
                    cas=False
                elif piece.rect.x==k1.rect.x+ss or piece.rect.x==k1.rect.x+2*ss:
                    cas=False
                else:
                    k.rect.x=k.rect.x+2*ss
                    r.rect.x=r.rect.x-2*ss
        
        if white_turn:
            k1=k
            r2=r
        else:
            k2=k
            r4=r

pieces = [r1,r2,r3,r4,q1,q2,k1,k2,n1,n2,n3,n4,b1,b2,b3,b4,p1,p2,p3,p4,p5,p6,p7,p8,pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8]

temp_pieces = None

def drawBoard():
    screen.fill(WHITE)
    for i in range(8):
        if(i%2==1):
            for j in range(4):
                pygame.draw.rect(screen, BLACK, (j*2*square_size,i*square_size,square_size, square_size))
        else:
            for j in range(1,5):
                pygame.draw.rect(screen, BLACK, (j*2*square_size - square_size,i*square_size,square_size, square_size))

white_turn = True
checked = [False, None, None]
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
                #print("keydown")
                cas=True
                if event.key==pygame.K_k:
                    #print("kingside")
                    if white_turn:
                        k=k2
                        r=r2
                    else:
                        k=k1
                        r=r4
                    if k.firstmove and r.firstmove:
                        for piece in pieces:
                        
                            if piece.rules(k.rect.x,k.rect.y,pieces) and piece.restrict(k.rect.x,k.rect.y,pieces) and piece.white!=k.white:
                                #print("check")
                                cas=False
                            elif piece.rules(k.rect.x+1*ss,k.rect.y,pieces) and piece.restrict(k.rect.x+1+ss,k.rect.y,pieces) and piece.white!=k.white:
                                #print ("route check")
                                cas=False
                            elif piece.rules(k.rect.x+2+ss,k.rect.y,pieces) and piece.restrict(k.rect.x+2+ss,k.rect.y,pieces) and piece.white!=k.white:
                                #print("reach check")
                                cas=False
                            elif (piece.rect.x==k.rect.x+ss or piece.rect.x==k.rect.x+2*ss) and piece.rect.y==k.rect.y:
                                #print("obs")
                                #print(piece.rect.x)
                                cas=False
                        if cas:
                            k.rect.x=k.rect.x+2*ss
                            r.rect.x=r.rect.x-2*ss
                            k.firstmove=False
                            white_turn=not white_turn

                        if white_turn:
                            k2=k
                            r2=r
                            print(r2.rect.x/ss)
                        else:
                            k1=k
                            r4=r
                if event.key==pygame.K_q:
                    #print("kingside")
                    if white_turn:
                        k=k2
                        r=r1
                    else:
                        k=k1
                        r=r3
                    if k.firstmove and r.firstmove:
                        for piece in pieces:
                        
                            if piece.rules(k.rect.x,k.rect.y,pieces) and piece.restrict(k.rect.x,k.rect.y,pieces) and piece.white!=k.white:
                                #print("check")
                                cas=False
                            elif piece.rules(k.rect.x-1*ss,k.rect.y,pieces) and piece.restrict(k.rect.x-1*ss,k.rect.y,pieces) and piece.white!=k.white:
                                #print ("route check")
                                cas=False
                            elif piece.rules(k.rect.x-2*ss,k.rect.y,pieces) and piece.restrict(k.rect.x-2*ss,k.rect.y,pieces) and piece.white!=k.white:
                                #print("reach check")
                                cas=False
                            elif (piece.rect.x==k.rect.x-ss or piece.rect.x==k.rect.x-2*ss or piece.rect.x==k.rect.x-3*ss) and piece.rect.y==k.rect.y:
                                #print("obs")
                                #print(piece.rect.x)
                                cas=False
                        if cas:
                            k.rect.x=k.rect.x-2*ss
                            r.rect.x=r.rect.x+3*ss
                            k.firstmove=False
                            white_turn=not white_turn

                        if white_turn:
                            k2=k
                            r1=r
                            #print(r2.rect.x/ss)
                        else:
                            k1=k
                            r3=r


    for index in range(len(pieces)):
        if pieces[index] != None:
            try:
                piece_name = (str(pieces[index]).strip('<').split()[0].split('.')[1])
            except IndexError:
                piece_name = None
            if piece_name == 'pawn':
                if (pieces[index].rect.y == square_size*7) or (pieces[index].rect.y == 0):
                    temp = pieces[index]
                    pieces[index] = queen(temp.rect.x, temp.rect.y, screen, temp.white)
            if piece_name == 'king':
                if pieces[index].check_square(pieces)[0]:
                    pieces[index].attack = True
                    checked = [True, pieces[index].white, pieces[index].check_square(pieces)[1]]

    drawBoard()
    temp_pieces = pieces
    for i in range(len(pieces)):
        if None != pieces[i]:
            pieces[i].highlight()
            pieces[i].click(pieces, white_turn, checked)
            
            if pieces[i].turn:
                white_turn = not white_turn
                for x in range(len(pieces)):
                    if (i != x) and pieces[x] != None:
                        if (pieces[i].rect.y == pieces[x].rect.y) and (pieces[i].rect.x == pieces[x].rect.x):
                            pieces[x] = None
                            pieces[i].turn = False
            pieces[i].draw()

    for i in range(len(pieces)):
        try:
            if pieces[i] != None:
                pieces[i].turn = False
                piece_name = (str(pieces[i]).strip('<').split()[0].split('.')[1])
                if piece_name == 'king':
                    pieces[i].attack = False
            if pieces[i] == None:
                del pieces[i]
        except IndexError:
            continue
    checked = [False, None, None]
    
        

    pygame.display.update()
pygame.quit()