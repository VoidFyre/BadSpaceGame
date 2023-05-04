import pygame
import os
import random

class Upgrade:
    def __init__(self):

        self.uncommon_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/uncommon_orb.png"))
        self.rare_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/rare_orb.png"))
        self.epic_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/epic_orb.png"))
        self.legendary_orb = pygame.transform.scale(pygame.image.load(os.path.join("assets", "upgrade-orb/epic_orb.png")).convert_alpha(),(60, 60))

        self.mask = pygame.mask.from_surface(self.uncommon_orb)

        self.sound = pygame.mixer.Sound(os.path.join("assets", "sounds/upgrade.ogg"))


        self.width = 30
        self.height = 30

        self.orb_type = None
        self.x = None
        self.y = None

    def play_sound(self):
        # Play the sound
        self.sound.play()

    def draw(self, window):
        if self.orb_type == 'common':
            return
        elif self.orb_type == 'uncommon':
            window.blit(self.uncommon_orb, (self.x, self.y))
        elif self.orb_type == 'rare':
            window.blit(self.rare_orb, (self.x, self.y))
        elif self.orb_type == 'epic':
            window.blit(self.epic_orb, (self.x, self.y))
        elif self.orb_type == 'legendary':
            window.blit(self.legendary_orb, (self.x, self.y))
    def move(self, vel):
        self.y += vel

    # Function to summon an orb on a ship that has been destroyed
    # Every ship has a 20% chance to drop an upgrade of its own rarity
    def summon_random_orb(self, rarity):
        rand_orb = random.randint(1, 100)
        reward_type = 'common' #Set reward type to the basic common

        #Default
        if rarity == "common":
            return reward_type

        #Uncommon Orb
        elif rand_orb <= 20 and rarity == "uncommon":
            reward_type = 'uncommon'
            return reward_type
        
        #Rare orb
        elif rand_orb <= 20 and rarity == "rare":
            reward_type = 'rare'
            return reward_type

        #Epic orb
        elif rand_orb <= 20 and rarity == "epic":
            reward_type = 'epic'
            return reward_type

        #Legendary orb
        elif rand_orb <= 20 and rarity == "legendary":
            reward_type = 'legendary'
            return reward_type
    
    # This function rewards the player with a random item
    # The player has an equal chance of getting a ship, thruster, primary weapon, or secondary weapon
    # based off of the orb that they collide with
    def reward_player(self, type, game_state, player):
        rand_upgrade = random.randint(1,100)
        if type == 'uncommon':
            print(type)
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to uncommon
                if game_state.player_current_ship == "common":
                    game_state.player_current_ship = "uncommon"
                    player.set_player_ship()
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to uncommon
                if game_state.player_current_thruster == "common":
                    game_state.player_current_thruster = "uncommon"
                    player.set_player_thruster()
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to uncommon
                if game_state.player_current_primary == "common":
                    game_state.player_current_primary = "uncommon"
                    player.set_player_primary()
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to uncommon
                if game_state.player_current_secondary == "common":
                    game_state.player_current_secondary = "uncommon"
                    player.set_player_secondary()

        if type == 'rare':
            print(type)
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to rare
                if game_state.player_current_ship == "common" or game_state.player_current_ship == "uncommon":
                    game_state.player_current_ship = "rare"
                    player.set_player_ship()
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to rare
                if game_state.player_current_thruster == "common" or game_state.player_current_thruster == "uncommon":
                    game_state.player_current_thruster = "rare"
                    player.set_player_thruster()
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to rare
                if game_state.player_current_primary == "common" or game_state.player_current_primary == "uncommon":
                    game_state.player_current_primary = "rare"
                    player.set_player_primary()
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to rare
                if game_state.player_current_secondary == "common" or game_state.player_current_secondary == "uncommon":
                    game_state.player_current_secondary = "rare"
                    player.set_player_secondary()

        if type == 'epic':
            print(type)
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to epic
                if game_state.player_current_ship != "legendary":
                    game_state.player_current_ship = "epic"
                    player.set_player_ship()
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to epic
                if game_state.player_current_thruster != "legendary":
                    game_state.player_current_thruster = "epic"
                    player.set_player_thruster()
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to epic
                if game_state.player_current_primary != "legendary":
                    game_state.player_current_primary = "epic"
                    player.set_player_primary()
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to epic
                if game_state.player_current_secondary != "legendary":
                    game_state.player_current_secondary = "epic"
                    player.set_player_secondary()

        if type == 'legendary':
            print(type)
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to legendary
                game_state.player_current_ship = "legendary"
                player.set_player_ship()
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to legendary
                game_state.player_current_thruster = "legendary"
                player.set_player_thruster()
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to legendary
                game_state.player_current_primary = "legendary"
                player.set_player_primary()
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to legendary
                game_state.player_current_secondary = "legendary"
                player.set_player_secondary()
