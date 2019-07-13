#imports
import sys, pygame, copy
import itertools
from atom import Atom

# Initialise database
DATABASE = set()
COMBI_DESC = dict()

#initialising game engine
pygame.init()

#init game_state to menu
#game state 0 = menu, 1 = game, 2 = help screen
game_state = 0

#setting the title
pygame.display.set_caption("Learn About Elements!")

#setting size of window
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

#resources inits go here

#colours in RGB
white = 255, 255, 255
black = 0, 0, 0
title_color = 2, 117, 185

#helpscreenimage
helpscreenimage = pygame.image.load("assets/helpscreen.png")

helpscreenimagerect = helpscreenimage.get_rect()

#button image assets
helpbutton = pygame.image.load("assets/button/helpbutton.png")
gobutton = pygame.image.load("assets/button/startbutton.png")
quitbutton = pygame.image.load("assets/button/quitbutton.png")
combinebutton = pygame.image.load("assets/button/combinebutton.png")
clearbutton = pygame.image.load("assets/button/clearbutton.png")
backbutton = pygame.image.load("assets/button/backbutton.png")
menubutton = pygame.image.load("assets/button/quittomenubutton.png")

#button rects
helpbuttonrect = helpbutton.get_rect()
gobuttonrect = gobutton.get_rect()
quitbuttonrect = quitbutton.get_rect()
combinebuttonrect = combinebutton.get_rect()
clearbuttonrect = clearbutton.get_rect()
backbuttonrect = backbutton.get_rect()
menubuttonrect = menubutton.get_rect()


#button locations
helpbuttonrect.x = 560
gobuttonrect.x = 560
quitbuttonrect.x = 560

combinebuttonrect.x = 1050
clearbuttonrect.x = 830
menubuttonrect.x = 1050

backbuttonrect.x = 560

gobuttonrect.y = 200
helpbuttonrect.y = 270
quitbuttonrect.y = 340

combinebuttonrect.y = 650
clearbuttonrect.y = 650
menubuttonrect.y = 30

backbuttonrect.y = 650

#text
font = pygame.font.Font('freesansbold.ttf', 20)
element_name_text = "Press Combine to see if you've made a compound"
element_text_obj = font.render(element_name_text, True, black, white)
element_text_rect = element_text_obj.get_rect()

#text loc
element_text_rect.x = 550
element_text_rect.y = 45

#molecule description
font = pygame.font.Font('freesansbold.ttf', 13)
fontbig = pygame.font.Font('freesansbold.ttf', 20)

element_desc_text = ""
element_desc_obj = font.render(element_desc_text, True, black, white)
element_desc_rect = element_desc_obj.get_rect()

#molecule description loc
element_desc_rect.x = 550
element_desc_rect.y = 95

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

# reads the database file and load it to the program
def read_database(db_file="database.txt"):
    with open(db_file, 'r') as f:
        for line in f:
            combi, name, desc = line.rstrip().split(":")
            DATABASE.add(combi)
            COMBI_DESC[combi] = (name, desc)

# checks if current combination of atoms are in the database
# the database must first be populated with read_database() function
def is_in_database(atom_combination):
    # sort the current atom combination by their name
    atom_sorted = ''.join([x.name for x in sorted(atom_combination)])
    mol_name = ""
    mol_desc = ""

    if atom_sorted in DATABASE:
        mol_name, mol_desc = COMBI_DESC[atom_sorted]
    return (atom_sorted in DATABASE, mol_name, mol_desc)

def setup_bg():
    # draw background image
    bg_image = pygame.image.load("assets/bg.png")
    img_w, img_h = bg_image.get_width(), bg_image.get_height()
    for x, y in itertools.product(range(0, width+1, img_w),
            range(0, height+1, img_h)):
        screen.blit(bg_image, (x, y))

    # draw title
    title_font = pygame.font.Font('freesansbold.ttf', 50)
    title_obj = title_font.render("Chemical Creator", True, title_color)
    title_rect = title_obj.get_rect(center=(width/2, 100))
    screen.blit(title_obj, title_rect)

    line_start = title_rect.left, title_rect.top + title_rect.height + 3
    line_end = title_rect.left + title_rect.width, title_rect.top + title_rect.height + 3
    pygame.draw.line(screen, title_color, line_start, line_end, 1)

while 1:
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

        #screen.fill(white)
        setup_bg()
        screen.blit(quitbutton, quitbuttonrect)
        screen.blit(gobutton, gobuttonrect)
        screen.blit(helpbutton, helpbuttonrect)
        
        #making everything visible
        pygame.display.flip()
    
    
    
    #getting data into program
    read_database()
    
    #gameplay loop
    while game_state == 1:
        #exiting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            
            
            #mousebutton down event
            if event.type == pygame.MOUSEBUTTONDOWN:
                #getting the position
                pos = pygame.mouse.get_pos()
                #now we need to check which atom it is clicked on
                if(selection_rect.collidepoint(pos)):
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
            
            
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(simulation_rect.collidepoint(pos) and selected_atom is not None):
                    #we in the simulation rect
                    element_name_text = "Press Combine to see if you've made a compound"
                    simulation_atoms.append(selected_atom)
                selected_atom = None
                atom_info_img = None
                if(combinebuttonrect.collidepoint(pos)):
                    #now we want to combine all the atoms
                    in_database, mol_name, mol_desc = is_in_database(simulation_atoms)
                    if(in_database):
                        element_name_text = mol_name
                        #this is where we need to save the Compound to a file
                        sav_file = open("saves/madeelements.txt", 'r+')
                        sav_list = sav_file.readlines()
                        print(sav_list)
                        print(mol_name + '\n')
                        if(mol_name + '\n' not in sav_list):
                            sav_file.close()
                            sav_file = open("saves/madeelements.txt", 'a')
                            sav_file.write(mol_name + '\n')
                        sav_file.close()
                    else:
                        element_name_text = "Sorry, this is not a compound"
                    element_desc_text = mol_desc
                
                if(clearbuttonrect.collidepoint(pos)):
                    simulation_atoms = []
                    element_name_text = "Press Combine to see if you've made a compound"
                    element_desc_text = ""
                
                if(menubuttonrect.collidepoint(pos)):
                    simulation_atoms = []
                    game_state = 0
                    
        
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
            pos = pygame.mouse.get_pos()
            infoRect = atom_info_img.get_rect()
            infoRect.x = pos[0]
            infoRect.y = pos[1]
            screen.blit(atom_info_img, infoRect)
        
        #drawring combine button
        screen.blit(combinebutton, combinebuttonrect)
        screen.blit(clearbutton, clearbuttonrect)
        screen.blit(menubutton, menubuttonrect)
        
        #text box shit
        element_text_obj = fontbig.render(element_name_text, True, black, white)
        screen.blit(element_text_obj, element_text_rect)

        #desc box
        element_desc_obj = font.render(element_desc_text, True, black, white)
        screen.blit(element_desc_obj, element_desc_rect)
        
        #making all redrawn things visible
        pygame.display.flip()
    
    
    while game_state == 2:
        #this is the help menu
        
        #exiting game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            
            #checking if they want to exit
            if(event.type == pygame.MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                if(backbuttonrect.collidepoint(pos)):
                    #now we go back to gamestate 0
                    game_state = 0
            
        
        screen.fill(black)
        screen.blit(helpscreenimage, helpscreenimagerect)
        screen.blit(backbutton, backbuttonrect)
        
        pygame.display.flip()
        
