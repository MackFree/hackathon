#imports
import sys, pygame, copy
from atom import Atom

#initialising game engine
pygame.init()

#setting size of window
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

#resources inits go here

#colours in RGB
white = 255, 255, 255
black = 0, 0, 0

#drawing the rectangles needed, atom selection screen and place screen
selection_rect = pygame.Rect(0, 0, 500, 719)
simulation_rect = pygame.Rect(500, 0, 780, 720)

#array that will hold all atoms Possible
atom_array = []
selected_atom = None

#list of atoms in the simulation
simulation_atoms = []


#creating atoms
hydrogen    = Atom("Hydrogen", 1, 1, 1, "assets/img/hydrogen-small.png", "assets/desc/hydrogen.txt")
helium      = Atom("Helium", 2, 2, 2, "assets/img/helium-small.png", "assets/desc/helium.txt")
lithium     = Atom("lithium".title(), 3, 4, 3, "assets/img/lithium-small.png", "assets/img/lithium.txt")
beryllium   = Atom("beryllium".title(), 4, 5, 4, "assets/img/beryllium-small.png", "assets/img/beryllium.txt")
boron       = Atom("boron".title(), 5, 6, 5, "assets/img/boron-small.png", "assets/img/boron.txt")
carbon      = Atom("carbon".title(), 6, 6, 6, "assets/img/carbon-small.png", "assets/img/carbon.txt")
nitrogen    = Atom("nitrogen".title(), 7, 7, 7, "assets/img/nitrogen-small.png", "assets/img/nitrogen.txt")
oxygen      = Atom("oxygen".title(), 8, 8, 8, "assets/img/oxygen-small.png", "assets/img/oxygen.txt")
fluorine    = Atom("fluorine".title(), 9, 10, 9, "assets/img/flourine-small.png", "assets/img/flourine.txt")
neon        = Atom("neon".title(), 10, 10, 10, "assets/img/neon-small.png", "assets/img/neon.txt")
sodium      = Atom("sodium".title(), 11, 12, 11, "assets/img/sodium-small.png", "assets/img/sodium.txt")
magnesium   = Atom("magnesium".title(), 12, 12, 12, "assets/img/magnesium-small.png", "assets/img/magnesium.txt")
aluminium   = Atom("aluminium".title(), 13, 14, 13, "assets/img/aluminium-small.png", "assets/img/aluminium.txt")
silicon     = Atom("silicon".title(), 14, 14, 14, "assets/img/silicon-small.png", "assets/img/silicon.txt")
phosphorus  = Atom("phosphorus".title(), 15, 16, 15, "assets/img/phosphorus-small.png", "assets/img/phosphorus.txt")
sulfur      = Atom("sulfur".title(), 16, 16, 16, "assets/img/sulfur-small.png", "assets/img/sulfur.txt")
chlorine    = Atom("chlorine".title(), 17, 18, 17, "assets/img/chlorine-small.png", "assets/img/chlorine.txt")
argon       = Atom("argon".title(), 18, 22, 18, "assets/img/argon-small.png", "assets/img/argon.txt")
potassium   = Atom("potassium".title(), 19, 20, 19, "assets/img/potassium-small.png", "assets/img/potassium.txt")
calcium     = Atom("calcium".title(), 20, 20, 20, "assets/img/calcium-small.png", "assets/img/calcium.txt")

#adding atoms to atom_array
atom_array.append(hydrogen)
atom_array.append(helium)
atom_array.append(lithium)
atom_array.append(beryllium)
atom_array.append(boron)
atom_array.append(carbon)
atom_array.append(nitrogen)
atom_array.append(oxygen)
atom_array.append(fluorine)
atom_array.append(neon)
atom_array.append(sodium)
atom_array.append(magnesium)
atom_array.append(aluminium)
atom_array.append(silicon)
atom_array.append(phosphorus)
atom_array.append(sulfur)
atom_array.append(chlorine)
atom_array.append(argon)
atom_array.append(potassium)
atom_array.append(calcium)

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
    draw_pos_x = 25
    draw_pos_y = 25
    for atom in atom_array:
        atom.rect.x = draw_pos_x
        atom.rect.y = draw_pos_y
        screen.blit(atom.image, atom.rect)
        if(draw_pos_x != 400):
            draw_pos_x += 125
        else:
            draw_pos_x = 25
            draw_pos_y += 125
    
    for atom in simulation_atoms:
        screen.blit(atom.image, atom.rect)
    
    if selected_atom is not None:
        screen.blit(selected_atom.image, selected_atom.rect)    
    
    #making all redrawn things visible
    pygame.display.flip()
