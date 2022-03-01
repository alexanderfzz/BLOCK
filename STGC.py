import pre_game

def correction():
    #edge correction
    if pre_game.turretX == -36:
        pre_game.turretX = 36
    elif pre_game.turretX == 972:
        pre_game.turretX = 900


    #bread correction
    elif (pre_game.turretX == 396 and pre_game.turretY == 364) or (pre_game.turretX == 396 and pre_game.turretY== 292):
        pre_game.turretX, pre_game.turretY =  322, 292
    elif pre_game.turretX == 396 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 324, 436
    elif pre_game.turretX == 468 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 468, 508
    elif pre_game.turretX == 540 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 612, 436
    elif pre_game.turretX == 540 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 612, 364
    elif (pre_game.turretX == 468 and pre_game.turretY== 292) or (pre_game.turretX == 540 and pre_game.turretY== 292):
        pre_game.turretX, pre_game.turretY = 540, 220


    #path correction
    #route 1
    elif pre_game.turretX == 180 and pre_game.turretY == 4:
        pre_game.turretX, pre_game.turretY = 108, 4
    elif pre_game.turretX == 180 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 108, 76
    elif pre_game.turretX == 180 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 252, 148
    elif pre_game.turretX == 108 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 108, 76
    elif pre_game.turretX == 36 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 32, 76
    elif pre_game.turretX == 36 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 108, 220
    elif pre_game.turretX == 36 and pre_game.turretY == 292:
        pre_game.turretX, pre_game.turretY = 32, 364
    elif pre_game.turretX == 108 and pre_game.turretY == 292:
        pre_game.turretX, pre_game.turretY = 180, 292
    elif pre_game.turretX == 108 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 32, 364
    elif pre_game.turretX == 108 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 32, 436
    elif pre_game.turretX == 180 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 180, 364
    elif pre_game.turretX == 252 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 252, 508
    elif pre_game.turretX == 252 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 252, 292
    elif pre_game.turretX == 324 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 324, 292

    #route 2
    elif pre_game.turretX == 756 and pre_game.turretY == 4:
        pre_game.turretX, pre_game.turretY = 828, 4
    elif pre_game.turretX == 756 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 828, 76
    elif pre_game.turretX == 756 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 828, 148
    elif pre_game.turretX == 756 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 828, 220
    elif pre_game.turretX == 684 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 684, 148
    elif pre_game.turretX == 612 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 612, 292
    elif pre_game.turretX == 612 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 540, 148
    elif pre_game.turretX == 612 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 612, 2
    elif pre_game.turretX == 540 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 540, 2
    elif pre_game.turretX == 468 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 468, 2
    elif pre_game.turretX == 396 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 396, 2
    elif pre_game.turretX == 324 and pre_game.turretY == 76:
        pre_game.turretX, pre_game.turretY = 324, 2
    elif pre_game.turretX == 324 and pre_game.turretY == 148:
        pre_game.turretX, pre_game.turretY = 396, 148
    elif pre_game.turretX == 324 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 252, 220
    elif pre_game.turretX == 396 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 396, 148
    elif pre_game.turretX == 468 and pre_game.turretY == 220:
        pre_game.turretX, pre_game.turretY = 468, 148

    #route 3
    elif pre_game.turretX == 900 and pre_game.turretY == 724:
        pre_game.turretX, pre_game.turretY = 900, 652
    elif pre_game.turretX == 828 and pre_game.turretY == 724:
        pre_game.turretX, pre_game.turretY = 756, 724
    elif pre_game.turretX == 828 and pre_game.turretY == 652:
        pre_game.turretX, pre_game.turretY = 756, 652
    elif pre_game.turretX == 828 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 756, 580
    elif pre_game.turretX == 900 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 900, 652
    elif pre_game.turretX == 900 and pre_game.turretY == 508:
        pre_game.turretX, pre_game.turretY = 828, 508
    elif pre_game.turretX == 900 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 828, 436
    elif pre_game.turretX == 900 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 900, 292
    elif pre_game.turretX == 828 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 828, 292
    elif pre_game.turretX == 756 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 756, 292
    elif pre_game.turretX == 684 and pre_game.turretY == 364:
        pre_game.turretX, pre_game.turretY = 684, 292
    elif pre_game.turretX == 684 and pre_game.turretY == 436:
        pre_game.turretX, pre_game.turretY = 612, 436
    elif pre_game.turretX == 684 and pre_game.turretY == 508:
        pre_game.turretX, pre_game.turretY = 612, 508
    elif pre_game.turretX == 684 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 684, 652
    elif pre_game.turretX == 612 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 612, 652
    elif pre_game.turretX == 540 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 540, 508
    elif pre_game.turretX == 540 and pre_game.turretY == 652:
        pre_game.turretX, pre_game.turretY = 540, 724
    elif pre_game.turretX == 468 and pre_game.turretY == 652:
        pre_game.turretX, pre_game.turretY = 468, 724
    elif pre_game.turretX == 396 and pre_game.turretY == 652:
        pre_game.turretX, pre_game.turretY = 396, 724
    elif pre_game.turretX == 396 and pre_game.turretY == 580:
        pre_game.turretX, pre_game.turretY = 324, 580
    elif pre_game.turretX == 396 and pre_game.turretY == 508:
        pre_game.turretX, pre_game.turretY = 324, 508