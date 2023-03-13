import pygame

class Component(pygame.sprite.Sprite):
    def __init__(self, c_type, rarity, name):
        super().__init__()

        #Type of component (Primary Weapon, Secondary Weapon, Hull, Armor, Shield, Thrusters)
        self.c_type = c_type

        #Rarity of component (Common, Uncommon, Rare, Epic, Legendary)
        self.rarity = rarity

        #Name of component
        self.name = name

class Weapon(Component):
    def __init__(self, damage, fire_rate, damage_type, slot):
        super().__init__()

        #Amount of damage a weapon deals PER SHOT
        self.damage = damage

        #Amount of times this weapon fires PER SECOND
        self.fire_rate = fire_rate

        #Type of damage dealt by this weapon (Ballistic or Energy for Primary Weapon, Explosive or EMP for Secondary Weapon)
        self.damage_type = damage_type