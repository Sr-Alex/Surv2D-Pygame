# Um jogo 2D de sobrevivência com estilo isométrico;
# O jogador é capaz de interagir com quase tudo dentro do game,
# dando liberdade para criação e destruição de estruturas.

import pygame

from src.components.map import Map
from src.components.player import Player

class Surv_App:
    def __init__(self) -> None:
        self.running = True
        self.size = self.width, self.height = 800,600
        self.window_surf = pygame.display.set_mode(self.size)

        self.on_init()

    # on_init -------> Ao iniciar jogo
    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Surv2D')

        self.player = Player(self.window_surf)
        self.world = Map(self.window_surf, self.player)

    # on_event -------> Para cada evento no jogo
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        # Ao teclar uma única vez  
        if event.type == pygame.KEYDOWN:
            self.world.switch_cartesian_map(event.key)

    # on_loop -------> Em cada ciclo
    def on_loop(self):
        self.on_keyPressed()
        
        pygame.display.update()
        pygame.time.Clock().tick(60)

    # render -------> Renderizar objetos
    def render(self):
        self.window_surf.fill((30,30,50))

        self.world.render_map()        
    # on_exit -------> Ao fechar a tela do jogo
    def on_exit(self):
        pygame.quit() 

    # run -------> Fluxo do jogo
    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.render()
            self.on_loop()

        self.on_exit()

    # on_keyPressed -------> Ao manter tecla pressionada
    def on_keyPressed(self):
        keys = pygame.key.get_pressed()
        
        self.player.walk(keys)

surv_game = Surv_App()
surv_game.run()