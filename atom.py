#!/usr/bin/env python3
import pygame
"""
Atom class
Oh look a docstring! Richard Lobb would be proud
"""

class Atom():
    def __init__(self, name, proton, neutron, electron, image_loc, info_loc=""):
        """Constructor for class Atom"""
        self.name = name
        self.proton = proton
        self.neutron = neutron
        self.electron = electron
        self.image_loc = image_loc
        self.info_loc = info_loc
        try:
            self.info = pygame.image.load(info_loc)
        except pygame.error as e:
            self.info = ""
        try:
            self.image = pygame.image.load(image_loc)
        except pygame.error as e:
            self.image = pygame.image.load("assets/img/oxygen.png")
        self.rect = self.image.get_rect()

    def combine(self, atoms):
        """function handling what happens when 2 or more atoms
        are combined

        Return: new combined Atom object
        """
        pass 
    
    def is_positive(self):
        """determines whether an atom is positively charged
        Return: True if positive False otherwise
        """
        return (self.proton - self.neutron) > 0

    def __lt__(self, other):
        """decides whether another atom is "less" than this atom
        comparison is done alphabetically on their name
        """
        return self.name < other.name
