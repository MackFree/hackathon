import sys, pygame

pygame.init()

size = width, height = 1280, 720
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

#creating the graphics below
screen = pygame.display.set_mode(size)



ball = pygame.image.load("newspaper.png")


ballrect = ball.get_rect()
is_clicked = False

#building the menu

#button images
helpbutton = pygame.image.load("helpbutton.png")
gobutton = pygame.image.load("startbutton.png")
quitbutton = pygame.image.load("quitbutton.png")

#button rects
helpbuttonrect = helpbutton.get_rect()
gobuttonrect = gobutton.get_rect()
quitbuttonrect = quitbutton.get_rect()

helpbuttonrect.x = 560
gobuttonrect.x = 560
quitbuttonrect.x = 560

gobuttonrect.y = 200
helpbuttonrect.y = 270
quitbuttonrect.y = 340

#game state 0 = menu, 1 = game, 2 = help screen
game_state = 0

while game_state == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(gobuttonrect.collidepoint(pos)):
                #go to game
                game_state = 1
            elif(quitbuttonrect.collidepoint(pos)):
                #quit the game
                pygame.quit()
            elif(helpbuttonrect.collidepoint(pos)):
                #display help
                game_state = 2
    
    
    #drawring
    screen.fill(white)
    screen.blit(quitbutton, quitbuttonrect)
    screen.blit(gobutton, gobuttonrect)
    screen.blit(helpbutton, helpbuttonrect)
    
    #making everything visible
    pygame.display.flip()
    
while game_state == 1:
    #quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #getting the position
            pos = pygame.mouse.get_pos()
            if(ballrect.collidepoint(pos)):
                is_clicked = True
                game_state = 3
        if(event.type == pygame.MOUSEBUTTONUP):
            is_clicked = False
    
    ballrect = ballrect.move(speed)
    if(is_clicked):
        pos = pygame.mouse.get_pos()
        #because the fuggin thing is taken from the top corner
        #we need the second part of the equation        
        ballrect.x = pos[0] - (ballrect.width/2)
        ballrect.y = pos[1] - (ballrect.width/2)
    else:
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
    #re drawing all shite
    screen.fill(black)
    screen.blit(ball, ballrect)
    #making everything visible
    pygame.display.flip()
    
while game_state == 3:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
    screen.fill(white)
    pygame.display.flip()