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
        self.info = open(info_loc, "r").read()
        self.image = pygame.image.load(image_loc)
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
