import pygame, time

from game_files.scripts import battle_mode, bullet
from game_files.scripts.events import event_name


class Game_event_handler():

    def __init__(self, user_event):
        self.user_events_dispatcher = user_event
        self.battle = battle_mode.Battle(user_event)
        self.is_paused = False

    def run(self, delta_time, world):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            world.player.move_x(world.player.speed * delta_time)
            world.player.set_curr_frame(2)

        elif key_pressed[pygame.K_LEFT]:
            world.player.set_curr_frame(0)
            world.player.move_x(-world.player.speed * delta_time)

        if key_pressed[pygame.K_UP]:
            world.player.move_y(-world.player.speed * delta_time)
            world.player.set_curr_frame(1)

        elif key_pressed[pygame.K_DOWN]:
            world.player.move_y(world.player.speed * delta_time)
            world.player.set_curr_frame(3)

        if key_pressed[pygame.K_SPACE]:
            world.bullets.add_bullets(world.player)

        if key_pressed[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        # if key_pressed[pygame.K_RETURN]: #TODO ESSE PAUSE N FUNFA
        #     self.is_paused = True
        #
        # while self.is_paused:
        #     time.sleep(.25)
        #     key_pressed = pygame.key.get_pressed()
        #     if key_pressed[pygame.K_RETURN]:
        #         self.is_paused = False

        user_events = list(set(self.user_events_dispatcher.get_user_events()))
        for event in user_events:

            if event == event_name.START_PLAYER_INVUL:
                world.player.invul_start()

            elif event == event_name.END_PLAYER_INVUL:
                world.player.invul_end()

            elif event == event_name.DAMAGE_RECEIVED:
                world.player.loseHp(world.enemy_colliding.damage)

            elif event == event_name.DAMAGE_DEALT:
                world.enemy_colliding.lose_hp(world.player.damage)

            elif event == event_name.START_BULLET_TICK:
                world.bullets.tick_start()

            elif event == event_name.END_BULLET_TICK:
                world.bullets.tick_end()
