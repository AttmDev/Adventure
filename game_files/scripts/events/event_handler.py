from threading import Timer

import pygame, time

from game_files.scripts import battle_mode, bullet
from game_files.scripts.events import event_name


class Game_event_handler():

    def __init__(self, user_event):
        self.user_events_dispatcher = user_event
        self.battle = battle_mode.Battle(user_event)
        self.is_paused = False
        self.activate_shotgun = False

        self.bullet_params = [350, 1, 15]

    def randomize_shot(self, world, activated, direc):
        if activated:
            shot = []
            i = 1
            speed = 50
            for i in range(0, 3):
                result = [self.bullet_params[0]-speed-25, 5 - i, 10*i, direc]
                shot.append(result)
                result = [self.bullet_params[0] - speed, self.bullet_params[1]+i, 10*i, direc]
                shot.append(result)
                # result = [self.bullet_params[0] - speed + 15, 5 - i, 4 * i]
                # shot.append(result)
                # result = [self.bullet_params[0] - speed, self.bullet_params[1] + i, 5 * i]
                # shot.append(result)
                i+=1
                speed+=30

            for param in shot:
                # print(shot)
                world.bullets.add_bullets(world.player, *param)
        else:
            world.bullets.add_bullets(world.player, direction=direc)

    def end_timer(self):
        self.activate_shotgun = False

    def run(self, delta_time, world):

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            world.player.set_curr_frame(2)
            world.player.move_x(world.player.speed * delta_time)
        elif key_pressed[pygame.K_a]:
            world.player.set_curr_frame(0)
            world.player.move_x(-world.player.speed * delta_time)

        if key_pressed[pygame.K_w]:
            world.player.move_y(-world.player.speed * delta_time)
            world.player.set_curr_frame(1)
        elif key_pressed[pygame.K_s]:
            world.player.move_y(world.player.speed * delta_time)
            world.player.set_curr_frame(3)




        if key_pressed[pygame.K_RIGHT]:
            world.player.set_curr_frame(2)
            self.randomize_shot(world, self.activate_shotgun, 2)
            # world.bullets.add_bullets(world.player, *self.bullet_params)
        elif key_pressed[pygame.K_LEFT]:
            world.player.set_curr_frame(0)
            self.randomize_shot(world, self.activate_shotgun, 0)
            # world.bullets.add_bullets(world.player, *self.bullet_params)
        if key_pressed[pygame.K_UP]:
            self.randomize_shot(world, self.activate_shotgun, 1)
            world.player.set_curr_frame(1)
            # world.bullets.add_bullets(world.player, *self.bullet_params)
        elif key_pressed[pygame.K_DOWN]:
            self.randomize_shot(world, self.activate_shotgun, 3)
            world.player.set_curr_frame(3)
            # world.bullets.add_bullets(world.player, *self.bullet_params)

        if key_pressed[pygame.K_SPACE]:
            world.item_manager.use_item(world.player, world.bullets)

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

            elif event == event_name.START_ITEM_USED:
                world.item_manager.tick_start()

            elif event == event_name.END_ITEM_USED:
                world.item_manager.tick_end()

            elif event == event_name.SHOTGUN_BEGIN:
                self.activate_shotgun = True
                t = Timer(10, self.end_timer)
                t.start()


            elif event == event_name.ROUND_INCREMENT:
                world.incrementRound()