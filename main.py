import pygame

def checkCollision(x, y, treasurex, treasurey, window):
    collision_state = False
    if y >= treasurey and y <= treasurey + 40:
        if x >= treasurex and x <= treasurex + 35:
            y = 650
            collision_state = True
        elif x + 35 >= treasurex and x + 35 <= treasurex + 35:
            y = 650
            collision_state = True
    elif y + 40 >= treasurey and y + 40 <= treasurey + 40:
        if x >= treasurex and x <= treasurex + 35:
            y = 650
            collision_state = True
        elif x + 35 >= treasurex and x + 35 <= treasurex + 35:
            y = 650
            collision_state = True
    return collision_state, y

pygame.init()
window = pygame.display.set_mode((900, 700))
font = pygame.font.SysFont("comicsans", 80)
level = 1

finished = False
x = 450 - 35/2
y = 650
playerimg = pygame.image.load("player.png")
playerimg = pygame.transform.scale(playerimg, (35, 40))
playerimg = playerimg.convert_alpha()
bgimg = pygame.image.load("background.png")
bgimg = pygame.transform.scale(bgimg, (900, 700))
window.blit(bgimg, (0, 0))

treasureimg = pygame.image.load("treasure.png")
treasureimg = pygame.transform.scale(treasureimg, (35, 40))
treasureimg = treasureimg.convert_alpha()

enemyimg = pygame.image.load("enemy.png")
enemyimg = pygame.transform.scale(enemyimg, (35,40))
enemyimg = enemyimg.convert_alpha()


treasurex = 450 - 35/2
treasurey = 50

enemyx = 100
enemyy = 570

window.blit(treasureimg, (treasurex, treasurey))

enemynames = {0:"Max", 1:"Jill", 2:"Greg", 3:"Diane"}

frame = pygame.time.Clock()
collision_treasure = False
enemyright = True
collision_enemy = False
name = ""
enemies = [(enemyx, enemyy, enemyright)]#(enemyx, enemyy, enemyright)

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    keypress = pygame.key.get_pressed()
    enemyIndex = 0
    for enemyx, enemyy, enemyright in enemies:
        if enemyx >= 800-35:
            enemyright = False
        elif enemyx <= 100:
            enemyright = True
        if enemyright == True:
            enemyx += 5*level
        else:
            enemyx -= 5*level
        enemies[enemyIndex] = (enemyx, enemyy, enemyright)
        enemyIndex += 1
    if keypress[pygame.K_SPACE] == 1:
        y -= 5
    #dorect = pygame.Rect(x, y, 30, 30)

    rectcolor = (0, 0, 255)
    #white = (255, 255, 255)
    window.blit(bgimg, (0, 0))
    window.blit(treasureimg, (treasurex, treasurey))
    window.blit(playerimg, (x, y))
    
    enemyIndex = 0
    for enemyx, enemyy, enemyright in enemies:
        window.blit(enemyimg, (enemyx, enemyy))
        collision_enemy,y = checkCollision(x, y, enemyx, enemyy, window)
        if collision_enemy == True:
            name = enemynames[enemyIndex]
            textDead = font.render("You died!",True,(255,0,0))
            textKilled = font.render("You were killed by "+name,True,(255,0,0))
            window.blit(textDead, (450 - textDead.get_width()/2,250 - textDead.get_height()/2))
            window.blit(textKilled, (450 - textKilled.get_width()/2,300 - textKilled.get_height()/2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(50)
        enemyIndex += 1
    collision_treasure,y = checkCollision(x, y, treasurex, treasurey, window)
    #collision_enemy,y = checkCollision(x, y, enemyx, enemyy, window)
    if collision_treasure == True:
        level +=  1
        enemies.append((enemyx-50*level, enemyy-50*level, False))
        winText = font.render("You've reached Level"+str(level),True, (0,0,0))
        window.blit(winText, (450 - winText.get_width()/2,300))
        pygame.display.flip()
        frame.tick(1)
    #elif collision_enemy == True:
    #    winText = font.render("You died!  :( " ,True, (0,0,0))
    #    window.blit(winText, (450 - winText.get_width()/2,200))
    #    collision_enemy = False
    #    pygame.display.flip()
    #    frame.tick(1)
    #pygame.draw.rect(window, rectcolor, dorect)
    pygame.display.flip()
    frame.tick(30)
