import pygame
import random
import math
import os

from model.GameState import GameState

from model.Enemy import Enemy
from model.Player import Player

from model.HealthAid import HealthAid

from view.MainMenuView import MainMenuView
from view.PauseMenuView import PauseMenuView
from view.GameOverMenuView import GameOverMenuView
from model.Upgrade import Upgrade

from model.SaveStats import SaveStats

from view.MovingBackgroundView import MovingBackgroundView


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


class GameController:
    def __init__(self, width, height):

        self.game_state = GameState(width, height)

        self.death = pygame.mixer.Sound(os.path.join("assets", "sounds/death.ogg"))

        self.player = Player(300, 680)
        self.player.set_game_state(self.game_state)
        self.player.set_player_ship()
        self.player.set_player_primary()
        self.player.set_player_secondary()
        self.player.set_player_thruster()

        self.mainMenuView = MainMenuView()
        self.mainMenuView.set_game_state(self.game_state)

        self.pauseMenuView = PauseMenuView()
        self.pauseMenuView.set_game_state(self.game_state)

        self.movingBackgroundView = MovingBackgroundView()
        self.movingBackgroundView.set_game_state(self.game_state)

        self.gameOverMenuView = GameOverMenuView()
        self.gameOverMenuView.set_game_state(self.game_state)

        self.saveStats = SaveStats(self.game_state)

        self.scroll = 0

    def reset_game_controller_by_restart(self, width=750, height=750):

        self.game_state.game_reset()

        self.player = Player(300, 680)
        self.player.set_game_state(self.game_state)
        self.player.set_player_ship()
        self.player.set_player_primary()
        self.player.set_player_secondary()
        self.player.set_player_thruster()

        #self.mainMenuView = MainMenuView()
        self.mainMenuView.set_game_state(self.game_state)

        #self.pauseMenuView = PauseMenuView()
        self.pauseMenuView.set_game_state(self.game_state)

        #self.movingBackgroundView = MovingBackgroundView()
        self.movingBackgroundView.set_game_state(self.game_state)

        #self.gameOverMenuView = GameOverMenuView()
        self.gameOverMenuView.set_game_state(self.game_state)

        self.saveStats = SaveStats(self.game_state)

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

    def random_enemy_shoot_and_collision_check(self):
        for enemy in self.game_state.enemies[:]:
            enemy.move(self.game_state.enemy_vel)
            enemy.move_lasers(self.game_state.laser_vel, self.player)

            # Only allow enemy to shoot if it is on screen and with a certain probability
            if enemy.y > 0 and random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, self.player):

                if enemy.rarity == "common" or enemy.rarity == "uncommon":
                    self.player.health -= self.player.max_health / 3
                if enemy.rarity == "rare":
                    self.player.health -= self.player.max_health / 2
                if enemy.rarity == "epic":
                    self.player.health -= (self.player.max_health / 3) * 2
                if enemy.rarity == "legendary":
                    self.player.health -= (self.player.max_health / 4) * 3
                enemy.health = 0
                
            elif enemy.y + enemy.get_height() > 750:
                self.game_state.enemies.remove(enemy)

    def random_health_move_and_collision_check(self):
        for healthAid in self.game_state.healthAids[:]:
            healthAid.move(self.game_state.healthAids_vel)
            #healthAid.move_lasers(self.game_state.laser_vel, self.player)

            # Only allow enemy to shoot if it is on screen and with a certain probability
            if collide(healthAid, self.player):

                healthAid.play_sound()

                self.player.health += self.player.max_health / 5

                if self.player.health > self.player.max_health:
                    self.player.health = self.player.max_health

                self.game_state.healthAids.remove(healthAid)

            elif healthAid.y + healthAid.get_height() > 750:
                self.game_state.healthAids.remove(healthAid)

    def random_upgrade_move_and_collision_check(self):
        for upgrade in self.game_state.upgrades[:]:
            if upgrade.orb_type == 'common':
                self.game_state.upgrades.remove(upgrade)
            upgrade.move(self.game_state.upgrades_vel)
            if collide(upgrade, self.player):

                upgrade.play_sound()
                
                upgrade.reward_player(upgrade.orb_type, self.game_state, self.player)

                self.game_state.upgrades.remove(upgrade)

    def update_game_status(self):
        # if self.game_state.lives <= 0 or self.player.health <= 0:

        if self.player.health <= 0:
            self.game_state.lost = True
            self.game_state.lost_count += 1

    def get_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def spawn_random_enemy(self):
        if len(self.game_state.enemies) == 0:
            self.game_state.level += 1
            self.game_state.wave_length += 5
            for i in range(self.game_state.wave_length):
                if self.game_state.level < 5:
                    choice = random.choice(["common", "uncommon"])
                if self.game_state.level >= 5 and self.game_state.level < 10:
                    choice = random.choice(["common", "uncommon", "rare"])
                if self.game_state.level >= 10 and self.game_state.level < 15:
                    choice = random.choice(["common", "uncommon", "rare", "epic"])
                if self.game_state.level >= 15:
                    choice = random.choice(["common", "uncommon", "rare", "epic", "legendary"])
                enemy = Enemy(random.randrange(50, 750 - 100), random.randrange(-1500, -10), choice, self.game_state.level)
                # Check the distance between each existing enemy and the new enemy being created
                is_valid_position = True
                for existing_enemy in self.game_state.enemies:
                    if self.get_distance(existing_enemy.x, existing_enemy.y, enemy.x, enemy.y) < 50:
                        is_valid_position = False
                        break
                # If the position is valid, add the enemy to the game state
                if is_valid_position:
                    self.game_state.enemies.append(enemy)

    def spawn_random_health_aids(self):
        if len(self.game_state.healthAids) == 0:
            self.game_state.level += 1
            self.game_state.wave_length = random.randrange(0,5)
            for i in range(self.game_state.wave_length):
                heathAid = HealthAid(random.randrange(50, 750 - 100), random.randrange(-1500, -10))
                # Check the distance between each existing enemy and the new enemy being created
                is_valid_position = True
                for existing_healthAid in self.game_state.healthAids:
                    if self.get_distance(existing_healthAid.x, existing_healthAid.y, heathAid.x, heathAid.y) < 100:
                        is_valid_position = False
                        break
                # If the position is valid, add the enemy to the game state
                if is_valid_position:
                    self.game_state.healthAids.append(heathAid)

    def redraw_window(self):

        #self.game_state.window.blit(self.game_state.BG, (0, self.scroll))

        self.movingBackgroundView.run()

        # draw text
        level_label = self.game_state.main_font.render(f"WAVE: {self.game_state.level}", 1, (255, 255, 255))

        self.game_state.window.blit(level_label, (self.game_state.DISPLAY_W - level_label.get_width() - 10, 10))

        # Draw the kill count and score on the top-left corner of the screen
        kill_label = self.game_state.main_font.render(f"Kills: {self.game_state.total_killing}", 1, (255, 255, 255))
        score_label = self.game_state.main_font.render(f"Score: {self.game_state.score_counter}", 1, (255, 255, 255))

        # Blit the labels onto the screen
        self.game_state.window.blit(kill_label, (15, 15))
        self.game_state.window.blit(score_label, (125, 15))

        for enemy in self.game_state.enemies:
            enemy.draw(self.game_state.window)

        for health in self.game_state.healthAids:
            health.draw(self.game_state.window)

        for explosion in self.game_state.explosions:
            explosion.draw(self.game_state.window)
        
        for upgrades in self.game_state.upgrades:
            upgrades.draw(self.game_state.window)

        self.player.draw(self.game_state.window)

        pygame.display.update()

    def clean_up(self):
        for explosion in self.game_state.explosions[:]:
            if abs(explosion.explosion_shoot_timer - pygame.time.get_ticks()) >= 200:
                self.game_state.explosions.remove(explosion)

    def enemy_check(self):
        for enemy in self.game_state.enemies:
            if enemy.health <= 0:
                self.death.play()
                x = enemy.x
                y = enemy.y

                if enemy.rarity != "common":
                    newUpgrade = Upgrade()
                    newUpgrade.x = x
                    newUpgrade.y = y
                    newUpgrade.orb_type = newUpgrade.summon_random_orb(enemy.rarity)
                    if newUpgrade.orb_type != None:
                        self.game_state.upgrades.append(newUpgrade)

                self.player.track_score_and_kills(enemy)

                self.player.create_ship_explosion(enemy)
                self.game_state.enemies.remove(enemy)

    def draw_game_stats(self):

        self.saveStats.end_game()

        # Generate a random RGB color
        color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

        # Draw the kill count and score using the random color
        kill_label = self.game_state.main_font.render(f"Kills: {self.game_state.total_killing}", 1, color)
        score_label = self.game_state.main_font.render(f"Score: {self.game_state.score_counter}", 1, color)
        best_kill_label = self.game_state.main_font.render(
            f"Best Kills: {self.game_state.high_total_killing}", 1, color)
        best_score_label = self.game_state.main_font.render(
            f"Best Score: {self.game_state.high_score_counter}", 1, color)

        # Blit the labels onto the screen
        self.game_state.window.blit(kill_label, (200, 210))
        self.game_state.window.blit(score_label, (400, 210))
        self.game_state.window.blit(best_kill_label, (200, 260))
        self.game_state.window.blit(best_score_label, (400, 260))

        pygame.display.update()

    def run_game_loop(self):

        self.game_state.enable_music()

        while self.game_state.running:

            while self.game_state.lost is True:
                self.draw_game_stats()
                self.gameOverMenuView.run()
                if self.game_state.current_menu_button == "Restart":
                    self.reset_game_controller_by_restart()

            while self.game_state.playing is False and self.game_state.pause is False:
                self.mainMenuView.run()
                if self.game_state.current_menu_button == "Play":
                    self.reset_game_controller_by_restart()

            while self.game_state.playing is False and self.game_state.pause is True:
                self.pauseMenuView.run()
                if self.game_state.current_menu_button == "Restart":
                    self.reset_game_controller_by_restart()

            while self.game_state.playing:

                self.game_state.check_events()

                self.game_state.clock.tick(self.game_state.FPS)

                self.check_key_pressed()

                self.update_game_status()

                self.spawn_random_enemy()

                self.random_enemy_shoot_and_collision_check()

                self.spawn_random_health_aids()

                self.random_health_move_and_collision_check()

                self.player.move_primary_proj(-self.game_state.laser_vel, self.game_state.enemies)

                self.player.move_secondary_proj(-self.game_state.laser_vel, self.game_state.enemies)

                self.random_upgrade_move_and_collision_check()

                self.player.move_lasers(-self.game_state.laser_vel, self.game_state.enemies)

                self.redraw_window()

                self.enemy_check()

                self.clean_up()

                self.player.set_game_state(self.game_state)

                if self.game_state.lost:
                    self.game_state.playing = False





