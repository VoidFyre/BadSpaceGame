import pygame

class Component(pygame.sprite.Sprite):
    def __init__(self, c_type, rarity, name, image):
        super().__init__()

        #Type of component (Primary Weapon, Secondary Weapon, Hull, Armor, Shield, Thrusters)
        self.c_type = c_type

        #Rarity of component (Common, Uncommon, Rare, Epic, Legendary)
        self.rarity = rarity

        #Name of component
        self.name = name

        #Image of component
        self.image = image

        #Background image of component
        self.base_image = None
        match rarity:
            case 'common':
                self.base_image = pygame.image.load("./assets/interface/background/component_common")
            case 'uncommon':
                self.base_image = pygame.image.load("./assets/interface/background/component_uncommon")
            case 'rare':
                self.base_image = pygame.image.load("./assets/interface/background/component_rare")
            case 'epic':
                self.base_image = pygame.image.load("./assets/interface/background/component_epic")
            case 'legendary':
                self.base_image = pygame.image.load("./assets/interface/background/component_legendary")

            

class Weapon(Component):
    def __init__(self, fire_rate, damage_type, slot, rarity, name, image, projectile):
        super().__init__(slot, rarity, name, image)

        #Projectile shot by this weapon
        self.projectile = projectile

        #Amount of times this weapon fires PER SECOND
        self.fire_rate = fire_rate

        #Type of damage dealt by this weapon (Ballistic or Energy for Primary Weapon, Explosive or EMP for Secondary Weapon)
        self.damage_type = damage_type

class Body(Component):
    def __init__(self, modifier, recharge, multiplier, slot, rarity, name, image):
        #Slot can be Hull, Shield, or Armor
        super().__init__(slot, rarity, name, image)

        self.modifier = modifier
        self.recharge = recharge

        self.multiplier = multiplier

class Thruster(Component):
    def __init__(self, speed_mod, turn_mod, rarity, name, image):
        super().__init__('thruster', rarity, name, image)

        self.speed_mod = speed_mod
        self.turn_mod = turn_mod
