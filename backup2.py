import pygame
import os
import random



time = 0


class Settings:
    window_width = 1000
    window_height = 800
    window_border = 75
    window_border2 = 0
    file_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(file_path, "images")
   
    
class Background(object):
    def __init__(self, filename):
        self.image = pygame.image.load(os.path.join(Settings.image_path, filename))
        self.image = pygame.transform.scale(self.image, (Settings.window_width, Settings.window_height)).convert()
        self.rect = self.image.get_rect()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect) 


    
class Bubble(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        bitmap = pygame.image.load(os.path.join(Settings.image_path, filename))
        self.image = bitmap.convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = (Settings.window_width - 75) // 2
        self.rect.bottom = Settings.window_height - Settings.window_border2 -10
        self.random1 = 0
        self.random2 = 0
        

        

    def update(self):
        newrect = self.rect.move(self.random1, self.random2)
        if newrect.top <= Settings.window_border2:
             self.move_stop()
        if newrect.bottom >= Settings.window_height - Settings.window_border2:
             self.move_stop()
        if newrect.left <= Settings.window_border2:
            self.move_stop()
        if newrect.right >= Settings.window_width - Settings.window_border2:
            self.move_stop()
        self.rect.move_ip(self.random1, self.random2)


    def move_random(self):
        self.rect.centerx = random.randint(75, 825)
        self.random1 = self.rect.centerx
        self.rect.bottom = random.randint(75, 625)
        self.random2 = self.rect.bottom

    def move_stop(self):
        self.random1 = 0
        self.random2 = 0


    

if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    

    
    background = Background("background2.png")
    bubble = Bubble("bubble.png")
    all_sprites.add(bubble)


    
    running = True
    while running:
        clock.tick(60)
        time = time +1
        if time == 120:
            time = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if time == 119:
            bubble.move_random()
         

        bubble.update()

        
        background.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
