import pytest
from src.preposition import Preposition

from src.main import generate_prep
from src.vessle import Vessle


@pytest.mark.parametrize('vessle,expected_prep',[
    (Vessle('Bus', True, True, False, True), Preposition.ON),
    (Vessle('Train', True, True, False, True), Preposition.ON),
    (Vessle('Raft', False, False, False, True), Preposition.ON),
    (Vessle('Boat', True, False, False, True), Preposition.ON),
    (Vessle('Bike', False, False, False, False), Preposition.ON),
    (Vessle('Horse', False, False, False, False), Preposition.ON),
    (Vessle('Scooter', False, False, False, False), Preposition.ON),
    (Vessle('Motorbike', False, False, False, False), Preposition.ON),
    (Vessle('Plane', True, True, False, True), Preposition.ON),
    (Vessle('Canoe', True, False, False, False), Preposition.IN),
    (Vessle('Zorb', True, True, False, False), Preposition.IN),
    (Vessle('Car', True, True, True, False), Preposition.IN),
    (Vessle('Truck', True, True, True, False), Preposition.IN),
    (Vessle('Forklift Truck', False, True, True, False), Preposition.IN),
    (Vessle('Hot Air Balloon', True, False, False, False), Preposition.IN),
])
def test_adjectives(vessle: Vessle, expected_prep: Preposition):
    assert generate_prep(vessle) == expected_prep

