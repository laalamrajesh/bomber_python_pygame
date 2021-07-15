import pygame
import random
import time
pygame.init()

width = 1000
height = 600
gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bomber")
icon = pygame.image.load("bombClear.png")
dOpen = pygame.image.load("doorOpen.png")
dClose = pygame.image.load("doorClose.png")
rock = pygame.image.load("rock.png")
man = pygame.image.load("man.png")
enemy = pygame.image.load("enemy.png")
pygame.display.set_icon(icon)
#color
white = (255,255,255)
black = (0,0,0)
green = (0,125,0)
red = (255,0,0)
mix = (125,125,125)
blue = (0,0,255)
yel = (255,0,150)
wt = (255,200,200)


sfont = pygame.font.SysFont("comicsansms",15)
msfont = pygame.font.SysFont("comicsansms",30)
mfont = pygame.font.SysFont("comicsansms",38)
lfont = pygame.font.SysFont("comicsansms",80)
clock = pygame.time.Clock()
speed = 8
enemySpeed = 10


def makeBomber(bomberList,blockSize):
  for xy in bomberList[:-1]:
    pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,50))
  xy=bomberList[-1]
  pygame.draw.rect(gameWindow,yel,(xy[0],xy[1],50,50))
  #gameWindow.blit(man,(xy[0],xy[1]))
  pygame.display.update()

def makeEnemy(blockSize):
  global enemyMove
  for index in range(len(enemyList)):
    enemyList[index][1]+=enemyMove[index]
    if enemyList[index][1] <0:
      enemyMove[index] = -enemyMove[index]
      enemyList[index][1]+=enemyMove[index]
    if enemyList[index][1]>height-blockSize:
      enemyMove[index] = -enemyMove[index]
      enemyList[index][1]+=enemyMove[index]
    #pygame.draw.rect(gameWindow,red,(enemyList[index][0],enemyList[index][1],50,50))
    gameWindow.blit(enemy,(enemyList[index][0],enemyList[index][1]))
    pygame.display.update()


def message(text,color,y_disp,size,wid,hei):
  if size == "small":
    testSurface = sfont.render(text,True,color)
  elif size == "medium":
    testSurface = mfont.render(text,True,color)
  elif size == "large":
    testSurface = lfont.render(text,True,color)
  elif size == "msmall":
    testSurface = msfont.render(text,True,color)
  textReact = testSurface.get_rect()
  textReact.center = (wid/2),(hei/2)+y_disp
  gameWindow.blit(testSurface,textReact)

def pause():
  paus = True
  while paus == True:
    gameWindow.fill(white)
    message("Paused!",blue,y_disp=-80,size="large",wid=width,hei=height)
    message("Press  C to continue (or) Q to quit!.",black,y_disp=60,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_c :
          paus = False
def setMode():
  global enemyMax
  intro = True
  while intro == True:
    gameWindow.fill(white)
    message(" click E to Easy ",red,y_disp=-120,size="medium",wid=width,hei=height)
    message(" In Easy mode you have to complete game with in 50 sec ",red,y_disp=-70,size="msmall",wid=width,hei=height)
    message(" click M to Medium",green,y_disp=-20,size="medium",wid=width,hei=height)
    message(" In Medium mode you have to complete game with in 75 sec ",green,y_disp=30,size="msmall",wid=width,hei=height)
    message(" click H to Hard ",blue,y_disp=80,size="medium",wid=width,hei=height)
    message(" In Hard mode you have to complete game with in 100 sec ",blue,y_disp=120,size="msmall",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
      	if event.key == pygame.K_e :
          enemyMax = 9
          playGame()
        elif event.key == pygame.K_m :
	  	  	enemyMax = 18
	  	  	playGame()
        elif event.key == pygame.K_h :
	  			enemyMax = 27
	  			playGame()

    
def GameOver(seconds,mes,siz):
  gameover = True
  while gameover is True:
    gameWindow.fill(white)
    if siz!="":
      message("Game Over!"+mes,blue,y_disp=-150,size="medium",wid=width,hei=height)
    else:
      message("Game Over!"+mes,blue,y_disp=-150,size="large",wid=width,hei=height)
    message("Score : "+str(score),green,y_disp=-40,size="large",wid=width,hei=height)
    message("Time : "+str(int(seconds))+" sec",green,y_disp=60,size="large",wid=width,hei=height)
    message("Press  N to New Game (or) Q to quit!.",black,y_disp=150,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_n :
          setMode()
          playGame()
def gameCompleted(seconds):
  gameover = True
  while gameover is True:
    gameWindow.fill(white)
    message("WOW CONGRATS!!!",blue,y_disp=-150,size="large",wid=width,hei=height)
    message("Score : "+str(score),green,y_disp=-40,size="large",wid=width,hei=height)
    message("Time : "+str(int(seconds))+" sec",green,y_disp=60,size="large",wid=width,hei=height)
    message("Press  N to New Game (or) Q to quit!.",black,y_disp=150,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_n :
          setMode()
          playGame()

def intro():
  intro = True
  while intro == True:
    gameWindow.fill(mix)
    message("Bomber Game!",green,y_disp=-175,size="large",wid=width,hei=height)
    message("1) Place bomb Smash enemy and get high score. ",blue,y_disp=-80,size="medium",wid=width,hei=height)
    message("2) Use arrow keys to move bomber.",blue,y_disp=-30,size="medium",wid=width,hei=height)
    message("3) Press B to put Bomb. And keep bomber away from bomb ",blue,y_disp=20,size="msmall",wid=width,hei=height)
    message("4) Warning!!! Don't allow bomber to touch enemy",blue,y_disp=70,size="medium",wid=width,hei=height)
    message("Press  C to continue (or) Q to quit! or p to pause.",black,y_disp=140,size="medium",wid=width,hei=height)
    message("By RajeshLalam",white,y_disp=190,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_c :
	  			setMode()
	  			playGame()
topDown = []
DownTop = []
enemyList = []
enemyMove = []
bomb = [-1,-1]
def makeWall():
  global topDown
  global DownTop
  for i in range(50,width,200):
    topDown.append([i,0])
  for i in range(150,width,200):
    DownTop.append([i,height])
def topDownWall():
  for xy in topDown:
    for i in range(xy[1],height-50,50):
      gameWindow.blit(rock,(xy[0],i))
    #pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,height-50))
def DownTopWall(blockSize):
  for xy in DownTop:
    for i in range(xy[1],49,-50):
      gameWindow.blit(rock,(xy[0],i))
  #pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,-height+51))

def checkDash(blockSize,sizeEnemy):
  global enemyList
  global score
  if bomb!=[-1,-1]:
    xAxis=bomb[0]
    yAxis=bomb[1]
    for ind  in range(len(enemyList)):
      xEnemy,yEnemy=enemyList[ind][0],enemyList[ind][1]
      if (xAxis==xEnemy) and ((yAxis >= yEnemy and yAxis <= yEnemy+sizeEnemy) or  (yAxis+blockSize >= yEnemy and yAxis+blockSize <= yEnemy+sizeEnemy)):
        del enemyList[ind]
        score+=100
        return 1
  return 0
score =0
enemyMax=10
def playGame():
  last_time = time.time()
  global speed
  global enemyList
  global bomb
  global score
  bomb=[-1,-1]
  count=-1
  score=0
  enemyList = []
  enemyCount = 1
  gameOver = False
  xAxis = 0
  yAxis = 0
  blockSize = 50
  xMove = 0
  yMove = 0
  sizeEnemy = 50
  bomberList = []
  snakeLength = 1
  gameWindow.fill(white)
  mod=50
  makeWall()
  while True:
    xEnemy = random.randrange(sizeEnemy,width-2*sizeEnemy)
    yEnemy = random.randrange(sizeEnemy+2*blockSize,height-2*sizeEnemy)
    xEnemy =(xEnemy+sizeEnemy-xEnemy%sizeEnemy)%width
    yEnemy = (yEnemy+sizeEnemy-yEnemy%sizeEnemy)%height
    
    flag=0
    for xy in topDown:
      if xEnemy == xy[0]  and yEnemy < height-50:
        flag=1
        break
    if flag==1:
      continue
    flag=0
    for xy in DownTop:
      if xEnemy == xy[0] and yEnemy >=50:
        flag=1
        break
    if flag==1:
      continue
    if [xEnemy,yEnemy] in enemyList:
      continue
    flag=0
    for xy in enemyList:
      if xEnemy == xy[0]:
        flag=1
        break
    if flag==1 and enemyCount<10:
      continue

    enemyCount+=1
    enemyList.append([xEnemy,yEnemy])
    ran = random.randint(0,1)
    if ran==0:
      enemyMove.append(-enemySpeed)
    else:
      enemyMove.append(enemySpeed)
    if enemyCount >enemyMax:
      break
    
    
  while gameOver is False :
    now = time.time() - last_time
    minute = now / 60
    seconds = now % 60
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
          xMove = -blockSize
          yMove = 0
          if count ==0:
            count=1
        elif event.key == pygame.K_RIGHT :
          xMove = blockSize
          yMove = 0
          if count ==0:
            count=1
        elif event.key == pygame.K_UP :
          yMove = -blockSize
          xMove = 0
          if count ==0:
            count=1
        elif event.key == pygame.K_DOWN :
          yMove = blockSize
          xMove = 0
          if count ==0:
            count=1
        elif event.key == pygame.K_p :
          pause()
        elif event.key == pygame.K_m :
          intro()
        elif event.key == pygame.K_b :
          bomb=[xAxis,yAxis]
          count=0
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT :
          xMove = 0
          yMove = 0
        elif event.key == pygame.K_RIGHT :
          xMove = 0
          yMove = 0
        elif event.key == pygame.K_UP :
          yMove = 0
          xMove = 0
        elif event.key == pygame.K_DOWN :
          yMove = 0
          xMove = 0
    xAxis+=xMove
    yAxis+=yMove
    if xAxis < 0 or xAxis > width-blockSize or yAxis < 0 or yAxis > height-blockSize:
      xAxis-=xMove
      yAxis-=yMove
      xMove=0
      yMove=0
      count=0
    newMove =[xAxis,yAxis]
    for xy in enemyList:
      xEnemy=xy[0]
      yEnemy=xy[1]
      
      if (xAxis==xEnemy) and ((yAxis >= yEnemy and yAxis <= yEnemy+sizeEnemy) or  (yAxis+blockSize >= yEnemy and yAxis+blockSize <= yEnemy+sizeEnemy)):
        gameOver=True
        break
    val = checkDash(blockSize,sizeEnemy)
    if val==1:
      pygame.draw.rect(gameWindow,blue,(bomb[0],bomb[1],sizeEnemy,sizeEnemy))
      bomb=[-1,-1]
    #print newMove,topDown,DownTop
    flag=0
    for xy in topDown:
      if xAxis == xy[0]  and yAxis < height-50:
        flag=1
        xAxis-=xMove
        yAxis-=yMove
        xMove=0
        yMove=0
        break
    if flag==1:
      count=0
      continue
    flag=0
    for xy in DownTop:
      if xAxis == xy[0] and yAxis >=50:
        flag=1
        xAxis-=xMove
        yAxis-=yMove
        xMove=0
        yMove=0
        break
    if flag==1:
      count=0
      continue
      
    gameWindow.fill(white)
    topDownWall()
    DownTopWall(blockSize)
    message("                                                                 Score : "+str(score) + "    Time : "+str(int(seconds))+"sec ",blue,y_disp=0,size="small",wid=100,hei=20)
    message("Press P to Pause game!.",wt,y_disp=-80,size="medium",wid=width,hei=height)
    message("Press M to Main Menu !.",wt,y_disp=120,size="medium",wid=width,hei=height)
    pygame.display.update()
    makeEnemy(blockSize)
    if bomb !=[-1,-1]:
      #pygame.draw.rect(gameWindow,blue,(bomb[0],bomb[1],sizeEnemy,sizeEnemy))
      gameWindow.blit(icon,(bomb[0],bomb[1]))
    gameWindow.blit(man,(xAxis,yAxis))
    if [xAxis,yAxis]==bomb and count==1:
      GameOver(seconds,",You Blasted","")
      pygame.display.update()
    if enemyMax ==9 and int(seconds)>50:
      GameOver(seconds,",Time Out","")
    elif enemyMax ==18 and int(seconds)>75:
      GameOver(seconds,",Time Out","")
    elif enemyMax ==27 and int(seconds)>100:
      GameOver(seconds,",Time Out","")

    #pygame.draw.rect(gameWindow,mix,(width-blockSize,0,sizeEnemy,sizeEnemy))
    if len(enemyList)!=0:
      gameWindow.blit(dClose,(width-blockSize,0))
    else:
      gameWindow.blit(dOpen,(width-blockSize,0))
    pygame.display.update()
    if newMove == [width-blockSize,0]:
        gameCompleted(seconds)
    #if xAxis == xEnemy and yAxis == yEnemy:
        #gameWindow.blit(icon,(xEnemy,yEnemy))
        #gameOver =True
    clock.tick(10)
  if gameOver ==True:
    GameOver(seconds,"You Killed by enemy","s")
intro()
pygame.quit()


