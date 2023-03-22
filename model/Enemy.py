class Enemy:
    def __init__(self, x, y, speed, health, damage, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.damage = damage
        self.image = image

    def move(self):
        self.y += self.speed
