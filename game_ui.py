import pygame


class game_ui(object):
    def __init__(self):
        self.font = pg.font.Font(SysFont, 20)
        self.text = 'SCORE COINS WORLD TIME LIVES'
        
    def render(self, main):
    x = 10
    for word in self.text.split(' '):
        rect = self.font.render(word, False, (255, 255, 255))
        core.screen.blit(rect, (x, 0))
        x += 168
        
    text = self.font.render(str(main.get_map().get_player().score), False, (255, 255, 255))
    rect = text.get_rect(center=(60, 35))
    main.screen.blit(text, rect)
    
    text = self.font.render(str(main.get_map().get_player().coins), False, (255, 255, 255))
    rect = text.get_rect(center=(230,35))
    main.screen.blit(text, rect)
    
    text = self.font.render(main.get_map().get_name(), False, (255, 255, 255))
    rect = text.get_rect(center=(395,35))
    main.screen.blit(text, rect)
    
    text = self.font.render(str(main.get_map().time), False, (255, 255, 255))
    rect = text.get_rect(center=(557,35))
    main.screen.blit(text, rect)
    
    text = self.font.render(str(main.get_map().get_player().num_lives), False, (255, 255, 255))
    rect = text.get_rect(center=(730,35))
    main.screen.blit(text, rect)