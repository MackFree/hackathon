#imports
import sys, pygame, copy
from atom import Atom

#initialising game engine
pygame.init()

#setting size of window
size = width, height = 720, 480
screen = pygame.display.set_mode(size)

#resources inits go here

#colours in RGB
white = 255, 255, 255
black = 0, 0, 0

#drawing the rectangles needed, atom selection screen and place screen
selection_rect = pygame.Rect(0, 0, 300, 479)
simulation_rect = pygame.Rect(300, 0, 420, 480)

#array that will hold all atoms Possible
atom_array = []
selected_atom = None

#list of atoms in the simulation
simulation_atoms = []


#creating atoms
hydrogen = Atom("Hydrogen", 1, 1, 1, "assets/img/hydrogen.png", "assets/desc/hydrogen.txt")

hydrogen.rect.x = 2
hydrogen.rect.y = 2
#adding atoms to atom_array
atom_array.append(hydrogen)


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
            if(selection_rect.collidepoint(pos)):
                print("EAT MY ASS")
                for atom in atom_array:
                    #compare mousepos and atom circle pos
                    if(atom.rect.collidepoint(pos)):
                        #find atom type and create new instance 
                        #need atom constructor ect
                        selected_atom = Atom(atom.name, atom.proton, atom.neutron, atom.electron, atom.image_loc, atom.info_loc)
                
            if(simulation_rect.collidepoint(pos)):
                print("Sim")
        
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(simulation_rect.collidepoint(pos) and selected_atom is not None):
                #we in the simulation rect
                simulation_atoms.append(selected_atom)
            selected_atom = None
            #also need to place the atom in the simulator section
    
    #moving selected atom with the mouse
    if(selected_atom is not None):
        pos = pygame.mouse.get_pos()
        selected_atom.rect.x = pos[0] - (selected_atom.rect.width/2)
        selected_atom.rect.y = pos[1] - (selected_atom.rect.width/2)
    
    #re-drawring background
    screen.fill(white)    
    
    #drawring #needs to be from the bottom up 
    pygame.draw.rect(screen, black, selection_rect, 2)
    
    #now we draw an atom for each one in the array (Lets use a loop bc
    #fuck doing it induvidiall
    for atom in atom_array:
        screen.blit(atom.image, atom.rect)
    
    for atom in simulation_atoms:
        screen.blit(atom.image, atom.rect)
    
    if selected_atom is not None:
        screen.blit(selected_atom.image, selected_atom.rect)    
    
    #making all redrawn things visible
    pygame.display.flip()