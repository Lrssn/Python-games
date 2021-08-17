import pygame

class TextElement(object):
    def __init__(self, position, width, height, text, color):
        self.child_elements = list()
        self.position = position
        self.text = text
        self.color = color

        self.rect = pygame.Rect(position[0], position[1], width, height)
        

    def render(self, screen, text_renderer):
        # TODO: render current
        pygame.draw.rect(screen, self.color, self.rect)
        text_renderer.render(screen, self.text, (self.rect.left, self.rect.top ))
        for element in self.child_elements:
            element.render()

    def add_child_element(self, element):
        self.child_elements.append(element)

class FlatColorElement(object):
    def __init__(self, position, width, height, color):
        self.child_elements = list()
        self.position = position
        self.color = color

        self.rect = pygame.Rect(position[0], position[1], width, height)

    def render(self, screen):
        # TODO: render current
        pygame.draw.rect(screen, self.color, self.rect)
        
        for element in self.child_elements:
            element.render()

    def add_child_element(self, element):
        self.child_elements.append(element)