import pygame

import os

from model.Laser import Laser

from model.Spaceship import Spaceship

from model.Explosion import Explosion

from model.Upgrade import Upgrade


class Player(Spaceship):
    def __init__(self, x, y):
        

        # Images

        self.game_state = None
        self.primary_projectiles = []
        self.secondary_projectiles = []
        self.ship_img = pygame.image.load(os.path.join("assets", "component/ship/ship_common.png"))
        self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_common.png"))
        self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_common.png"))
        self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_common.png"))
        self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))
        self.primary_proj_size = (32, 32)
        self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_common.png"))
        self.secondary_proj_size = (32, 32)
        self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_common.png"))
        self.laser_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_common.png"))

        self.primary_damage = 100
        self.secondary_damage = 200

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
            self.primary_proj_size = (32, 32)
            self.primary_damage = 100

        if self.game_state.player_current_primary == "uncommon":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_uncommon.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_uncommon.png"))
            self.primary_proj_size = (32, 32)
            self.primary_damage = 150

        if self.game_state.player_current_primary == "rare":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_rare.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_rare.png"))
            self.primary_proj_size = (32, 32)
            self.primary_damage = 250

        if self.game_state.player_current_primary == "epic":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_epic.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_epic.png"))
            self.primary_proj_size = (32, 128)
            self.primary_damage = 350

        if self.game_state.player_current_primary == "legendary":
            self.primary_img = pygame.image.load(os.path.join("assets", "component/primary/weapon/primary_legendary.png"))
            self.primary_proj_img = pygame.image.load(os.path.join("assets", "component/primary/projectile/projectile_primary_legendary.png"))
            self.primary_proj_size = (32, 128)
            self.primary_damage = 500


    def set_player_secondary(self):
        if self.game_state.player_current_secondary == "common":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_common.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_common.png"))
            self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_common.png"))
            self.secondary_damage = 200

        if self.game_state.player_current_secondary == "uncommon":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_uncommon.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_uncommon.png"))
            self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_uncommon.png"))
            self.secondary_damage = 300

        if self.game_state.player_current_secondary == "rare":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_rare.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_rare.png"))
            self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_rare.png"))
            self.secondary_damage = 450
            
        if self.game_state.player_current_secondary == "epic":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_epic.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_epic.png"))
            self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_epic.png"))
            self.secondary_damage = 600

        if self.game_state.player_current_secondary == "legendary":
            self.secondary_img = pygame.image.load(os.path.join("assets", "component/secondary/weapon/secondary_legendary.png"))
            self.secondary_proj_img = pygame.image.load(os.path.join("assets", "component/secondary/projectile/projectile_secondary_legendary.png"))
            self.secondary_proj_explosion = pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_legendary.png"))
            self.secondary_damage = 900

    def set_player_thruster(self):
        if self.game_state.player_current_thruster == "common":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_common.png"))
            self.game_state.player_vel = 3

        if self.game_state.player_current_thruster == "uncommon":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_uncommon.png"))
            self.game_state.player_vel = 4

        if self.game_state.player_current_thruster == "rare":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_rare.png"))
            self.game_state.player_vel = 5

        if self.game_state.player_current_thruster == "epic":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_epic.png"))
            self.game_state.player_vel = 6

        if self.game_state.player_current_thruster == "legendary":
            self.thruster_img = pygame.image.load(os.path.join("assets", "component/thruster/thruster_legendary.png"))
            self.game_state.player_vel = 8

    def set_game_state(self, game_state):
        self.game_state = game_state

    def move_primary_proj(self, vel, objs):
        self.cooldown()
        for primary_proj in self.primary_projectiles:
            primary_proj.move(vel)
            if primary_proj.off_screen(750):
                self.primary_projectiles.remove(primary_proj)
            else:
                for obj in objs:
                    if primary_proj.collision(obj):
                        self.hit.play()
                        obj.health -= self.primary_damage
                        self.primary_projectiles.remove(primary_proj)

    def move_secondary_proj(self, vel, objs):
        self.cooldown()
        for secondary_proj in self.secondary_projectiles:
            secondary_proj.move(vel)
            if secondary_proj.off_screen(750):
                self.secondary_projectiles.remove(secondary_proj)
            else:
                for obj in objs:
                    if secondary_proj.collision(obj):
                        self.hit.play()
                        explosion = self.create_proj_explosion(obj, self.secondary_proj_explosion)
                        self.secondary_projectiles.remove(secondary_proj)
                        self.explosion_damage(explosion, objs)

                    
                            
    def explosion_damage(self, explosion, objs):
        for obj in objs:
            if explosion.collision(obj) and explosion.collide:
                if explosion.type == "weapon":
                    obj.health -= self.secondary_damage
        explosion.collide = False


    def shoot_primary(self):
        if self.primary_cool_down_counter == 0:
            self.primary_fire_sound.play()
            primary_proj = Laser(self.x, self.y-18, self.primary_proj_img, self.primary_proj_size)
            self.primary_projectiles.append(primary_proj)
            self.primary_cool_down_counter = 30

    def shoot_secondary(self):
        if self.secondary_cool_down_counter == 0:
            self.secondary_fire_sound.play()
            secondary_proj = Laser(self.x+16, self.y-18, self.secondary_proj_img, self.secondary_proj_size)
            self.secondary_projectiles.append(secondary_proj)
            self.secondary_cool_down_counter = 90

    def create_ship_explosion(self, obj):
        explosion = Explosion(obj.get_x() - 20, obj.get_y() - 20, pygame.image.load(os.path.join("assets", "component/secondary/explosion/explosion_secondary_common.png")), (80, 80))
        explosion.type = "ship"
        explosion.collide = False
        self.game_state.explosions.append(explosion)

        explosion.play_sound()

    def create_proj_explosion(self, obj, img):

        explosion = Explosion(obj.get_x() - 300, obj.get_y() - 300, self.secondary_proj_explosion, (600, 600))
        explosion.type = "weapon"
        explosion.collide = True
        self.game_state.explosions.append(explosion)

        explosion.play_sound()
        return explosion

    def track_score_and_kills(self, obj):
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

    def draw(self, window):
        super().draw(window)
        window.blit(self.primary_img, (self.x, self.y))
        window.blit(self.secondary_img, (self.x, self.y))
        window.blit(self.thruster_img, (self.x, self.y))
        for primary_proj in self.primary_projectiles:
            primary_proj.draw(window)
        for secondary_proj in self.secondary_projectiles:
            secondary_proj.draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
