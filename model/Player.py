import pygame

import os

from model.Spaceship import Spaceship


class Player(Spaceship):
    def __init__(self, x, y, health=20):
        super().__init__(x, y, health)

        # Images

        self.ship_img  = pygame.image.load(os.path.join("assets", "component/ship/ship_common.png"))
        self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_common.png"))
        self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_common.png"))
        self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_common.png"))
        self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))
        self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_common.png"))
        self.laser_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))

        ship_mask = pygame.mask.from_surface(self.ship_img)

        self.mask = ship_mask
        

        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
