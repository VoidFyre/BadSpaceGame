import pygame

import os

from model.Spaceship import Spaceship


class Player(Spaceship):
    def __init__(self, x, y):
        

        # Images

        self.game_state = None

        self.ship_img  = pygame.image.load(os.path.join("assets", "component/ship/ship_common.png"))
        self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_common.png"))
        self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_common.png"))
        self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_common.png"))
        self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))
        self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_common.png"))
        self.laser_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))

        self.primary_damage = 100
        self.secondary_damage = 200

        ship_mask = pygame.mask.from_surface(self.ship_img)

        self.mask = ship_mask

        self.max_health = 100

        super().__init__(x, y, self.max_health, self.ship_img)

    def set_player_ship(self):
        if self.game_state.player_current_ship == "common":
            self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_common.png"))
            self.max_health = 100
            self.health = 100
        if self.game_state.player_current_ship == "uncommon":
            self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_uncommon.png"))
            self.max_health = 150
            self.health = 150
        if self.game_state.player_current_ship == "rare":
            self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_rare.png"))
            self.max_health = 250
            self.health = 250
        if self.game_state.player_current_ship == "epic":
            self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_epic.png"))
            self.max_health = 350
            self.health = 350
        if self.game_state.player_current_ship == "legendary":
            self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_legendary.png"))
            self.max_health = 500
            self.health = 500

        ship_mask = pygame.mask.from_surface(self.ship_img)
        self.mask = ship_mask

    def set_player_primary(self):
        if self.game_state.player_current_primary == "common":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_common.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))
            self.primary_damage = 100
        if self.game_state.player_current_primary == "uncommon":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_uncommon.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_uncommon.png"))
            self.primary_damage = 150
        if self.game_state.player_current_primary == "rare":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_rare.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_rare.png"))
            self.primary_damage = 250
        if self.game_state.player_current_primary == "epic":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_epic.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_epic.png"))
            self.primary_damage = 350
        if self.game_state.player_current_primary == "legendary":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_legendary.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_legendary.png"))
            self.primary_damage = 500

    def set_player_secondary(self):
        if self.game_state.player_current_secondary == "common":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_common.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_common.png"))
            self.secondary_damage = 200
        if self.game_state.player_current_secondary == "uncommon":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_uncommon.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_uncommon.png"))
            self.secondary_damage = 300
        if self.game_state.player_current_secondary == "rare":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_rare.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_rare.png"))
            self.secondary_damage = 450
        if self.game_state.player_current_secondary == "epic":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_epic.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_epic.png"))
            self.secondary_damage = 600
        if self.game_state.player_current_secondary == "legendary":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_legendary.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_legendary.png"))
            self.secondary_damage = 900

    def set_player_thruster(self):
        if self.game_state.player_current_thruster == "common":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_common.png"))
        if self.game_state.player_current_thruster == "uncommon":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_uncommon.png"))
        if self.game_state.player_current_thruster == "rare":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_rare.png"))
        if self.game_state.player_current_thruster == "epic":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_epic.png"))
        if self.game_state.player_current_thruster == "legendary":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_legendary.png"))


    def set_game_state(self, game_state):
        self.game_state = game_state

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(750):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= self.primary_damage
                        if obj.health <= 0:
                            objs.remove(obj)

                            self.game_state.total_killing += 1

                            if obj.rarity == "common":
                                self.game_state.score_counter += 1
                            if obj.rarity == "uncommon":
                                self.game_state.score_counter += 2
                            if obj.rarity == "rare":
                                self.game_state.score_counter += 3
                            if obj.rarity == "epic":
                                self.game_state.score_counter += 4
                            if obj.rarity == "legendary":
                                self.game_state.score_counter += 5

                            if laser in self.lasers:
                                self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
