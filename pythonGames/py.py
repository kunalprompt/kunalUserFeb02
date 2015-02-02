import random
 
import pygame
 
 
pygame.init()
screen = pygame.display.set_mode( ( 640, 480 ) )
screen.fill( ( 255, 255, 255 ) )
balx, baly = ( 320, 240 )
balxspeed, balyspeed = random.choice( [( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 )] )
fps = pygame.time.Clock()
yleft = 240
yright = 240
 
right_score = 0
left_score = 0
 
while True:
    eventlst = pygame.event.get()
    for event in eventlst:
        if event.type == pygame.QUIT:
            raise SystemExit
 
    #  move the ball
    balx += balxspeed
    baly += balyspeed
 
    #  if the ball hits 0-up or 480-down it bounces back
    if baly >= 480 or baly <= 0:
        balyspeed *= -1
 
    #  score board
    if balx <= 0:
        right_score += 1
        #  print "left", left_score, "-", right_score, "right"
    if balx >= 640:
        left_score += 1
        #  print "left", left_score, "-", right_score, "right"
 
    #  if the ball hits 0-left or 640-right it resets the ball
    if balx >= 640 or balx <= 0:
        balx, baly = ( 320, 240 )
        balxspeed, balyspeed = random.choice( [( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 )] )
 
    keys = pygame.key.get_pressed()
 
    #  move the rectangle up or down
    if keys[pygame.K_DOWN]:
        yright += 2
    if keys[pygame.K_UP]:
        yright -= 2
    if keys[pygame.K_w]:
        yleft -= 2
    if keys[pygame.K_s]:
        yleft += 2
 
    #  make sure the rectangle yleft doesn't go further up or down than either 0 or 480
    if yleft <= 0:
        yleft = 0
    if yleft >= 430:
        yleft = 430
    #  make sure the rectangle yright doesn't go further up or down than either 0 or 480
    if yright <= 0:
        yright = 0
    if yright >= 430:
        yright = 430
 
    if balx <= 10:
        #  if ball hits rectangle do bounce
        if baly >= yleft and baly <= yleft + 50:
            balxspeed *= -1.5
            balx = 11
            if keys[pygame.K_w]:
                balyspeed = -abs( balyspeed )
            if keys[pygame.K_s]:
                balyspeed = abs( balyspeed )
 
    if balx >= 630:
        #  if ball hits rectangle do bounce
        if baly >= yright and baly <= yright + 50:
            balxspeed *= -1.5
            balx = 629
            if keys[pygame.K_UP]:
                balyspeed = -abs( balyspeed )
            if keys[pygame.K_DOWN]:
                balyspeed = abs( balyspeed )
 
    screen.fill( ( 255, 255, 255 ) )
    pygame.draw.circle( screen, ( 255, 0, 0 ), ( int( balx ), int( baly ) ), 8 )
    pygame.draw.rect( screen, ( 0, 0, 0 ), ( 0, yleft, 10, 50 ) )
    pygame.draw.rect( screen, ( 0, 0, 0 ), ( 630, yright, 10, 50 ) )
    pygame.display.update()
    fps.tick( 60 )



'''
3 4 3 2 4


diff = hk+1-bot

if hk+1>botEnergy, then he will lose diff
else: gain      -1*(diff)

Goal is to reach Nth building, and during the course bot should never have negative energy units. 
What should be the minimum units of energy with which bot should start to successfully complete the game?

'''