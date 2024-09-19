import pygame

pygame.init()

BLUE = pygame.Color("blue")
PINK = pygame.Color("pink")
RED = pygame.Color("red")


class ImmSprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [1,0]
    
    def update(self):
        flag = 0
        print(self.rect.bottom)
        self.rect.move_ip(self.velocity)
        if (self.rect.right <= 19):
            flag = 1
            self.velocity[0] = -self.velocity[0] 
            self.rect.move_ip(self.velocity)
        if (self.rect.left >= 500 - 19):
            flag = 1
            self.velocity[0] = -self.velocity[0] 
            self.rect.move_ip(self.velocity)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,colour,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [0,-1]
    
    def update(self):
        flag = 0
        print(self.rect.bottom)
        self.rect.move_ip(self.velocity)
        if (self.rect.top <= 0):
            flag = 1
            self.velocity[1] = -self.velocity[1] 
            self.rect.move_ip(self.velocity)
        if (self.rect.top >= 500):
            flag = 1
            self.velocity[1] = -self.velocity[1] 
            self.rect.move_ip(self.velocity)
                
            
all_spr_lst = pygame.sprite.Group()
        
surface1 = pygame.display.set_mode((500,500))
pygame.display.set_caption("Movable Sprites")
bg_color = PINK
surface1.fill(bg_color)

all_spr_lst = pygame.sprite.Group()
sp1 = Sprite(RED,20,30)
sp2 = ImmSprite(BLUE,20,30)
sp1.rect.x = 230.0
sp1.rect.y = 230.0
sp2.rect.x = 230.0
sp2.rect.y = 230.0
all_spr_lst.add(sp1)
all_spr_lst.add(sp2)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    all_spr_lst.update()
    surface1.fill(bg_color)
    all_spr_lst.draw(surface1)
    
    
    pygame.display.flip()
    clock.tick(240)

pygame.quit()   