import pygame


class Player:

    def __init__(self,surface):

        self.surface = surface

        self.set_sprite('player_east_north')

        self.flipX, self.flipY = False, False


        self.size = self.width, self.height = (50, 80)

        self.spawned = True


        self.__origin = (self.surface.get_width()/2 - self.size[0]/2), (self.surface.get_height()/2 - self.size[1]/2)

        self.__position = self.x, self.y = self.get_origin()

        self.__layer = 1


        self.__speed = [2, 2]

        self.__health = 20


        self.__can_walk = True

    def render(self):

        if self.spawned:

            self.box = pygame.Rect(self.get_position()[0], self.get_position()[1], self.size[0], self.size[1])

            self.surface.blit(self.sprite, self.to_isometric(self.get_position()))


    def destroy(self):

        if self.spawned == True:

            self.spawned = False


    def walk(self, key):

        if self.__can_walk:

            if key[pygame.K_w]:

                self.set_position((self.x - self.get_speed()[0], self.y))

                self.set_sprite('player_west_south')

                self.flip_sprite(False)
                print(self.get_position())


            if key[pygame.K_s]:

                self.set_position((self.x + self.get_speed()[0], self.y))

                self.set_sprite('player_east_north')

                self.flip_sprite(True)
                print(self.get_position())


            if key[pygame.K_a]:

                self.set_position((self.x, self.y + self.get_speed()[1]))

                self.set_sprite('player_east_north')

                self.flip_sprite(False)
                print(self.get_position())


            if key[pygame.K_d]:

                self.set_position((self.x, self.y - self.get_speed()[1]))

                self.set_sprite('player_west_south')

                self.flip_sprite(True)
                print(self.get_position())
                                

    def to_isometric(self, location):

        isoX = location[0] - location[1]

        isoY = (location[0] + location[1])/2


        return (isoX, isoY)


    #Getters & Setters

    def get_health(self) -> int:

        return self.__health


    def get_speed(self) -> list:

        return self.__speed


    def get_origin(self) -> tuple:

        return self.__origin

    def get_sprite(self):

        return self.sprite


    def get_can_walk(self) -> bool:

        return self.__can_walk


    def get_position(self) -> tuple:

        return self.__position
    

    def get_layer(self) -> int:

        return self.__layer


    def get_x(self) -> float:

        return self.x


    def get_y(self) -> float:

        return self.y
    

    def get_size(self) -> tuple:

        return self.size


    def get_width(self) -> int:

        return self.width


    def get_height(self) -> int:

        return self.height



    def set_health(self, health: int):

        self.__health = health


    def set_speed(self, speed: list):

        self.__speed = speed


    def set_origin(self, origin: tuple):

        self.__origin = (origin[0] - self.width/2), (origin[1] - self.height/2)


    def set_can_walk(self, can_walk):

        self.__can_walk = can_walk


    def set_position(self, position: tuple):

        self.__position = self.x, self.y = position


    def set_layer(self, layer):

        self.__layer = layer


    def set_size(self, size: tuple):

        self.size = size


    def set_width(self, width: int):

        self.width = width


    def set_height(self, height: int):

        self.height = height



    def set_sprite(self, filename):

        self.sprite = pygame.image.load(f'src/images/{filename}.png')

        self.sprite = pygame.transform.scale(self.sprite, (60,60))
    

    def flip_sprite(self, flipX: bool, flipY: bool = False):

        if flipX:

            self.sprite = pygame.transform.flip(self.get_sprite(),True, False)

            self.flipX = flipX

        elif flipY:

            self.sprite = pygame.transform.flip(self.get_sprite(),False, True)

            self.flipY = flipY