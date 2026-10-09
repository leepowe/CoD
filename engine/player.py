from engine.entity import Entity

class Player(Entity):
    def __init__(self):
        super().__init__("Hero", 100)
        self.inventory = {
            "crystals": {},
            "gadgets": {},
            "texts": {}
        }

    def add_crystal(self, crystal, amount):
        self.inventory["crystals"][crystal.name] = self.inventory["crystals"].get(crystal.name, 0) + amount
        if self.inventory["crystals"][crystal.name] > crystal.threshold:
            return self.trigger_explosion(crystal)
        return False
    
    def trigger_explosion(self, crystal):
        self.inventory["crystals"].pop(crystal.name, None)
        if crystal.purity > 5:
            crater_size = "massive"
        else:
            crater_size = "small"
        return f"The crystals have become unstable and have exploded creating a {crater_size} crater!"
        