from PPlay import window as win
from PPlay.gameimage import *
import playerStuff as p
import constants as c
import item as it



class Control():
    def __init__(self):
        self.screen = win.Window(c.width, c.height)
        self.screen.set_title(c.title)
        self.mouse = self.screen.get_mouse()

        self.background = GameImage(c.backgroundImage)

        self.titleImage = GameImage(c.menuTitleImage)
        self.titleImage.x = (c.width - self.titleImage.width) / 2
        self.titleImage.y = c.height / 12

        self.playButton = GameImage(c.playButtonImage[0]), GameImage(c.playButtonImage[1])
        for item in self.playButton:
            item.x = (c.width - item.width) / 2
            item.y = (c.height / 2.2)

        self.player = p.Player()
        self.inventory = it.Inventory()
        self.menuLoop()


    def menuLoop(self):
        while True:
            self.background.draw()
            self.titleImage.draw()
            if self.mouse.is_over_object(self.playButton[0]):
                self.playButton[1].draw()
                if self.mouse.is_button_pressed(1):
                    self.screen.clear()
                    self.gameLoop()
            else:
                self.playButton[0].draw()
            self.screen.update()


    def gameLoop(self):
        while True:
            self.background.draw()
            self.inventory.draw()
            self.player.move_key_x(1)
            self.player.move_key_y(1)
            self.player.drawPlayerStuff()
            self.screen.update()










"""



def menuLoop():
    global screen, background, playButton, titleImage, mouse
    while True:
        background.draw()
        titleImage.draw()
        if mouse.is_over_object(playButton[0]):
            playButton[1].draw()
            if mouse.is_button_pressed(1):
                screen.clear()
                gameLoop()
        else:
            playButton[0].draw()
        screen.update()

def start():
    global screen, background, player, titleImage, playButton, mouse, lifeBar, lifeUnits, hp
    screen = win.Window(c.width, c.height)
    screen.set_title(c.title)
    mouse = screen.get_mouse()


    background = GameImage(c.backgroundImage)

    titleImage = GameImage(c.menuTitleImage)
    titleImage.x = (c.width - titleImage.width) / 2
    titleImage.y = c.height / 12

    playButton = GameImage(c.playButtonImage[0]), GameImage(c.playButtonImage[1])
    for item in playButton:
        item.x = (c.width - item.width)/2
        item.y = (c.height/2.2)

    hp = 11
    lifeBar = GameImage(c.lifeBarImage)
    lifeBar.x = (c.width - lifeBar.width) / 2
    lifeBar.y = c.height - lifeBar.height - c.height/72
    lifeUnits = [GameImage(c.lifeUnitImage) for i in range(11)]
    lifeUnits[0].x = lifeBar.x
    lifeUnits[0].y = lifeBar.y
    for i in range(1, 11):
        lifeUnits[i].y = lifeBar.y
        lifeUnits[i].x = lifeUnits[i-1].x + lifeUnits[i].width


    player = GameImage(c.soldierImage)

    menuLoop()





def gameLoop():
    global screen, background, player, lifeBar, lifeUnits
    hp = 11
    while True:
        background.draw()
        player.draw()
        lifeBar.draw()
        tick = True
        if mouse.is_button_pressed(2) and tick:
            hp-=1
            tick = False
        for i in range(hp):
            lifeUnits[i].draw()
        screen.update() """