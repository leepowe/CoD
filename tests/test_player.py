from engine.entity import Entity
from engine.player import Player
from engine.crystal import Crystal

def test_add_crystal():
    player = Player()
    fire_stone = Crystal("Fire Stone", "Fire", 10, 5)
    player.add_crystal(fire_stone, 5)
    assert player.inventory["crystals"]["Fire Stone"] == 5

def test_crystal_threshold_exceeded():
    player = Player()
    fire_stone = Crystal("Fire Stone", "Fire", 10, 5)
    breached = player.add_crystal(fire_stone, 6)
    assert breached == "The crystals have become unstable and have exploded creating a massive crater!"
    assert fire_stone.name not in player.inventory["crystals"]

def test_trigger_explosion():
    player = Player()
    fire_stone = Crystal("Fire Stone", "Fire", 10, 5)
    player.add_crystal(fire_stone, 50)
    result = player.trigger_explosion(fire_stone)
    assert result == "The crystals have become unstable and have exploded creating a massive crater!"
    assert fire_stone not in player.inventory["crystals"]

def test_player_is_entity():
    player = Player()
    assert isinstance(player, Entity)