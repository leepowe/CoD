import pytest

from engine.entity import Entity

def test_entity_initialization():
    target = Entity("Cultist", 100)
    assert target.name == "Cultist"
    assert target.health == 100

def test_entity_health_cannot_be_negative():
    target = Entity("Cultist of the Shattered Veil", 100)
    with pytest.raises(ValueError):
        target.health = -10
