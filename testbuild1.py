#imports
import sys, pygame, copy
from atom import Atom

#initialising game engine
pygame.init()

#setting the title
pygame.display.set_caption("Learn About Elements!")

#setting size of window
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

#resources inits go here

#font
font = pygame.font.Font('freesansbold.ttf', 13) 

#colours in RGB
white = 255, 255, 255
black = 0, 0, 0

#drawing the rectangles needed, atom selection screen and place screen
selection_rect = pygame.Rect(0, 0, 525, 719)
simulation_rect = pygame.Rect(525, 0, 755, 720)

#array that will hold all atoms Possible
atom_array = []
selected_atom = None

#list of atoms in the simulation
simulation_atoms = []

#text atom
atom_info_img = None

#creating atoms
hydrogen    = Atom("Hydrogen", 1, 1, 1, "assets/img/hydrogen-small.png", "assets/desc/images/hydrogen.png")
helium      = Atom("Helium", 2, 2, 2, "assets/img/helium-small.png", "assets/desc/images/helium.png")
lithium     = Atom("lithium".title(), 3, 4, 3, "assets/img/lithium-small.png", "assets/desc/images/lithium.png")
beryllium   = Atom("beryllium".title(), 4, 5, 4, "assets/img/beryllium-small.png", "assets/desc/images/beryllium.png")
boron       = Atom("boron".title(), 5, 6, 5, "assets/img/boron-small.png", "assets/desc/images/boron.png")
carbon      = Atom("carbon".title(), 6, 6, 6, "assets/img/carbon-small.png", "assets/desc/images/carbon.png")
nitrogen    = Atom("nitrogen".title(), 7, 7, 7, "assets/img/nitrogen-small.png", "assets/desc/images/nitrogen.png")
oxygen      = Atom("oxygen".title(), 8, 8, 8, "assets/img/oxygen-small.png", "assets/desc/images/oxygen.png")
fluorine    = Atom("fluorine".title(), 9, 10, 9, "assets/img/flourine-small.png", "assets/desc/images/fluorine.png")
neon        = Atom("neon".title(), 10, 10, 10, "assets/img/neon-small.png", "assets/desc/images/neon.png")
sodium      = Atom("sodium".title(), 11, 12, 11, "assets/img/sodium-small.png", "assets/desc/images/sodium.png")
magnesium   = Atom("magnesium".title(), 12, 12, 12, "assets/img/magnesium-small.png", "assets/desc/images/magnesium.png")
aluminium   = Atom("aluminium".title(), 13, 14, 13, "assets/img/aluminium-small.png", "assets/desc/images/aluminium.png")
silicon     = Atom("silicon".title(), 14, 14, 14, "assets/img/silicon-small.png", "assets/desc/images/silicon.png")
phosphorus  = Atom("phosphorus".title(), 15, 16, 15, "assets/img/phosphorus-small.png", "assets/desc/images/phosphorus.png")
sulfur      = Atom("sulfur".title(), 16, 16, 16, "assets/img/sulfur-small.png", "assets/desc/images/sulfur.png")
chlorine    = Atom("chlorine".title(), 17, 18, 17, "assets/img/chlorine-small.png", "assets/desc/images/chlorine.png")
argon       = Atom("argon".title(), 18, 22, 18, "assets/img/argon-small.png", "assets/desc/images/argon.png")
potassium   = Atom("potassium".title(), 19, 20, 19, "assets/img/potassium-small.png", "assets/desc/images/potassium.png")
calcium     = Atom("calcium".title(), 20, 20, 20, "assets/img/calcium-small.png", "assets/desc/images/calcium.png")

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
            print(event.button)
            pos = pygame.mouse.get_pos()
            #now we need to check which atom it is clicked on
            if(selection_rect.collidepoint(pos)):
                print("EAT MY ASS")
                for atom in atom_array:
                    #compare mousepos and atom circle pos
                    if(atom.rect.collidepoint(pos)):
                        if(event.button == 1):
                            #find atom type and create new instance 
                            #need atom constructor ect
                            selected_atom = Atom(atom.name, atom.proton, atom.neutron, atom.electron, atom.image_loc, atom.info_loc)
                        elif(event.button == 3):
                            #now we gotta uhh disp text
                            atom_info_img = atom.info
            if(simulation_rect.collidepoint(pos)):
                print("Sim")
        
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(simulation_rect.collidepoint(pos) and selected_atom is not None):
                #we in the simulation rect
                simulation_atoms.append(selected_atom)
            selected_atom = None
            atom_info_img = None
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
    draw_pos_y = 70
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
    
    #text for atom info
    if(atom_info_img is not None):
        infoRect = atom_info_img.get_rect()
        infoRect.center = pygame.mouse.get_pos()
        screen.blit(atom_info_img, infoRect)
    
    
    #making all redrawn things visible
    pygame.display.flip()
