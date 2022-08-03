import pygame
import random

pygame.init()

#-------------------WELCOME----------------------------

#game = False
#game_over = False

#while game==False:
welcome = pygame.display.set_mode((500,540))
pygame.display.set_caption("SDD Assignment 2")
startGameImage = pygame.image.load('Start Game.png')
text_colour = (255,255,255)
button_colour = (0,68,185)
button_over_colour = (30,30,30)
button_width = 125
button_height:int = 50

button_rect = [(welcome.get_width()-button_width)/2,(welcome.get_height()-button_height)/2+50,button_width,button_height]

button_font = pygame.font.SysFont("Verdana",20)
button_text = button_font.render("Start Game", True, text_colour)
gameName = button_font.render("SDD Assignment", True, text_colour)


x,y = (0,0)

game_over = False
mainGame = False
Ship = False

while not game_over and not mainGame:
    welcome.blit(startGameImage,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True


#Mousebuttondown
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if (button_rect[0]<= x <= button_rect[0]+button_rect[2] and button_rect[1]<= y<=button_rect[1]+button_rect[3]):
                mainGame = True
#Mousemotion----------
        if event.type==pygame.MOUSEMOTION:
            x,y = event.pos
    if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
        pygame.draw.rect(welcome, button_over_colour, button_rect)

    else:
        pygame.draw.rect(welcome, button_colour, button_rect)

    welcome.blit(button_text, (button_rect[0] + (button_width - button_text.get_width()) / 2,
                              button_rect[1] + (button_height / 2 - button_text.get_height() / 2)))
    welcome.blit(gameName, ((welcome.get_width() - gameName.get_width())/2, (welcome.get_height()-gameName.get_height())/2-50))

    pygame.display.update()


#------------------WIN----------------

#while game:
win = pygame.display.set_mode((500, 279))
pygame.display.set_caption("SDD Assignment 2")

x = 50
y = 50
MenuHeight = 30
MenuWidth = 30
Menu_Rect = [((win.get_width()-MenuWidth)-20),20,MenuWidth,MenuHeight]
#PlayerWidth = 40
#PlayerHeight = 60
#PlayerRect = (x,y,PlayerWidth,PlayerHeight)
x3 = 0
y3 = 0
vel = 5
isJump = False
jumpCount = 10
Item1XList = []
Item1YList = []
Item2XList = []
Item2YList = []
Item3XList = []
Item3YList = []
Item1RectList = []
Item2RectList = []
Item3RectList = []
inventoryItem1List = []
inventoryItem2List = []
inventoryItem3List = []
Inventory1 = []
Inventory2 = []
Inventory3 = []
playerWidth = (pygame.image.load('Charactere_Idle_Left_0.png')).get_width()*5
playerHeight = (pygame.image.load('Charactere_Idle_Left_0.png')).get_height()*5
walkRight = [pygame.image.load('Charater_Walk_Right_0.png'), pygame.image.load('Charater_Walk_Right_1.png'), pygame.image.load('Charater_Walk_Right_2.png'), pygame.image.load('Charater_Walk_Right_3.png'), pygame.image.load('Charater_Walk_Right_4.png'), pygame.image.load('Charater_Walk_Right_5.png'), pygame.image.load('Charater_Walk_Right_6.png'), pygame.image.load('Charater_Walk_Right_7.png')]
walkLeft = [pygame.image.load('Character_Walk_Left_0.png'), pygame.image.load('Character_Walk_Left_1.png'), pygame.image.load('Character_Walk_Left_2.png'), pygame.image.load('Character_Walk_Left_3.png'), pygame.image.load('Character_Walk_Left_4.png'), pygame.image.load('Character_Walk_Left_5.png'), pygame.image.load('Character_Walk_Left_6.png'), pygame.image.load('Character_Walk_Left_7.png')]
#charLeft = [pygame.image.load('Charactere_Idle_Left_0.png'),pygame.image.load('Character_Idle_Left_1.png'), pygame.image.load('Character_Idle_Left_2.png'), pygame.image.load('Character_Idle_Left_3.png')]
#charRight = [pygame.image.load('Character_Idle_Right_0.png'),pygame.image.load('Character_Idle_Right_1.png'), pygame.image.load('Character_Idle_Right_2.png'), pygame.image.load('Character_Idle_Right_3.png')]
jumpRight = [pygame.image.load('Character_Jump_Right_0.png'), pygame.image.load('Character_Jump_Right_1.png'), pygame.image.load('Character_Jump_Right_2.png')]
jumpLeft = [pygame.image.load('Character_Jump_Left_0.png'), pygame.image.load('Character_Jump_Left_1.png'), pygame.image.load('Character_Jump_Left_2.png')]
interiorBackground = pygame.image.load('Inside.gif')
sceneryBackground = pygame.image.load('Scenery.gif')
Gem_Green = pygame.image.load("Gem_Green.png")
Gem_Purple = pygame.image.load("Gem_Purple_2.png")
Gem_Blue = pygame.image.load("Gem_Dark_Blue.png")
for r in range(len(walkRight)):
    walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
for r in range(len(walkLeft)):
    walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

man = player(200, 410, playerWidth,playerHeight)


update = False
blueGem = False
loadBlueGem = True
amount1 = 0
a1 = 0
n1 = 0
amount2 = 0
a2 = 0
n2 = 0
amount3 = 0
a3 = 0
n3 = 0
End = False

clock = pygame.time.Clock()

Jump = False
Forest = False
x4 = 0
y4 = 0
Home = True
Tutorial = True
Tutorial1 = True
Tutorial2 = False
Tutorial3 = False
Tutorial4 = False
Tutorial5 = False
TutorialFont = pygame.font.SysFont("Verdana",15)
Tutorial1Text = TutorialFont.render("Press Left and Right Keys to move, Press the Up Key to jump", True, text_colour)
Tutorial2Text = TutorialFont.render("Move to the right to go outside", True, text_colour)
Tutorial3Text = TutorialFont.render("Collect 2 purple and 2 green gems", True, text_colour)
Tutorial4Text = TutorialFont.render("Take them back home with you", True, text_colour)
Tutorial5Text = TutorialFont.render("Go back out and collect 3 more of each", True, text_colour)
Quest1Text = TutorialFont.render("Collect 10 purple and 10 green gems", True, text_colour)
Quest2Text = TutorialFont.render("Collect 10 purple and 15 green gems", True, text_colour)
Quest3Text = TutorialFont.render("Collect 1 blue gem", True, text_colour)
TutorialBox = ((500-(Tutorial1Text.get_width()+10))/2,30,Tutorial1Text.get_width()+10,40)
blueGemX = 0
blueGemY = 0
q1 = 2
q2 = 2
q3 = 2
quest1 = True
quest2 = False
quest3 = False



#def endGame():

while Tutorial:
    while Home and not End and not Forest:
        win = pygame.display.set_mode((500, 279))  # 500,279
        win.blit(interiorBackground, (0, 0))
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                Tutorial = False
                Home = False

            #if event.type == pygame.MOUSEBUTTONDOWN:
             #   x2, y2 = event.pos
              #  if (Menu_Rect[0] <= x2 <= Menu_Rect[0] + Menu_Rect[2] and Menu_Rect[1] <= y2 <= Menu_Rect[1] +
               #         Menu_Rect[3]):
                #    Forest = True
            # Mousemotion----------
            #if event.type == pygame.MOUSEMOTION:
             #   x2, y2 = event.pos
              #  if (Menu_Rect[0] <= x2 <= Menu_Rect[0] + Menu_Rect[2] and Menu_Rect[1] <= y2 <= Menu_Rect[1] +
               # Menu_Rect[3]):
                #    pygame.draw.rect(win, button_over_colour, Menu_Rect)

                #else:
                 #   pygame.draw.rect(win,button_colour, Menu_Rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            man.x -= vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            man.x += vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not (man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if not keys[pygame.K_UP]:
            man.y += vel^2

        #if man.x==0:
         #   Ship = True
          #  Home = False

        if man.y>(win.get_height()-playerHeight):
            man.y = win.get_height()-playerHeight
        if man.x<0:
            man.x = 0
        if man.x>(win.get_width()-playerWidth):
            if keys[pygame.K_RIGHT]:
                Forest = True
                Home = False
            #man.x = win.get_width()-playerWidth

        if Tutorial1:
            pygame.draw.rect(win,(0,0,0),TutorialBox)
            win.blit(Tutorial1Text, (250 - (Tutorial1Text.get_width() / 2),0+(Tutorial1Text.get_height())+20))
            if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                Tutorial1 = False
                Tutorial2 = True
        if Tutorial2:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Tutorial2Text, (250 - (Tutorial2Text.get_width() / 2), 0 + (Tutorial2Text.get_height()) + 20))
            if man.x>(win.get_width()-playerWidth):
                if keys[pygame.K_RIGHT]:
                    Tutorial2 = False
                    Tutorial3 = True
        if Tutorial5:
            q1 = 3
            q2 = 3
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Tutorial5Text, (250 - (Tutorial5Text.get_width() / 2), 0 + (Tutorial5Text.get_height()) + 20))
            if man.x==(win.get_width()-playerWidth)+50:
                if keys[pygame.K_RIGHT]:
                    Tutorial5 = False

        while len(inventoryItem1List) > 0:
            p1 = inventoryItem1List.pop(0)
            Inventory1.append(p1)

        while len(inventoryItem2List) > 0:
            p2 = inventoryItem2List.pop(0)
            Inventory2.append(p2)

        for r in range(len(walkRight)):
            walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
        for r in range(len(walkLeft)):
            walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))
        man.draw(win)
        pygame.display.update()
        if len(Inventory1) == 5 and len(Inventory2) == 5:
            End = True
            Home = False

    #-----------------SHIP----------------------------------

    #(while Ship and not Home and not Forest:
        #ship = pygame.display.set_mode((500, 500))

        #for event in pygame.event.get():
         #   if event.type == pygame.QUIT:
          #      mainGame = False
           #     Ship = False

#        ship.fill((0,50,80))
 #       pygame.display.update())

    while Forest and not End:
        Clock = pygame.time.get_ticks()
        forest = pygame.display.set_mode((500,450))
        InventoryFont = pygame.font.SysFont("Verdana", 10)
        Item1Score = InventoryFont.render("Green = "+str(len(inventoryItem1List))+"/"+str(q1), True, text_colour)
        Item2Score = InventoryFont.render("Purple = " + str(len(inventoryItem2List)) + "/"+str(q2), True, text_colour)

        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                Tutorial = False
                Forest = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            man.x -= vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            man.x += vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not (man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if not keys[pygame.K_UP]:
            man.y += vel^2

        if man.x == 0:
            if keys[pygame.K_LEFT]:
                Home = True
                man.x = win.get_width() - playerWidth
                Forest = False

        if man.y > forest.get_height()-playerHeight:
            man.y = forest.get_height()-playerHeight
        if man.x<0:
            man.x = 0
        if man.x > (forest.get_width()-playerWidth):
            man.x = forest.get_width()-playerWidth

        class Item:
            def __init__(self, width, height, value):
                self.value = value
                self.width = width
                self.height = height


        item1 = Item(40, 40, "item1")
        item2 = Item(40, 40, "item2")
        item3 = Item(40, 40, "item3")

        # ----------create item---------------
        # Item1XList = []
        # Item1YList = []
        # Item1RectList = []
        # Item1RectDrawList = []
        # amount1 = 0
        # a1 = 0
        # n = 0
        #update = False
        while Clock % 30000 == 0 and not update:
            update = True
        while update:
            amount1 += random.randint(0, 5)
            amount2 +=random.randint(0,5)
            while a1 < amount1:
                x3 = random.randint(0, forest.get_width()-item1.width)
                y3 = random.randint(250, forest.get_height()-item1.height)
                Item1XList.append(x3)
                Item1YList.append(y3)
                a1 += 1

                Item1RectList.append((Item1XList[n1], Item1YList[n1]))
                n1 += 1

            while a2 < amount2:
                x3 = random.randint(0, forest.get_width()-item2.width)
                y3 = random.randint(250, forest.get_height()-item2.height)
                Item2XList.append(x3)
                Item2YList.append(y3)
                a2 += 1

                Item2RectList.append((Item2XList[n2], Item2YList[n2]))
                n2 += 1
            update = False


        for item in Item1XList[:]:
            if len(inventoryItem1List)<q1 and (man.x<=item<=(playerWidth+man.x) or man.x<=(item+item1.width)<=(playerWidth+man.x)):
                v = Item1XList.index(item)
                if man.y<=Item1YList[v]<=(playerHeight+man.y) or man.y<=(Item1YList[v]+item1.height)<=(playerHeight+man.y):
                    Item1RectList.pop(v)
                    Item1YList.pop(v)
                    Item1XList.pop(v)
                    inventoryItem1List.append("item1")
                    n1-=1
                    a1-=1
                    amount1-=1
        for item in Item2XList[:]:
            if len(inventoryItem2List)<q2 and (man.x<=item<=(playerWidth+man.x) or man.x<=(item+item2.width)<=(playerWidth+man.x)):
                v = Item2XList.index(item)
                if man.y<=Item2YList[v]<=(playerHeight+man.y) or man.y<=(Item2YList[v]+item1.height)<=(playerHeight*2+man.y):
                    Item2RectList.pop(v)
                    Item2YList.pop(v)
                    Item2XList.pop(v)
                    inventoryItem2List.append("item2")
                    n2-=1
                    a2-=1
                    amount2-=1


        if y == (500-playerHeight) and x == 0:
            Home = True
            Forest = False


        forest.blit(sceneryBackground,(0,0))
        if Tutorial3:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            forest.blit(Tutorial3Text, (250 - (Tutorial3Text.get_width() / 2), 0 + (Tutorial3Text.get_height()) + 20))
            if len(inventoryItem1List)>=2 and len(inventoryItem2List)>=2:
                Tutorial3 = False
                Tutorial4 = True
        if Tutorial4:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            forest.blit(Tutorial4Text, (250 - (Tutorial4Text.get_width() / 2), 0 + (Tutorial4Text.get_height()) + 20))
            if not Forest:
                    Tutorial5 = True
                    Tutorial4 = False

        for i in Item1RectList:
            forest.blit(Gem_Green, i)
        for ii in Item2RectList:
            forest.blit(Gem_Purple, ii)

        forest.blit(Item1Score,(60,10))
        forest.blit(Item2Score, (140, 10))

        man.draw(forest)
        pygame.display.update()

    while End and not Forest and not Home:
        Countdown = pygame.time.get_ticks()
        endGameScreen = pygame.display.set_mode((500, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                Tutorial = False
                End = False
        endGameFont = pygame.font.SysFont("Verdana", 20)
        endGameText = endGameFont.render("You Completed the Tutorial!", True, text_colour)
        endGameScreen.fill((5,5,5))
        endGameScreen.blit(endGameText,(250-(endGameText.get_width()/2),240))
        pygame.display.update()
        if Countdown %  500 == 0:
            inventoryItem1List.clear()
            inventoryItem2List.clear()
            Item1XList.clear()
            Item1YList.clear()
            Item2YList.clear()
            Item2XList.clear()
            Item1RectList.clear()
            Item2RectList.clear()
            Inventory1.clear()
            Inventory2.clear()
            update = False
            n1 = 0
            a1 = 0
            amount1 = 0
            n2 = 0
            a2 = 0
            amount2 = 0
            Home = True
            mainGame = True
            Tutorial = False
            End = False

while mainGame:
    while Home and not End and not Forest:
        win = pygame.display.set_mode((500, 279))  # 500,279
        win.blit(interiorBackground, (0, 0))
        clock.tick(27)
        if quest1:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Quest1Text, (250 - (Quest1Text.get_width() / 2), 0 + (Quest1Text.get_height()) + 20))

            q1 = 5
            q2 = 5
            if len(Inventory1) >= 10 and len(Inventory1) >= 10:
                quest1 = False
                quest2 = True
                Inventory1.clear()
                Inventory2.clear()
        if quest2:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Quest2Text, (250 - (Quest2Text.get_width() / 2), 0 + (Quest2Text.get_height()) + 20))

            q1 = 8
            q2 = 8
            if len(Inventory1) >= 10 and len(Inventory1) >= 15:
                quest2 = False
                quest3 = True
                Inventory1.clear()
                Inventory2.clear()

        if quest3:
            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Quest3Text, (250 - (Quest3Text.get_width() / 2), 0 + (Quest3Text.get_height()) + 20))

            q1 = 8
            q2 = 8
            q3 = 1
            Item2Score = InventoryFont.render("Purple = " + str(len(inventoryItem2List)) + "/" + str(q2), True,
                                                  text_colour)
            if len(Inventory3) == 1:
                quest3 = False
                Home = False
                Forest = False
                End = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                Home = False

            #if event.type == pygame.MOUSEBUTTONDOWN:
             #   x2, y2 = event.pos
              #  if (Menu_Rect[0] <= x2 <= Menu_Rect[0] + Menu_Rect[2] and Menu_Rect[1] <= y2 <= Menu_Rect[1] +
               #         Menu_Rect[3]):
                #    Forest = True
            # Mousemotion----------
            #if event.type == pygame.MOUSEMOTION:
             #   x2, y2 = event.pos
              #  if (Menu_Rect[0] <= x2 <= Menu_Rect[0] + Menu_Rect[2] and Menu_Rect[1] <= y2 <= Menu_Rect[1] +
               # Menu_Rect[3]):
                #    pygame.draw.rect(win, button_over_colour, Menu_Rect)

                #else:
                 #   pygame.draw.rect(win,button_colour, Menu_Rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            man.x -= vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            man.x += vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not (man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if not keys[pygame.K_UP]:
            man.y += vel^2

        #if man.x==0:
         #   Ship = True
          #  Home = False

        if man.y>(win.get_height()-playerHeight):
            man.y = win.get_height()-playerHeight
        if man.x<0:
            man.x = 0
        if man.x>(win.get_width()-playerWidth):
            if keys[pygame.K_RIGHT]:
                Forest = True
                Home = False
            #man.x = win.get_width()-playerWidth

            pygame.draw.rect(win, (0, 0, 0), TutorialBox)
            win.blit(Tutorial5Text, (250 - (Tutorial5Text.get_width() / 2), 0 + (Tutorial5Text.get_height()) + 20))
            if man.x==(win.get_width()-playerWidth)+50:
                if keys[pygame.K_RIGHT]:
                    Tutorial5 = False

        while len(inventoryItem1List) > 0:
            p1 = inventoryItem1List.pop(0)
            Inventory1.append(p1)

        while len(inventoryItem2List) > 0:
            p2 = inventoryItem2List.pop(0)
            Inventory2.append(p2)

        while len(inventoryItem3List) > 0:
            p3 = inventoryItem3List.pop(0)
            Inventory3.append(p3)

        for r in range(len(walkRight)):
            walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth, playerHeight))
        for r in range(len(walkLeft)):
            walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth, playerHeight))
        man.draw(win)
        pygame.display.update()

    #-----------------SHIP----------------------------------

    #(while Ship and not Home and not Forest:
        #ship = pygame.display.set_mode((500, 500))

        #for event in pygame.event.get():
         #   if event.type == pygame.QUIT:
          #      mainGame = False
           #     Ship = False

#        ship.fill((0,50,80))
 #       pygame.display.update())

    while Forest and not End:

        Clock = pygame.time.get_ticks()
        forest = pygame.display.set_mode((500,450))
        InventoryFont = pygame.font.SysFont("Verdana", 10)
        Item1Score = InventoryFont.render("Green = "+str(len(inventoryItem1List))+"/"+str(q1), True, text_colour)
        Item2Score = InventoryFont.render("Purple = " + str(len(inventoryItem2List)) + "/"+str(q2), True, text_colour)
        Item3Score = InventoryFont.render("Blue = " + str(len(inventoryItem3List)) + "/" + str(q3), True,
                                          text_colour)

        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                Forest = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            man.x -= vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            man.x += vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not (man.isJump):
            if keys[pygame.K_UP]:
                man.isJump = True
                man.right = False
                man.left = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        if not keys[pygame.K_UP]:
            man.y += vel^2

        if man.x == 0:
            if keys[pygame.K_LEFT]:
                Home = True
                man.x = win.get_width() - playerWidth
                Forest = False

        if man.y > forest.get_height()-playerHeight:
            man.y = forest.get_height()-playerHeight
        if man.x<0:
            man.x = 0
        if man.x > (forest.get_width()-playerWidth):
            man.x = forest.get_width()-playerWidth

        class Item:
            def __init__(self, width, height, value):
                self.value = value
                self.width = width
                self.height = height


        item1 = Item(40, 40, "item1")
        item2 = Item(40, 40, "item2")
        item3 = Item(40, 40, "item3")

        # ----------create item---------------
        # Item1XList = []
        # Item1YList = []
        # Item1RectList = []
        # Item1RectDrawList = []
        # amount1 = 0
        # a1 = 0
        # n = 0
        #update = False
        while Clock % 500 == 0 and not update:
            update = True
        while update:
            amount1 += random.randint(0, 5)
            amount2 +=random.randint(0,5)
            while a1 < amount1:
                x3 = random.randint(0, forest.get_width()-item1.width)
                y3 = random.randint(250, forest.get_height()-item1.height)
                Item1XList.append(x3)
                Item1YList.append(y3)
                a1 += 1

                Item1RectList.append((Item1XList[n1], Item1YList[n1]))
                n1 += 1

            while a2 < amount2:
                x3 = random.randint(0, forest.get_width()-item2.width)
                y3 = random.randint(250, forest.get_height()-item2.height)
                Item2XList.append(x3)
                Item2YList.append(y3)
                a2 += 1

                Item2RectList.append((Item2XList[n2], Item2YList[n2]))
                n2 += 1
            update = False

        while quest3 and not blueGem and len(Item3RectList)<1 and loadBlueGem:
            blueGem = True
        while blueGem:
            blueGemX = random.randint(0, forest.get_width() - item1.width)
            blueGemY = random.randint(250, forest.get_height() - item1.height)

            Item3RectList.append((blueGemX, blueGemY))
            blueGem = False

        for item in Item1XList[:]:
            if len(inventoryItem1List)<q1 and (man.x<=item<=(playerWidth+man.x) or man.x<=(item+item1.width)<=(playerWidth+man.x)):
                v = Item1XList.index(item)
                if man.y<=Item1YList[v]<=(playerHeight+man.y) or man.y<=(Item1YList[v]+item1.height)<=(playerHeight+man.y):
                    Item1RectList.pop(v)
                    Item1YList.pop(v)
                    Item1XList.pop(v)
                    inventoryItem1List.append("item1")
                    n1-=1
                    a1-=1
                    amount1-=1
        for item in Item2XList[:]:
            if len(inventoryItem2List)<q2 and (man.x<=item<=(playerWidth+man.x) or man.x<=(item+item2.width)<=(playerWidth+man.x)):
                v = Item2XList.index(item)
                if man.y<=Item2YList[v]<=(playerHeight+man.y) or man.y<=(Item2YList[v]+item1.height)<=(playerHeight*2+man.y):
                    Item2RectList.pop(v)
                    Item2YList.pop(v)
                    Item2XList.pop(v)
                    inventoryItem2List.append("item2")
                    n2-=1
                    a2-=1
                    amount2-=1
        #listLength = len(Item1RectList)
        # d = 0
        # while d < listLength:
        # Item1RectDrawList.append((pygame.draw.rect(forest,item1.colour,Item1RectList[d])))
        # d+=1
        if (((man.x <= blueGemX <= (playerWidth + man.x) or man.x <= blueGemX + item3.width) <= (playerWidth + man.x))) and ((man.y <= blueGemY <= (playerHeight + man.y) or man.y <= (blueGemY + item3.height) <= (playerHeight + man.y))):
                    blueGemX = 0
                    blueGemY = 0
                    Item3RectList.pop(0)
                    inventoryItem3List.append("item3")
                    loadBlueGem = False

        if y == (500-playerHeight) and x == 0:
            Home = True
            Forest = False



                #update = False
        #for r in range(len(walkRight)):
         #   walkRight[r] = pygame.transform.scale(walkRight[r], (playerWidth*2, playerHeight*2))
        #for r in range(len(walkLeft)):
         #   walkLeft[r] = pygame.transform.scale(walkLeft[r], (playerWidth*2, playerHeight*2))
        forest.blit(sceneryBackground,(0,0))

        for i in Item1RectList:
            forest.blit(Gem_Green, i)
        for ii in Item2RectList:
            forest.blit(Gem_Purple, ii)
        for iii in Item3RectList:
            forest.blit(Gem_Blue,iii)

        forest.blit(Item1Score,(60,10))
        forest.blit(Item2Score, (140, 10))
        if quest3:
            forest.blit(Item3Score, (220, 10))

        man.draw(forest)
        pygame.display.update()

    while End and not Forest and not Home:
        Countdown = pygame.time.get_ticks()
        endGameScreen = pygame.display.set_mode((500, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainGame = False
                End = False
        endGameFont = pygame.font.SysFont("Verdana", 20)
        endGameText = endGameFont.render("You Completed All Quests!", True, text_colour)
        endGameScreen.fill((5,5,5))
        endGameScreen.blit(endGameText,(250-(endGameText.get_width()/2),240))
        pygame.display.update()


pygame.quit()