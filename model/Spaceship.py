from model.Laser import Laser
import pygame
import os


class Spaceship:

    def __init__(self, x, y, health, ship_img):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = ship_img
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        self.primary_cool_down_counter = 0
        self.secondary_cool_down_counter = 0
        self.laser_size = (64, 64)
        self.primary_proj_size = (64, 64)
        self.secondary_proj_size = (32, 32)
        self.shoot_sound = pygame.mixer.Sound(os.path.join("assets", "sounds/laser_fire.ogg"))

        self.laser_dmg = 10

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= self.laser_dmg
                self.lasers.remove(laser)

    def cooldown(self):

        if self.cool_down_counter > 0:
            self.cool_down_counter -= 1

        if self.primary_cool_down_counter > 0:
            self.primary_cool_down_counter -= 1

        if self.secondary_cool_down_counter > 0:
            self.secondary_cool_down_counter -= 1

    def shoot(self):
        if self.cool_down_counter == 0:
            self.shoot_sound.play()
            laser = Laser(self.x-12, self.y-18, self.laser_img, self.laser_size)
            self.lasers.append(laser)
            self.cool_down_counter = 30

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()