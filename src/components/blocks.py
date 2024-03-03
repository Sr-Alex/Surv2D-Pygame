import pygame

class Block: 
    def __init__(self, surface = None):
        self.surface = surface

        self.id = -1
        self.durability = 0.0

        self.size = self.width, self.height =  (90, 90)

    def render(self):
        self.box = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.surface.blit(self.sprite, self.box)

    # Getters & Setters
    def get_id(self) -> int:
        return self.id
    
    def get_sprite(self):
        return self.sprite
    
    def get_size(self) -> tuple:
        return self.size

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height
    
    def get_position(self) -> tuple:
        return self.position

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_durability(self) -> float:
        return self.durability
    
    def set_surface(self, surface):
        self.surface = surface

    def set_id(self, id):
        self.id = id

    def set_sprite(self, sprite):
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.get_sprite(), self.get_size())


    def set_size(self, size: tuple):
        self.size = self.width, self.height =  size
    
    def set_position(self, position: tuple):
        self.position = self.x, self.y = position

    def set_durability(self, durability):
        self.durability = durability


# Classes de Blocos

# Bloco de grama
class Grass_Block(Block):
    def __init__(self, surface):
        super().__init__(surface)

        self.set_id(1)
        self.set_sprite(pygame.image.load('src/images/grass_block.png').convert_alpha())

        self.set_durability(3)

# Bloco de grama com flores azuis
class Grass_blue_flower(Block):
    def __init__(self, surface):
        super().__init__(surface)

        self.set_id(2)
        self.set_sprite(pygame.image.load('src/images/grass_block_blue_flower.png').convert_alpha())

        self.set_durability(3)

# Bloco de grama com flores amarelas
class Grass_yellow_flower(Block):
    def __init__(self, surface):
        super().__init__(surface)

        self.set_id(3)
        self.set_sprite(pygame.image.load('src/images/grass_block_yellow_flower.png').convert_alpha())

        self.set_durability(3)
    
# Bloco de pedra
class Stone_block(Block):
    def __init__(self, surface):
        super().__init__(surface)

        self.set_id(4)
        self.set_sprite(pygame.image.load('src/images/stone_block.png').convert_alpha())
        
        self.set_durability(10)

class Rock_block(Block):
    def __init__(self, surface):
        super().__init__(surface)

        self.set_id(5)
        self.set_sprite(pygame.image.load('src/images/rock_block.png').convert_alpha())
        
        self.set_durability(14)