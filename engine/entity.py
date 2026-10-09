class Entity:
    def __init__(self, name, health):
        self.name = name
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value):
        if new_value < 0:
            raise ValueError("Health cannot be negative.")
        self.health = new_value
