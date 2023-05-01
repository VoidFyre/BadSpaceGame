import pygame
import random
import os
from model.Enemy import Enemy
from model.Player import Player

from view.MainMenuView import MainMenuView
from view.PauseMenuView import PauseMenuView

from view.MovingBackgroundView import MovingBackgroundView


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class GameController:
    def __init__(self, game_state, model, view):
        self.death = pygame.mixer.Sound(os.path.join("assets", "sounds/death.ogg"))

        self.model = model
        self.view = view
        self.game_state = game_state

        self.player = Player(300, 680)

        self.mainMenuView = MainMenuView()
        self.mainMenuView.set_game_state(self.game_state)

        self.pauseMenuView = PauseMenuView()
        self.pauseMenuView.set_game_state(self.game_state)

        self.movingBackgroundView = MovingBackgroundView()
        self.movingBackgroundView.set_game_state(self.game_state)

        self.scroll = 0

    def check_key_pressed(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if keys[pygame.K_a] and self.player.x - self.game_state.player_vel > 0:  # left
            self.player.x -= self.game_state.player_vel
        if keys[
            pygame.K_d] and self.player.x + self.game_state.player_vel + self.player.get_width() < self.game_state.DISPLAY_W:  # right
            self.player.x += self.game_state.player_vel
        if keys[pygame.K_w] and self.player.y - self.game_state.player_vel > 0:  # up
            self.player.y -= self.game_state.player_vel
        if keys[
            pygame.K_s] and self.player.y + self.game_state.player_vel + self.player.get_height() + 15 < self.game_state.DISPLAY_H:  # down
            self.player.y += self.game_state.player_vel
        if mouse[0]:
            self.player.shoot_primary()
        if mouse[2]:
            self.player.shoot_secondary()
        if keys[pygame.K_ESCAPE]:
            self.game_state.pause = True
            self.game_state.playing = False


    def update(self):
        self.model.update()

    def draw(self):
        self.view.draw(self.model)

    def generate_random_enemy(self):
        for enemy in self.game_state.enemies[:]:
            enemy.move(self.game_state.enemy_vel)
            enemy.move_lasers(self.game_state.laser_vel, self.player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, self.player):
                self.player.health -= 10
                self.game_state.enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > 750:
                self.game_state.lives -= 1
                self.game_state.enemies.remove(enemy)

    def update_dashboard(self):
        if self.game_state.lives <= 0 or self.player.health <= 0:
            self.game_state.lost = True
            self.game_state.lost_count += 1

        if len(self.game_state.enemies) == 0:
            self.game_state.level += 1
            self.game_state.wave_length += 5
            for i in range(self.game_state.wave_length):
                enemy = Enemy(random.randrange(50, 750 - 100), random.randrange(-1500, -100),
                              random.choice(["red", "blue", "green"]))
                self.game_state.enemies.append(enemy)

    def check_collisions(self):
        for enemy in self.model.enemies:
            if pygame.sprite.collide_rect(self.model.spaceship, enemy):
                self.model.spaceship.hit(enemy.damage)
                self.model.enemies.remove(enemy)
                self.death.play()

        for powerup in self.model.powerups:
            if pygame.sprite.collide_rect(self.model.spaceship, powerup):
                powerup.apply_effect(self.model.spaceship)
                self.model.powerups.remove(powerup)
                self.view.play_sound_effect('powerup')

        for bullet in self.model.spaceship.bullets:
            for enemy in self.model.enemies:
                if pygame.sprite.collide_rect(bullet, enemy):
                    enemy.hit(bullet.damage)
                    self.model.spaceship.bullets.remove(bullet)
                    self.death.play()
                    if enemy.health <= 0:
                        self.model.enemies.remove(enemy)
                        self.model.score += enemy.score_value
                        self.death.play()

    def redraw_window(self):

        #self.game_state.window.blit(self.game_state.BG, (0, self.scroll))

        self.movingBackgroundView.run()

        # draw text
        lives_label = self.game_state.main_font.render(f"Lives: {self.game_state.lives}", 1, (255, 255, 255))
        level_label = self.game_state.main_font.render(f"Level: {self.game_state.level}", 1, (255, 255, 255))

        self.game_state.window.blit(lives_label, (10, 10))
        self.game_state.window.blit(level_label, (self.game_state.DISPLAY_W - level_label.get_width() - 10, 10))

        for enemy in self.game_state.enemies:
            enemy.draw(self.game_state.window)

        self.player.draw(self.game_state.window)

        self.game_state.window.blit(self.player.ship_img, (self.player.x, self.player.y))
        self.game_state.window.blit(self.player.primary_img, (self.player.x, self.player.y))
        self.game_state.window.blit(self.player.secondary_img, (self.player.x, self.player.y))
        self.game_state.window.blit(self.player.thruster_img, (self.player.x, self.player.y))

        if self.game_state.lost:
            lost_label = self.game_state.lost_font.render("You Lost!!", 1, (255, 255, 255))
            self.game_state.window.blit(lost_label, (750 / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    def run_game_loop(self):
        pygame.mixer.music.load(os.path.join("assets", "sounds/background_music.ogg"))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        while self.game_state.running:

            while self.game_state.playing is False and self.game_state.pause is False:
                self.mainMenuView.run()

            while self.game_state.playing is False and self.game_state.pause is True:
                self.pauseMenuView.run()

            while self.game_state.playing:

                self.game_state.check_events()

                self.game_state.clock.tick(self.game_state.FPS)

                if len(self.game_state.enemies) == 0:
                    self.game_state.level += 1
                    self.game_state.wave_length += 5
                    for i in range(self.game_state.wave_length):

                        choice = random.choice(["common", "uncommon", "rare", "epic", "legendary"])
                        enemy = Enemy(random.randrange(50, 750 - 100), random.randrange(-1500, -10),
                                      choice)
                        self.game_state.enemies.append(enemy)

                self.redraw_window()

                self.check_key_pressed()

                self.generate_random_enemy()

                self.player.move_lasers(-self.game_state.laser_vel, self.game_state.enemies)

                self.update_dashboard()

                if self.game_state.lost:
                    self.game_state.playing = False





