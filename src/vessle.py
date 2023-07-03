from attr import define


@define
class Vessle:
    name: str
    has_sides: bool
    has_roof: bool
    requires_crouch: bool
    has_high_population: bool