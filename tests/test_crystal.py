from engine.crystal import Crystal

def test_crystal_creation():
    crystal = Crystal("Heartstone", "Fire", 10, 5)
    assert crystal.name == "Heartstone"
    assert crystal.threshold == 5