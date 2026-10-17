import pytest

from engine.enemy import Enemy

def test_enemy_exists():
    cultist = Enemy("Cultist of Decay", 100)

def test_enemy_inherits_health_protection():
    cultist = Enemy("Cultist of Decay", 100)

    with pytest.raises(ValueError):
        cultist.health = -10

def test_enemy_initialization():
    cultist = Enemy("Cultist of Decay", 50)
    assert cultist.name == "Cultist of Decay"
    assert cultist.health == 50