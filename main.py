import pygame, math, random
import pre_game, STGC, enemy


#game loop
while pre_game.running:
    if pre_game.gameOver:
        for event in pygame.event.get():
            # end detection
            if event.type == pygame.QUIT:
                pre_game.running = False
        pre_game.screen.fill((100,175,100))
        pre_game.ShowGameOver()
        pygame.display.update()
    else:
        #event detection
        for event in pygame.event.get():
            #end detection
            if event.type == pygame.QUIT:
                pre_game.running = False
            #key down detection
            if event.type == pygame.KEYDOWN:
                # player movement input
                if event.key == pygame.K_LEFT:
                    pre_game.playerMoveX = -2
                if event.key == pygame.K_RIGHT:
                    pre_game.playerMoveX = 2
                if event.key == pygame.K_DOWN:
                    pre_game.playerMoveY = 2
                if event.key == pygame.K_UP:
                    pre_game.playerMoveY = -2
                #r key detection, "function"
                if event.key == pygame.K_r and pre_game.rState and not pre_game.p_u:
                    pre_game.turret = pygame.transform.rotate(pre_game.turret, 90)
                    pre_game.turretAngle += 1
                #e key detection, function
                if event.key == pygame.K_e and pre_game.eState and not pre_game.p_u:
                    pre_game.p_u = True
                elif event.key == pygame.K_e and pre_game.eState and pre_game.p_u:
                    pre_game.p_u = False
                    if pre_game.playerX < 324 and pre_game.playerY > 576:
                        pre_game.turretPosition = "start"
                    else:
                        pre_game.turretPosition = "green"
                        pre_game.playerXt = pre_game.playerX
                        pre_game.playerYt = pre_game.playerY

            #key up detection
            if event.type == pygame.KEYUP:
                #halt player movement
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pre_game.playerMoveX = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    pre_game.playerMoveY = 0


        #load background image
        pre_game.screen.blit(pre_game.map, (0,0))


        pre_game.playerX += pre_game.playerMoveX
        pre_game.playerY += pre_game.playerMoveY

        #player edge movement boudaries
        if pre_game.playerX > 936:
            pre_game.playerX = 936
        elif pre_game.playerX < 0:
            pre_game.playerX = 0
        elif pre_game.playerY > 736:
            pre_game.playerY = 736
        elif pre_game.playerY < 0:
            pre_game.playerY = 0
        #player bread movement boundaries
        if 373 < pre_game.playerX < 375 and 272 < pre_game.playerY < 464:
            pre_game.playerX = 372
        if 563 > pre_game.playerX > 561 and 272 < pre_game.playerY < 464:
            pre_game.playerX = 564
        if 273 < pre_game.playerY < 275 and 372 < pre_game.playerX < 564:
            pre_game.playerY = 272
        if 463 > pre_game.playerY > 461 and 372 < pre_game.playerX < 564:
            pre_game.playerY = 464

        #enemy
        if pre_game.enemySpeedC < 5000:
            pre_game.enemySpeedC += 1
        else:
            pre_game.enemySpeedC = 0
            pre_game.enemySpeed += 1
        for i in range(pre_game.enemySpeed):
            if not pre_game.enemyAlive:
                pre_game.route = random.randint(1,3)
                enemyB = True
                pre_game.enemyAlive = True
                enemy.StatsReset()
            if enemyB:
                enemy.ShowEnemy()
                if enemy.done == True:
                    enemyB = False
                    pre_game.enemyAlive = False

        #load turret
        if not pre_game.p_u:
            if pre_game.turretPosition == "start":
                pre_game.ShowTurret(180, 652)
                pre_game.turretX = 180
                pre_game.turretY = 652
            elif pre_game.turretPosition == "green":
                #snap to grid
                pre_game.turretX = round((pre_game.playerXt - 32)/ 72) *72 + 36
                pre_game.turretY = round(pre_game.playerYt / 72) * 72 + 4
                #snap to grid correstion
                STGC.correction()
                pre_game.ShowTurret(pre_game.turretX, pre_game.turretY)

        #turret pick up, bullet fire action control
        if not pre_game.p_u:
            #bullet's speed control
            if pre_game.bulletState == "ready":
                pre_game.bulletSpeed += 1
            if pre_game.bulletSpeed == 50:
                if pre_game.bulletAngle != pre_game.turretAngle:
                    pre_game.bullet = pygame.transform.rotate(pre_game.bullet, (pre_game.turretAngle % 4 - pre_game.bulletAngle) * 90)
                    pre_game.bulletAngle = pre_game.turretAngle
                pre_game.bulletState = "fire"
                pre_game.bulletX = pre_game.turretX
                pre_game.bulletY = pre_game.turretY
                pre_game.bulletSpeed = 0
        else:
            if pre_game.bulletState == "ready":
                pre_game.bulletX, pre_game.bulletY = 0, 0
        #bullet if-fired detection
        if pre_game.bulletState == "fire":
            pre_game.ShowBullet(pre_game.bulletX + 4, pre_game.bulletY + 12)
            #bullet direction detection
            if pre_game.bulletAngle % 4 == 0:
                pre_game.bulletY += pre_game.bulletMoveY
                if pre_game.bulletY > 790:
                    pre_game.bulletY = pre_game.turretY
                    pre_game.bulletX = pre_game.turretX
                    pre_game.bulletState = "ready"
            if pre_game.bulletAngle % 4 == 1:
                pre_game.bulletX += pre_game.bulletMoveX
                if pre_game.bulletX > 990:
                    pre_game.bulletX = pre_game.turretX
                    pre_game.bulletY = pre_game.turretY
                    pre_game.bulletState = "ready"
            if pre_game.bulletAngle % 4 == 2:
                pre_game.bulletY -= pre_game.bulletMoveY
                if pre_game.bulletY < 10:
                    pre_game.bulletY = pre_game.turretY
                    pre_game.bulletX = pre_game.turretX
                    pre_game.bulletState = "ready"
            if pre_game.bulletAngle % 4 == 3:
                pre_game.bulletX -= pre_game.bulletMoveX
                if pre_game.bulletX < 10:
                    pre_game.bulletX = pre_game.turretX
                    pre_game.bulletY = pre_game.turretY
                    pre_game.bulletState = "ready"

        # load turret 2nd layer
        if not pre_game.p_u:
            pre_game.ShowTurret(pre_game.turretX,pre_game.turretY)

        #load bread
        pre_game.ShowBread()
        if pre_game.breadHP == 0:
            pre_game.gameOver = True

        #load player
        pre_game.ShowPlayer(pre_game.playerX, pre_game.playerY)

        # player-turret range calculation
        length = math.sqrt((pre_game.playerX - pre_game.turretX) ** 2 + (pre_game.playerY - pre_game.turretY) ** 2)
        if pre_game.p_u:
            pre_game.eState = True
            pre_game.rState = False
        elif length < 96:
            pre_game.rState = True
            pre_game.eState = True
        else:
            pre_game.rState = False
            pre_game.eState = False

        #load r key
        if pre_game.rState:
            pre_game.ShowR(pre_game.playerX, pre_game.playerY)
        #load e key
        if pre_game.eState:
            pre_game.ShowE(pre_game.playerX, pre_game.playerY)

        #load stats
        pre_game.ShowScore()
        pre_game.ShowHP()
        #update new frame
        pygame.display.update()