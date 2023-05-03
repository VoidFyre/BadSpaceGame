import pygame
import os
import random

class Upgrade:
    def __init__(self):
        self.images = {
            'uncommon_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/uncommon_orb.png")),
            'rare_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/rare_orb.png")),
            'epic_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/epic_orb.png")),
            'legendary_orb': pygame.image.load(os.path.join("assets", "upgrade-orb/legendary_orb.png"))
        }
        self.width = 30
        self.height = 30

    def draw(self, window, orb, x, y):
        window.blit(self.images[orb], (x, y))

    # Function to summon an orb on a ship that has been destroyed
    # The player has a 40% chance of getting nothing, a 30% chance of getting uncommon, a 15% chance of getting rare,
    # a 10% chance of getting epic, and a 5% chance of getting a legendary item.
    def summon_random_orb(self, window, x, y):
        rand_orb = random.randint(1, 100)
        reward_type = 'common' #Set reward type to the basic common

        #Uncommon Orb
        if rand_orb > 40 & rand_orb <= 70 :
            self.draw(window, self.images['uncommon_orb'], x, y)
            reward_type = 'uncommon'
            self.reward_player(reward_type)
        
        #Rare orb
        if rand_orb > 70 and rand_orb <= 85:
            self.draw(window, self.images['rare_orb'], x, y)
            reward_type = 'rare'
            self.reward_player(reward_type)

        #Epic orb
        if rand_orb > 85 and rand_orb <= 95 :
            self.draw(window, self.images['epic_orb'], x, y)
            reward_type = 'epic'
            self.reward_player(reward_type)

        #Legendary orb
        if rand_orb > 95 and rand_orb <= 100:
            self.draw(window, self.images['legendary_orb'], x, y)
            reward_type = 'legendary'
            self.reward_player(reward_type)
    
    # This function rewards the player with a random item
    # The player has an equal chance of getting a ship, thruster, primary weapon, or secondary weapon
    # based off of the orb that they collide with
    def reward_player(self, type):
        rand_upgrade = random.randint(1-100)
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
