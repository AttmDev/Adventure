import pygame

from game_files.PPlay import window as win
from game_files.PPlay.gameimage import GameImage
from game_files.PPlay.sprite import Sprite
from game_files.scripts import player_manager as p, constants as c, hotbar as it, game_events, game_state as gs


class Control():
    def __init__(self, state):
        self.screen = win.Window(c.width, c.height)
        self.screen.set_title(c.TITTLE)
        self.mouse = self.screen.get_mouse()
        self.state_manager = state

        self.background = GameImage(c.BACKGROUND_IMAGE)

        self.titleImage = GameImage(c.MENU_TITTLE_IMAGE)
        self.titleImage.x = (c.width - self.titleImage.width) / 2
        self.titleImage.y = c.height / 12

        self.playButton = GameImage(c.MENU_PLAY_IMAGE[0]), GameImage(c.MENU_PLAY_IMAGE[1])
        for item in self.playButton:
            item.x = (c.width - item.width) / 2
            item.y = (c.height / 2)

        self.player = p.Player()
        self.inventory = it.Inventory()

        self.spike = Sprite("game_files/assets/spike.png") #TODO VAI SER CRIADA UMA CLASSE SPIKE E INSTANCIADA EM ENEMIES
        self.spike.x = 300
        self.spike.y = 100
        self.enemies = [self.spike] #TODO ADICIONAR A LISTA DE INIMIGOS NA CLASSE ENEMIES

    def __event_handle(self):
        #if [self.player.collided_perfect(x) for x in self.enemies]:
        for enemy in self.enemies:
            if self.player.collided_perfect(enemy):
                self.player.loseHp() #TODO VAI PERDER x.damage DE VIDA, CRIAR SELF.DAMAGE NAS CLASSES DE INIMIGOS

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.player.move_x(self.player.speed * self.screen.delta_time())
        elif key_pressed[pygame.K_LEFT]:
            self.player.move_x(-self.player.speed * self.screen.delta_time())
        elif key_pressed[pygame.K_UP]:
            self.player.move_y(-self.player.speed * self.screen.delta_time())
        elif key_pressed[pygame.K_DOWN]:
            self.player.move_y(self.player.speed * self.screen.delta_time())
            self.player.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == game_events.END_PLAYER_INVUL:
                self.player.invul_end()
            elif event.type == game_events.START_PLAYER_INVUL:
                self.player.invul_start()

    def draw(self, STATE):
        if STATE == 0:
            self.background.draw()
            self.titleImage.draw()

        elif STATE == 1:
            self.background.draw()
            self.inventory.draw()
            self.spike.draw()
            self.player.draw_and_update()

    def menuLoop(self):
        if self.mouse.is_over_object(self.playButton[0]):
            self.playButton[1].draw()
            if self.mouse.is_button_pressed(1):
                self.screen.clear()
                self.state_manager.set_state(1)
        else:
            self.playButton[0].draw()
        self.screen.update()

    def gameLoop(self):
        self.__event_handle()
        self.screen.update()


