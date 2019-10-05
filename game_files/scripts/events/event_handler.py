import pygame

from game_files.scripts import battle_mode
from game_files.scripts.events import event_name


class Game_event_handler():

    def __init__(self, user_event):
        self.user_events_dispatcher = user_event
        self.battle = battle_mode.Battle(user_event)

    def run(self, delta_time, world):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            world.player.move_x(world.player.speed * delta_time)
            world.player.set_curr_frame(2)

        elif key_pressed[pygame.K_LEFT]:
            world.player.set_curr_frame(0)
            world.player.move_x(-world.player.speed * delta_time)

        elif key_pressed[pygame.K_UP]:
            world.player.move_y(-world.player.speed * delta_time)
            world.player.set_curr_frame(1)

        elif key_pressed[pygame.K_DOWN]:
            world.player.move_y(world.player.speed * delta_time)
            world.player.set_curr_frame(3)


        user_events = list(set(self.user_events_dispatcher.get_user_events()))
        for event in user_events:

            if event == event_name.START_PLAYER_INVUL:
                world.player.invul_start()

            elif event == event_name.END_PLAYER_INVUL:
                world.player.invul_end()

            elif event == event_name.START_BATTLE:
                #TODO MUDAR STATE//
                self.battle.run()

            elif event == event_name.DAMAGE_RECEIVED:
                world.player.loseHp(world.enemy_colliding.damage)

            elif event == event_name.DAMAGE_DEALT:
                world.enemy_colliding.lose_hp(world.player.damage)




