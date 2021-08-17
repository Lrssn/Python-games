import pygame
from utils.gui_element import *
from utils.text_renderer import *

class Gui_handler(object):
    def __init__(self):
        self.elements = list()
        self.text_renderer = Text_renderer()

    def render(self, screen):
        for element in self.elements:
            element.render(screen, self.text_renderer)

    def add_element(self, element):
        self.elements.append(element)

    def load_gui(self, gui):
        #read Xml File with gui information
        print("Load gui is not yet implemented")