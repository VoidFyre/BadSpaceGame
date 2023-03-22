class Projectile:
    def __init__(self, x, y, speed, damage, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.damage = damage
        self.image = image

    def move(self):
        self.y -= self.speed
