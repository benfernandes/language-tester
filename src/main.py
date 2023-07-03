from src.preposition import Preposition
from src.vessle import Vessle


def generate_prep(vessle: Vessle) -> Preposition:
    if (vessle.has_sides or vessle.requires_crouch) and not vessle.has_high_population:
        return Preposition.IN
    else:
        return Preposition.ON