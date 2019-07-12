#!/usr/bin/env python3

"""
Atom class
Oh look a docstring! Richard Lobb would be proud
"""

class Atom():
    def init(name, proton, neutron, electron, info=""):
        """Constructor for class Atom"""
        self.name = name
        self.proton = proton
        self.neutron = neutron
        self.electron = electron
        self.info = info

    def combine(atoms):
        """function handling what happens when 2 or more atoms
        are combined

        Return: new combined Atom object
        """
        pass
