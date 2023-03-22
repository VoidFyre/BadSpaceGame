class Spaceship:
    def __init__(self, x=10, y=10, speed=100, health=100, image=""):
        self.score = None
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.image = image

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def collides_with(self, enemy):
        pass

    def update(self):
        pass
