import pygame, sys
from time import *
from pygame.locals import *
from subprocess import call


def check_win_main(matrix):

    copy_matrix_x=[['s' for x in xrange(3)] for x in xrange(3)]
    copy_matrix_o=[['s' for x in xrange(3)] for x in xrange(3)]
    
    for x in xrange(3):
        for y in xrange(3):
            if(matrix[x][y]=='t'):
                copy_matrix_x[x][y]='s'
            else:
                copy_matrix_x[x][y]=matrix[x][y]

    for x in xrange(3):
        for y in xrange(3):
            if(matrix[x][y]=='t'):
                copy_matrix_o[x][y]='s'
            else:
                copy_matrix_o[x][y]=matrix[x][y]

#    if((check_winner(copy_matrix_o)=='o') and (check_winner(copy_matrix_x)=='x')):
#        return 's'

    if(check_winner(copy_matrix_o)=='o'):
        return 'o'

    elif(check_winner(copy_matrix_x)=='x'):
        return 'x'
    
    elif(True):
        flag=0

        for x in xrange(3):
            for y in xrange(3):
                if(matrix[x][y]=='s'):
                    flag=1
                    break;

        if(flag==0):
            return 't'

    return 's'
    

def check_winner(matrix):
    if(matrix[0][0]==matrix[0][1]==matrix[0][2]!='s'):
        return matrix[0][0]
    elif (matrix[1][0]==matrix[1][1]==matrix[1][2]!='s'):
        return matrix[1][0]
    elif (matrix[2][0]==matrix[2][1]==matrix[2][2]!='s'):
        return matrix[2][0]
    elif (matrix[0][0]==matrix[1][0]==matrix[2][0]!='s'):
        return matrix[0][0]
    elif (matrix[0][1]==matrix[1][1]==matrix[2][1]!='s'):
        return matrix[0][1]
    elif (matrix[0][2]==matrix[1][2]==matrix[2][2]!='s'):
        return matrix[0][2]
    elif (matrix[0][0]==matrix[1][1]==matrix[2][2]!='s'):
        return matrix[0][0]
    elif (matrix[0][2]==matrix[1][1]==matrix[2][0]!='s'):
        return matrix[0][2]
    else:
        for x in xrange(3):
            for y in xrange(3):
                if(matrix[x][y]=='s'):
                    return 's'
    return 't'

matrix=[[[['s','s','s'],['s','s','s'],['s','s','s']] for x in xrange(3)] for x in xrange(3)]
main_matrix=[['s','s','s'],['s','s','s'],['s','s','s']]

coord_of_cells = [[[[[0 for x in xrange(2)] for x in xrange(3)] for x in xrange(3)] for x in xrange(3)] for x in xrange(3)]

for x in xrange(3):
    for y in xrange(3):
        for i in xrange(3):
            for j in xrange(3):
                coord_of_cells[x][y][i][j]=(210*y+70*j,210*x+70*i)
                
bg="./img/grid.png"
xsimg="./img/xsmall.png"
osimg="./img/osmall.png"
xlimg="./img/xbig.png"
olimg="./img/obig.png"
timg="./img/tie.png"
psmall="./img/presentsmall.png"
pbig="./img/presentbig.png"
mus = "./img/music.ogg"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(mus)	
screen=pygame.display.set_mode((630,630),0,32)
pygame.display.set_caption("Tic-Tac-Toe")
pygame.mixer.music.play(-1, 0.0)
BackgroundimageObject=pygame.image.load(bg).convert()
XSMALLimageObject=pygame.image.load(xsimg).convert_alpha()
OSMALLimageObject=pygame.image.load(osimg).convert_alpha()
XLARGEimageObject=pygame.image.load(xlimg).convert_alpha()
OLARGEimageObject=pygame.image.load(olimg).convert_alpha()
TLARGEimageObject=pygame.image.load(timg).convert_alpha()
PRESENTSMALLimageObject=pygame.image.load(psmall).convert_alpha()
PRESENTLARGEimageObject=pygame.image.load(pbig).convert_alpha()


flg= 0
black = (0,0,0)
white = (255,255,255)
green = (0,150,0)
bright_green = (0,255,0)
red = (170,0,0)
bright_red = (255,0,0)
blue = (0,0,150)
bright_blue = (0,0,255)
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print click
   # if(msg == "2 Players"):
    #    flg = 2
    #if(msg == "1 Player"):
     #   flg = 1
      #  print flg
       # print "player 1"
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)



def game_intro1():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Tic Tac Toe", largeText)
        TextRect.center = ((630/2),(630/2))
        screen.blit(TextSurf, TextRect)


        button("1 Player", 125, 450, 100, 50, bright_green, green, game_intro2)
        button("2 Players", 400, 450, 100, 50, bright_blue, blue, game_ttt2)
        button("Quit", 260, 500, 100, 50, bright_red, red, game_quit)


        pygame.display.update()
        clock.tick(15)

def game_intro2():

    intro1 = True

    while intro1:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

        screen.fill(white)
        #largeText = pygame.font.Font('freesansbold.ttf',115)
        #TextSurf, TextRect = text_objects("Tic Tac Toe", largeText)
        #TextRect.center = ((630/2),(630/2))
        #screen.blit(TextSurf, TextRect)

        button("Easy", 270, 250, 100, 50, bright_green, green, game_ttte)
        button("Medium", 270, 315, 100, 50, bright_red, red, game_tttm)
        button("Hard", 270, 380, 100, 50, bright_blue, blue, game_ttth)


        pygame.display.update()
        clock.tick(15)

def game_quit():
    pygame.quit()
    sys.exit()

class Board(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,img):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.image = img
       self.rect = self.image.get_rect()

def game_ttte():
    player=1
    iprev=-1
    jprev=-1
    board = Board(BackgroundimageObject)
    board.rect= [0,0]
    all_sprite_list = pygame.sprite.OrderedUpdates()
#all_sprite_list.empty()
    all_sprite_list.add(board)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    call(["gcc","./alphabeta_easy.c","-o","./playmini_easy"])		#Compiles the program for different systems
    highg=0
    highlight = Board(PRESENTLARGEimageObject)
    highlight.rect= [0,0]
    all_sprite_list.add(highlight)
    all_sprite_list.draw(screen)
    highg=highlight
    pygame.display.flip()


    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
	    if event.type == pygame.KEYDOWN:
	    	if event.key == K_q:
		    pygame.quit()
	            sys.exit()

            
            if event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for x in xrange(3):
                    for y in xrange(3):
                        for i in xrange(3):
                            for j in xrange(3):
                                if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                    if (matrix[x][y][i][j]!='s'):
                                        continue

                                    elif((iprev==-1)and(jprev==-1)):
                                        if(main_matrix[x][y]=='s'):
                                            if(player%2==1):
                                                
                                                board = Board(XSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
    					    	player+=1
                                                matrix[x][y][i][j]='x'
                                                iprev=i
                                                jprev=j

                                            else:
                                                board = Board(OSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                                player+=1
                                                matrix[x][y][i][j]='o'
                                                iprev=i
                                                jprev=j
                                        else:
                                            continue
                                    elif((x==iprev)and(y==jprev)):
                                        if(player%2==1):
                                            board = Board(XSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='x'
                                            iprev=i
                                            jprev=j
                                            
                                        else:
                                            board = Board(OSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='o'
                                            iprev=i
                                            jprev=j

                                    else:
                                        continue

                                    if(check_winner(matrix[x][y])!='s'):
                                        if(check_winner(matrix[x][y])=='x'):
                                            board = Board(XLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='x'

                                        elif(check_winner(matrix[x][y])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0] 
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
                                            sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1

                                    #Finished one move
				    #print "v"
                                    # print flg 
                                    # print "v"
                                    all_sprite_list.remove(highlight)
                                    pygame.display.flip()

                                    fout=open("./data/matrixforai.txt","w")

                                    if (player%2 == 1):
                                        fout.write("x" + "\n")
                                    else:
                                        fout.write("O" + "\n")
                                        
                                    fout.write(str(iprev)+" "+str(jprev)+"\n")

                                    for var1 in range(3):
                                        for var2 in range(3):
                                            for var3 in range(3):
                                                for var4 in range(3):
                                                    if(matrix[var1][var3][var2][var4]=='s'):
                                                        fout.write("-")
                                                    elif(matrix[var1][var3][var2][var4]=='x'):
                                                        fout.write("X")
                                                    elif(matrix[var1][var3][var2][var4]=='o'):
                                                        fout.write("O")
                                            fout.write("\n")
                                    fout.write("\n")            
                                    fout.close()

                                    pygame.display.update()

                                    print "Computer's move is:"         
                                    call(["./playmini_easy"])

                                    fin=open("./data/aimove.txt","r")

                                    a=fin.read()

                                    print a
                                    a=a.split()

                                    fin.close()

                                    var1=int(a[0])
                                    var2=int(a[1])
                                    var3=int(a[2])
                                    var4=int(a[3])

                                    board = Board(OSMALLimageObject)
                                    board.rect= coord_of_cells[var1][var2][var3][var4]
                                    
                                    all_sprite_list.add(board)
                                    all_sprite_list.draw(screen)
                                    pygame.display.flip()
                                    player+=1
                                    matrix[var1][var2][var3][var4]='o'
                                    iprev=var3
                                    jprev=var4

                                    if(check_winner(matrix[var1][var2])!='s'):
                                        if(check_winner(matrix[var1][var2])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
    					    sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1
                                    
                                    if ((iprev==-1)and(jprev==-1)):
                                        highlight = Board(PRESENTLARGEimageObject)
                                        highg = highlight
                                        highlight.rect= [0,0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                    else:
                                        highlight = Board(PRESENTSMALLimageObject)
                                        highg = highlight
                                        highlight.rect= coord_of_cells[iprev][jprev][0][0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()

                                    
def game_tttm():
    player=1
    iprev=-1
    jprev=-1
    board = Board(BackgroundimageObject)
    board.rect= [0,0]
    all_sprite_list = pygame.sprite.OrderedUpdates()
    
    all_sprite_list.add(board)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    call(["gcc","./alphabeta_med.c","-o","./playmini_med"])     #Compiles the program for different systems
    highg=0
    highlight = Board(PRESENTLARGEimageObject)
    highlight.rect= [0,0]
    all_sprite_list.add(highlight)
    all_sprite_list.draw(screen)
    highg=highlight
    pygame.display.flip()


    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
    	    if event.type == pygame.KEYDOWN:
	    	if event.key == K_q:
		    pygame.quit()
		    sys.exit()

            if event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for x in xrange(3):
                    for y in xrange(3):
                        for i in xrange(3):
                            for j in xrange(3):
                                if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                    if (matrix[x][y][i][j]!='s'):
                                        continue

                                    elif((iprev==-1)and(jprev==-1)):
                                        if(main_matrix[x][y]=='s'):
                                            if(player%2==1):
                                                
                                                board = Board(XSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                		player+=1
                                                matrix[x][y][i][j]='x'
                                                iprev=i
                                                jprev=j

                                            else:
                                                board = Board(OSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                                player+=1
                                                matrix[x][y][i][j]='o'
                                                iprev=i
                                                jprev=j
                                        else:
                                            continue
                                    elif((x==iprev)and(y==jprev)):
                                        if(player%2==1):
                                            board = Board(XSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='x'
                                            iprev=i
                                            jprev=j
                                            
                                        else:
                                            board = Board(OSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='o'
                                            iprev=i
                                            jprev=j

                                    else:
                                        continue

                                    if(check_winner(matrix[x][y])!='s'):
                                        if(check_winner(matrix[x][y])=='x'):
                                            board = Board(XLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='x'

                                        elif(check_winner(matrix[x][y])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0] 
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
                                            sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1

                                    #Finished one move
# print "v"
#                                   print flg 
#                                   print "v"
                                    all_sprite_list.remove(highlight)
                                    pygame.display.flip()

                                    fout=open("./data/matrixforai.txt","w")

                                    if (player%2 == 1):
                                        fout.write("x" + "\n")
                                    else:
                                        fout.write("O" + "\n")
                                        
                                    fout.write(str(iprev)+" "+str(jprev)+"\n")

                                    for var1 in range(3):
                                        for var2 in range(3):
                                            for var3 in range(3):
                                                for var4 in range(3):
                                                    if(matrix[var1][var3][var2][var4]=='s'):
                                                        fout.write("-")
                                                    elif(matrix[var1][var3][var2][var4]=='x'):
                                                        fout.write("X")
                                                    elif(matrix[var1][var3][var2][var4]=='o'):
                                                        fout.write("O")
                                            fout.write("\n")
                                    fout.write("\n")            
                                    fout.close()

                                    pygame.display.update() 

                                    print "Computer's move is:"               
                                    call(["./playmini_med"])

                                    fin=open("./data/aimove.txt","r")

                                    a=fin.read()

                                    print a
                                    a=a.split()

                                    fin.close()

                                    var1=int(a[0])
                                    var2=int(a[1])
                                    var3=int(a[2])
                                    var4=int(a[3])

                                    board = Board(OSMALLimageObject)
                                    board.rect= coord_of_cells[var1][var2][var3][var4]
                                    
                                    all_sprite_list.add(board)
                                    all_sprite_list.draw(screen)
                                    pygame.display.flip()
                                    player+=1
                                    matrix[var1][var2][var3][var4]='o'
                                    iprev=var3
                                    jprev=var4

                                    if(check_winner(matrix[var1][var2])!='s'):
                                        if(check_winner(matrix[var1][var2])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
                            		    sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1
                                    
                                    if ((iprev==-1)and(jprev==-1)):
                                        highlight = Board(PRESENTLARGEimageObject)
                                        highg = highlight
                                        highlight.rect= [0,0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                    else:
                                        highlight = Board(PRESENTSMALLimageObject)
                                        highg = highlight
                                        highlight.rect= coord_of_cells[iprev][jprev][0][0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()


def game_ttth():
    player=1
    iprev=-1
    jprev=-1
    board = Board(BackgroundimageObject)
    board.rect= [0,0]
    all_sprite_list = pygame.sprite.OrderedUpdates()

    all_sprite_list.add(board)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    call(["gcc","./alphabeta.c","-o","./playmini"])     #Compiles the program for different systems
    highg=0
    highlight = Board(PRESENTLARGEimageObject)
    highlight.rect= [0,0]
    all_sprite_list.add(highlight)
    all_sprite_list.draw(screen)
    highg=highlight
    pygame.display.flip()


    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

	    if event.type == pygame.KEYDOWN:
	    	if event.key == K_q:
		    pygame.quit()
	            sys.exit()
            
            
            if event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for x in xrange(3):
                    for y in xrange(3):
                        for i in xrange(3):
                            for j in xrange(3):
                                if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                    if (matrix[x][y][i][j]!='s'):
                                        continue

                                    elif((iprev==-1)and(jprev==-1)):
                                        if(main_matrix[x][y]=='s'):
                                            if(player%2==1):
                                                
                                                board = Board(XSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                		player+=1
                                                matrix[x][y][i][j]='x'
                                                iprev=i
                                                jprev=j

                                            else:
                                                board = Board(OSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                                player+=1
                                                matrix[x][y][i][j]='o'
                                                iprev=i
                                                jprev=j
                                        else:
                                            continue
                                    elif((x==iprev)and(y==jprev)):
                                        if(player%2==1):
                                            board = Board(XSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='x'
                                            iprev=i
                                            jprev=j
                                            
                                        else:
                                            board = Board(OSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='o'
                                            iprev=i
                                            jprev=j

                                    else:
                                        continue

                                    if(check_winner(matrix[x][y])!='s'):
                                        if(check_winner(matrix[x][y])=='x'):
                                            board = Board(XLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='x'

                                        elif(check_winner(matrix[x][y])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0] 
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
                                            sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1

                                    #Finished one move
#print "v"
#                                   print flg 
#                                   print "v"
                                    all_sprite_list.remove(highlight)
                                    pygame.display.flip()

                                    fout=open("./data/matrixforai.txt","w")

                                    if (player%2 == 1):
                                        fout.write("x" + "\n")
                                    else:
                                        fout.write("O" + "\n")
                                        
                                    fout.write(str(iprev)+" "+str(jprev)+"\n")

                                    for var1 in range(3):
                                        for var2 in range(3):
                                            for var3 in range(3):
                                                for var4 in range(3):
                                                    if(matrix[var1][var3][var2][var4]=='s'):
                                                        fout.write("-")
                                                    elif(matrix[var1][var3][var2][var4]=='x'):
                                                        fout.write("X")
                                                    elif(matrix[var1][var3][var2][var4]=='o'):
                                                        fout.write("O")
                                            fout.write("\n")
                                    fout.write("\n")           
                                    fout.close()

                                    pygame.display.update() 

                                    print "Computer's move is:"                 
                                    call(["./playmini"])

                                    fin=open("./data/aimove.txt","r")

                                    a=fin.read()

                                    print a
                                    a=a.split()

                                    fin.close()

                                    var1=int(a[0])
                                    var2=int(a[1])
                                    var3=int(a[2])
                                    var4=int(a[3])

                                    board = Board(OSMALLimageObject)
                                    board.rect= coord_of_cells[var1][var2][var3][var4]
                                    
                                    all_sprite_list.add(board)
                                    all_sprite_list.draw(screen)
                                    pygame.display.flip()
                                    player+=1
                                    matrix[var1][var2][var3][var4]='o'
                                    iprev=var3
                                    jprev=var4

                                    if(check_winner(matrix[var1][var2])!='s'):
                                        if(check_winner(matrix[var1][var2])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[var1][var2][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[var1][var2]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
					    sleep(5)  
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1
                                    
                                    if ((iprev==-1)and(jprev==-1)):
                                        highlight = Board(PRESENTLARGEimageObject)
                                        highg = highlight
                                        highlight.rect= [0,0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()
                                    else:
                                        highlight = Board(PRESENTSMALLimageObject)
                                        highg = highlight
                                        highlight.rect= coord_of_cells[iprev][jprev][0][0]
                                        all_sprite_list.add(highlight)
                                        all_sprite_list.draw(screen)
                                        pygame.display.flip()

                                    


def game_ttt2():
    player=1
    iprev=-1
    jprev=-1
    board = Board(BackgroundimageObject)
    board.rect= [0,0]
    all_sprite_list = pygame.sprite.OrderedUpdates() 
#all_sprite_list.empty()
    all_sprite_list.add(board)
    all_sprite_list.draw(screen)
    pygame.display.flip()
   # call(["gcc","./alphabeta.c","-o","./playmini"])     #Compiles the program for different systems
    highg=0
    highlight = Board(PRESENTLARGEimageObject)
    highlight.rect= [0,0]
    all_sprite_list.add(highlight)
    all_sprite_list.draw(screen)
    highg=highlight
    pygame.display.flip()


    while True:

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
	    	if event.key == K_q:
		    pygame.quit()
	            sys.exit()

            if event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                for x in xrange(3):
                    for y in xrange(3):
                        for i in xrange(3):
                            for j in xrange(3):
                                if ((pos[0]>coord_of_cells[x][y][i][j][0])and(pos[0]<coord_of_cells[x][y][i][j][0]+70)and(pos[1]>coord_of_cells[x][y][i][j][1])and(pos[1]<coord_of_cells[x][y][i][j][1]+70)):

                                    if (matrix[x][y][i][j]!='s'):
                                        continue

                                    elif((iprev==-1)and(jprev==-1)):
                                        if(main_matrix[x][y]=='s'):
                                            if(player%2==1):
                                                
                                                board = Board(XSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                		player+=1
                                                matrix[x][y][i][j]='x'
                                                iprev=i
                                                jprev=j

                                            else:
                                                board = Board(OSMALLimageObject)
                                                board.rect= coord_of_cells[x][y][i][j]
                                                
                                                all_sprite_list.add(board)
                                                all_sprite_list.draw(screen)
                                                pygame.display.flip()
                                                player+=1
                                                matrix[x][y][i][j]='o'
                                                iprev=i
                                                jprev=j
                                        else:
                                            continue
                                    elif((x==iprev)and(y==jprev)):
                                        if(player%2==1):
                                            board = Board(XSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='x'
                                            iprev=i
                                            jprev=j
                                            
                                        else:
                                            board = Board(OSMALLimageObject)
                                            board.rect= coord_of_cells[x][y][i][j]
                                            
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            player+=1
                                            matrix[x][y][i][j]='o'
                                            iprev=i
                                            jprev=j

                                    else:
                                        continue

                                    if(check_winner(matrix[x][y])!='s'):
                                        if(check_winner(matrix[x][y])=='x'):
                                            board = Board(XLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='x'

                                        elif(check_winner(matrix[x][y])=='o'):
                                            board = Board(OLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0]
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='o'

                                        else:
                                            board = Board(TLARGEimageObject)
                                            board.rect= coord_of_cells[x][y][0][0] 
                                            all_sprite_list.add(board)
                                            all_sprite_list.draw(screen)
                                            pygame.display.flip()
                                            main_matrix[x][y]='t'

                                        if(check_win_main(main_matrix)!='s'):

                                            if(check_win_main(main_matrix)!='t'):
                                                print "The winner is "+ check_win_main(main_matrix)
                                            else:
                                                print "The game is a tie"
                                            sleep(5)
                                            pygame.quit()
                                            sys.exit()

                                    if(main_matrix[iprev][jprev]!='s'):
                                        iprev=-1
                                        jprev=-1

				    all_sprite_list.remove(highlight)
				    pygame.display.flip()

				    if ((iprev==-1)and(jprev==-1)):
				        highlight = Board(PRESENTLARGEimageObject)
				        highg = highlight
				        highlight.rec = [0,0]
				        all_sprite_list.add(highlight)
				        all_sprite_list.draw(screen)
				        pygame.display.flip()

				    else:
				        highlight = Board(PRESENTSMALLimageObject)
	                                highg = highlight
					highlight.rect = coord_of_cells[iprev][jprev][0][0]
					all_sprite_list.add(highlight)
	                                all_sprite_list.draw(screen)
	                                pygame.display.flip()





game_intro1()
