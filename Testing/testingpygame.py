import sys, pygame

pygame.init()

size = width, height = 1000, 1000
speed = [2, 2]
black = 0, 0, 0

#creating the graphics below
screen = pygame.display.set_mode(size)

ball = pygame.image.load("newspaper.png")
ballrect = ball.get_rect()

is_clicked = False

while 1:
    #quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #getting the position
            pos = pygame.mouse.get_pos()
            if(ballrect.collidepoint(pos)):
                is_clicked = True
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