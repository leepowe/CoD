import pytest
from engine.crystal import Crystal

def test_crystal_creation():
    crystal = Crystal("Heartstone", "Fire", 10, 5)
    assert crystal.name == "Heartstone"
    assert crystal.threshold == 5

def test_crystal_purity_cannot_be_negative():
    crystal = Crystal("Void Shard", "Dark", 10, 5)
    with   pytest.raises(ValueError):
        crystal.purity = -15