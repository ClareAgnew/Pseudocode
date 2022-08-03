#1. Create List of random items----------------------------------
while a < amount:
    x3 = random.randint(0, forest.get_width() - item.width)
    y3 = random.randint(250, forest.get_height() - item.height)
    ItemXList.append(x3)
    ItemYList.append(y3)
    a += 1

    ItemRectList.append((ItemXList[n], ItemYList[n]))
    n += 1



#2. collision/pick up item------------------------
for item in ItemXList[:]:
    if len(inventoryItemList) < q and (
            man.x <= item <= (playerWidth + man.x)\
            or man.x <= (item + item.width) <= (playerWidth + man.x)):
        v = ItemXList.index(item)
        if man.y <= ItemYList[v] <= (playerHeight + man.y) or man.y <= (ItemYList[v] + item.height) <= (
                playerHeight + man.y):
            ItemRectList.pop(v)
            ItemYList.pop(v)
            ItemXList.pop(v)
            inventoryItemList.append(item.value)
            n -= 1
            a -= 1
            amount -= 1

#3. print items on the screen
for i in ItemRectList:
    screen.blit(Gem_Green, i)

#4. quit game---------------------
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        location = False
        mainRoutine = False

#5. end Tutorial
if Countdown %  500 == 0:
    lists.clear()
    #reset values
    Home = True
    End = False
    Tutorial = False
    mainGame = True



