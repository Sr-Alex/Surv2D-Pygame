import pygame

from assets.blocks import *


class Map:
    def __init__(self, surface, player) -> None:
        self.surface = surface
        self.player = player
        self.load_tiles()
        self.load_blocks()

        self.show_cartesian_map = True

    def load_blocks(self):
        self.blocks = {
            Grass_Block(self.surface).get_id(): Grass_Block(self.surface),
            Grass_blue_flower(self.surface).get_id(): Grass_blue_flower(self.surface),
            Grass_yellow_flower(self.surface).get_id(): Grass_yellow_flower(self.surface),
            Stone_block(self.surface).get_id(): Stone_block(self.surface),
            Rock_block(self.surface).get_id(): Rock_block(self.surface)
        }

    def load_tiles(self):
        self.file = open('Game/script/assets/map_matrix.txt', 'r')
        self.tiles_map = []
        for line in self.get_file():
            layer = list(data.strip().split(',') for data in line.strip().split(';'))
            self.tiles_map.append(layer)


    def render_map(self):
        for y, layer in enumerate(self.get_tiles_map()):
            for x, row in enumerate(layer):
                for z, tile in enumerate(row):
                    if int(tile) in self.blocks:

                        block = self.blocks[int(tile)]
                        block.set_position(self.to_isometric((x*(block.get_width()/2) - (y*(block.get_width()/2)) + 350, z*(block.get_height()/2) - (y*(block.get_height()/2)))))
                        self.surface.blit(block.get_sprite(),
                        block.get_position())
                            
                        if self.player.get_x() > block.get_x():
                            self.player.render()

                        if self.show_cartesian_map:
                            block = self.blocks[int(tile)]
                            pygame.draw.rect(self.surface, (255,255,255),
                            (pygame.Rect(z*20, x*20, 20, 20)), 1)

                        

    def to_isometric(self, location):
        isoX = location[0] - location[1]
        isoY = (location[0] + location[1])/2

        return (isoX, isoY)

    def switch_cartesian_map(self, key):
        if key == pygame.K_m:
            if self.show_cartesian_map:
                self.show_cartesian_map = False
            elif not self.show_cartesian_map:
                self.show_cartesian_map = True
        
    def get_file(self):
        return self.file
    
    def get_tiles_map(self):
        return self.tiles_map
