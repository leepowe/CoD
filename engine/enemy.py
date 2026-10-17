from engine.entity import Entity

class Enemy(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)