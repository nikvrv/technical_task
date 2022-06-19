from pydantic import BaseModel


class PeopleModel(BaseModel):
    """
    Response model for get people
    """
    id: int
    name: str
    lastname: str


class PlanetModal(BaseModel):
    """
    Response model for get planet
    """
    name: str
    rotation_period: int
    orbital_period: float
    diameter: int
    climate: str
    gravity: str
    terrain: str
    surface_water: int
    population: int


class StarshipModel(BaseModel):
    """
    Response model for get starship
    """
    name: str
    model: str
    manufacturer: str
    cost_in_credits: int
    length: float
    max_atmosphering_speed: int
    crew: int
    passengers: int
    cargo_capacity: int
    consumables: str
    hyperdrive_rating: float
    MGLT: int
    starship_class: str
