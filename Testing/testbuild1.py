#imports
import sys, pygame

#initialising game engine
pygame.init()

#setting size of window
size = width, height = 720, 480
screen = pygame.display.set_mode(size)

#resources inits go here

#colours in RGB
white = 255, 255, 255


#array that will hold all atoms in the atom class
atom_array = []

#game loop
while 1:
    #exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        #mousebutton down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            #getting the position
            pos = pygame.mouse.get_pos()
            #now we need to check which atom it is clicked on
            
    #re-drawring background
    screen.fill(white)
    #making all redrawn things visible
    pygame.display.flip()