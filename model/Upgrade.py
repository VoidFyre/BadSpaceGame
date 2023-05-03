import pygame
import os
import random

class Upgrade:
    def __init__(self):

        self.uncommon_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/uncommon_orb.png"))
        self.rare_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/rare_orb.png"))
        self.epic_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/epic_orb.png"))
        self.legendary_orb = pygame.image.load(os.path.join("assets", "upgrade-orb/legendary_orb.png"))


        self.width = 30
        self.height = 30

        self.orb_type = None
        self.x = None
        self.y = None

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
    # The player has a 40% chance of getting nothing, a 30% chance of getting uncommon, a 15% chance of getting rare,
    # a 10% chance of getting epic, and a 5% chance of getting a legendary item.
    def summon_random_orb(self):
        rand_orb = random.randint(1, 100)
        reward_type = 'common' #Set reward type to the basic common

        #Uncommon Orb
        if rand_orb >0 and rand_orb <= 40:
            return reward_type
        elif rand_orb > 40 and rand_orb <= 70 :
            reward_type = 'uncommon'
            print(reward_type + " ")
            print(rand_orb)
            return reward_type
        
        #Rare orb
        elif rand_orb > 70 and rand_orb <= 85:
            reward_type = 'rare'
            print(reward_type + " ")
            print(rand_orb)
            return reward_type

        #Epic orb
        elif rand_orb > 85 and rand_orb <= 95 :
            reward_type = 'epic'
            print(reward_type + " ")
            print(rand_orb)
            return reward_type

        #Legendary orb
        elif rand_orb > 95 and rand_orb <= 100:
            reward_type = 'legendary'
            print(reward_type + " ")
            print(rand_orb)
            return reward_type
    
    # This function rewards the player with a random item
    # The player has an equal chance of getting a ship, thruster, primary weapon, or secondary weapon
    # based off of the orb that they collide with
    def reward_player(self, type):
        rand_upgrade = random.randint(1,100)
        if type == 'uncommon':
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to uncommon
                pass
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to uncommon
                pass
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to uncommon
                pass
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to uncommon
                pass

        if type == 'rare':
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to rare
                pass
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to rare
                pass
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to rare
                pass
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to rare
                pass

        if type == 'epic':
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to epic
                pass
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to epic
                pass
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to epic
                pass
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to epic
                pass

        if type == 'legendary':
            if rand_upgrade > 0 and rand_upgrade <= 25:
                #Set ship to legendary
                pass
            if rand_upgrade > 25 and rand_upgrade <= 50:
                #Set thruster to legendary
                pass
            if rand_upgrade > 50 and rand_upgrade <= 75:
                #Set primary to legendary
                pass
            if rand_upgrade > 75 and rand_upgrade <= 100:
                #Set secondary to legendary
                pass
