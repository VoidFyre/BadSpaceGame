import pygame
from model import Spaceship, Enemy, PowerUp
from view import SpaceshipView, EnemyView, PowerUpView, GameView

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_input(self, event):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.model.spaceship.move_left()
        if keys[pygame.K_RIGHT]:
            self.model.spaceship.move_right()
        if keys[pygame.K_SPACE]:
            self.model.spaceship.shoot()

    def update(self):
        self.model.update()

    def draw(self):
        self.view.draw(self.model)

    def check_collisions(self):
        for enemy in self.model.enemies:
            if pygame.sprite.collide_rect(self.model.spaceship, enemy):
                self.model.spaceship.hit(enemy.damage)
                self.model.enemies.remove(enemy)
                self.view.play_sound_effect('explosion')

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
                    self.view.play_sound_effect('explosion')
                    if enemy.health <= 0:
                        self.model.enemies.remove(enemy)
                        self.model.score += enemy.score_value
                        self.view.play_sound_effect('explosion')

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()
            self.update()
            self.check_collisions()
            self.draw()

            if self.model.game_over:
                running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
