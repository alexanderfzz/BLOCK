import pre_game
import math

enemyMove = 0.5

# boolean values
def StatsReset():
    global done, begin_1, hit1_1, hit1_2, hit1_3, hit1_4, hit1_5, hit1_6, hit1_7, enemyX_1, enemyY_1
    global begin_2, hit2_1, hit2_2, hit2_3, hit2_4, hit2_5, hit2_6,enemyX_2, enemyY_2
    global begin_3, hit3_1, hit3_2, hit3_3, hit3_4, hit3_5, hit3_6, hit3_7, hit3_8, hit3_9, enemyX_3, enemyY_3
    done = False
    begin_1 = True
    hit1_1 = False
    hit1_2 = False
    hit1_3 = False
    hit1_4 = False
    hit1_5 = False
    hit1_6 = False
    hit1_7 = False
    enemyX_1 = 180
    enemyY_1 = 4
    begin_2 = True
    hit2_1 = False
    hit2_2 = False
    hit2_3 = False
    hit2_4 = False
    hit2_5 = False
    hit2_6 = False
    enemyX_2 = 756
    enemyY_2 = 4
    begin_3 = True
    hit3_1 = False
    hit3_2 = False
    hit3_3 = False
    hit3_4 = False
    hit3_5 = False
    hit3_6 = False
    hit3_7 = False
    hit3_8 = False
    hit3_9 = False
    enemyX_3 = 900
    enemyY_3 = 724

def ShowEnemy():
    #route 1
    if pre_game.route == 1:
        global done, begin_1, hit1_1, hit1_2, hit1_3, hit1_4, hit1_5, hit1_6, hit1_7, enemyX_1, enemyY_1
        if  begin_1 and not hit1_1 and not hit1_2 and not hit1_3 and not hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            begin_1 = False
        elif not begin_1 and not hit1_1 and not hit1_2 and not hit1_3 and not hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            enemyY_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 180 and enemyY_1 == 148:
                hit1_1 = True
        elif not begin_1 and hit1_1 and not hit1_2 and not hit1_3 and not hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            enemyX_1 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 36 and enemyY_1 == 148:
                hit1_2 = True
        elif not begin_1 and hit1_1 and hit1_2 and not hit1_3 and not hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            enemyY_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 36 and enemyY_1 == 292:
                hit1_3 = True
        elif not begin_1 and hit1_1 and hit1_2 and hit1_3 and not hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            enemyX_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 108 and enemyY_1 == 292:
                hit1_4 = True
        elif not begin_1 and hit1_1 and hit1_2 and hit1_3 and hit1_4 and not hit1_5 and not hit1_6 and not hit1_7:
            enemyY_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 108 and enemyY_1 == 436:
                hit1_5= True
        elif not begin_1 and hit1_1 and hit1_2 and hit1_3 and hit1_4 and hit1_5 and not hit1_6 and not hit1_7:
            enemyX_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 252 and enemyY_1 == 436:
                hit1_6 = True
        elif not begin_1 and hit1_1 and hit1_2 and hit1_3 and hit1_4 and hit1_5 and hit1_6 and not hit1_7:
            enemyY_1 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 252 and enemyY_1 == 364:
                hit1_7 = True
        elif not begin_1 and hit1_1 and hit1_2 and hit1_3 and hit1_4 and hit1_5 and hit1_6 and hit1_7:
            enemyX_1 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_1, enemyY_1))
            if enemyX_1 == 396 and enemyY_1 == 364:
                pre_game.breadHP -= 1
                done = True
        if math.sqrt((enemyX_1 + 20 - pre_game.bulletX + 4) ** 2 + (enemyY_1 + 20 - pre_game.bulletY + 4) ** 2)  <= 33:
            pre_game.enemyAlive = False
            pre_game.bulletState = "ready"
    #route 2
    elif pre_game.route == 2:
        global begin_2, hit2_1, hit2_2, hit2_3, hit2_4, hit2_5, hit2_6, enemyX_2, enemyY_2
        if  begin_2 and not hit2_1 and not hit2_2 and not hit2_3 and not hit2_4 and not hit2_5 and not hit2_6:
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            begin_2 = False
        elif not begin_2 and not hit2_1 and not hit2_2 and not hit2_3 and not hit2_4 and not hit2_5 and not hit2_6:
            enemyY_2 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 756 and enemyY_2 == 220:
                hit2_1 = True
        elif not begin_2 and  hit2_1 and not hit2_2 and not hit2_3 and not hit2_4 and not hit2_5 and not hit2_6:
            enemyX_2 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 612 and enemyY_2 == 220:
                hit2_2 = True
        elif not begin_2 and  hit2_1 and hit2_2 and not hit2_3 and not hit2_4 and not hit2_5 and not hit2_6:
            enemyY_2 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 612 and enemyY_2 == 76:
                hit2_3 = True
        elif not begin_2 and  hit2_1 and hit2_2 and hit2_3 and not hit2_4 and not hit2_5 and not hit2_6:
            enemyX_2 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 324 and enemyY_2 == 76:
                hit2_4 = True
        elif not begin_2 and  hit2_1 and hit2_2 and hit2_3 and hit2_4 and not hit2_5 and not hit2_6:
            enemyY_2 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 324 and enemyY_2 == 220:
                hit2_5 = True
        elif not begin_2 and  hit2_1 and hit2_2 and hit2_3 and hit2_4 and hit2_5 and not hit2_6:
            enemyX_2 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 468 and enemyY_2 == 220:
                hit2_6 = True
        elif not begin_2 and  hit2_1 and hit2_2 and hit2_3 and hit2_4 and hit2_5 and hit2_6:
            enemyY_2 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_2, enemyY_2))
            if enemyX_2 == 468 and enemyY_2 == 292:
                pre_game.breadHP -= 1
                done = True
        if math.sqrt((enemyX_2 + 20 - pre_game.bulletX + 4) ** 2 + (enemyY_2 + 20 - pre_game.bulletY + 4) ** 2)  <= 33:
            pre_game.enemyAlive = False
            pre_game.bulletState = "ready"

        #route 3
    elif pre_game.route == 3:
        global begin_3, hit3_1, hit3_2, hit3_3, hit3_4, hit3_5, hit3_6, hit3_7, hit3_8, hit3_9, enemyX_3, enemyY_3
        if begin_3 and not hit3_1 and not hit3_2 and not hit3_3 and not hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            begin_3 = False
        if not begin_3 and not hit3_1 and not hit3_2 and not hit3_3 and not hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyX_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 828 and enemyY_3 == 724:
                hit3_1 = True
        elif not begin_3 and hit3_1 and not hit3_2 and not hit3_3 and not hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyY_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 828 and enemyY_3 == 580:
                hit3_2 = True
        elif not begin_3 and hit3_1 and hit3_2 and not hit3_3 and not hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyX_3 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 900 and enemyY_3 == 580:
                hit3_3 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and not hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyY_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 900 and enemyY_3 == 364:
                hit3_4 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and not hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyX_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 684 and enemyY_3 == 364:
                hit3_5 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and hit3_5 and not hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyY_3 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 684 and enemyY_3 == 580:
                hit3_6 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and hit3_5 and hit3_6 and not hit3_7 and not hit3_8 and not hit3_9:
            enemyX_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 540 and enemyY_3 == 580:
                hit3_7 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and hit3_5 and hit3_6 and hit3_7 and not hit3_8 and not hit3_9:
            enemyY_3 += enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 540 and enemyY_3 == 652:
                hit3_8 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and hit3_5 and hit3_6 and hit3_7 and hit3_8 and not hit3_9:
            enemyX_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 396 and enemyY_3 == 652:
                hit3_9 = True
        elif not begin_3 and hit3_1 and hit3_2 and hit3_3 and hit3_4 and hit3_5 and hit3_6 and hit3_7 and hit3_8 and hit3_9:
            enemyY_3 -= enemyMove
            pre_game.screen.blit(pre_game.enemy, (enemyX_3, enemyY_3))
            if enemyX_3 == 396 and enemyY_3 == 436:
                pre_game.breadHP -= 1
                done = True
        if math.sqrt((enemyX_3 +20 - pre_game.bulletX + 4) ** 2 + (enemyY_3 +20 - pre_game.bulletY + 4) ** 2)  <= 33:
            pre_game.enemyAlive = False
            pre_game.bulletState = "ready"