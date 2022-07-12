from time import sleep
import pygame

class Visualizer:
    def __init__(self, screen_width=400, screen_height=400, dot_color=[255,255,255], dot_size=1, bg_color=[0,0,0]) -> None:
        
        self.screen_size = (screen_width, screen_height)
        self.dot_color = dot_color
        self.dot_size = dot_size
        self.bg_color = bg_color
        
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(self.bg_color)
    
    def init_elements(self,sorting_list:list) -> None:
        for index, element in enumerate(sorting_list):
            pygame.draw.circle(self.screen, self.dot_color, [element, index], self.dot_size, 0)
    
    def update_state(self, sorting_list:list) -> None:
        self.screen.fill(self.bg_color)
        
        for index, element in enumerate(sorting_list):
            pygame.draw.circle(self.screen, self.dot_color, [element, index], self.dot_size, 0)
        
        pygame.display.flip()
        sleep(0.005)
