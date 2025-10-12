
import random
from constants import (
    CELL_SPEED_MIN, CELL_SPEED_MAX, CELL_SENSE_RADIUS_MIN, CELL_SENSE_RADIUS_MAX,
    CELL_ENERGY_EFFICIENCY_MIN, CELL_ENERGY_EFFICIENCY_MAX, CELL_SIZE_MIN, CELL_SIZE_MAX,
    CELL_MAX_LIFESPAN, CLAN_COLORS
)
from utils import clamp

class Clan:
    next_id = 0

    def __init__(self, color=None):
        self.id = Clan.next_id
        Clan.next_id += 1
        self.color = color if color is not None else random.choice(CLAN_COLORS)

        # Shared traits for the clan
        self.speed = random.uniform(CELL_SPEED_MIN, CELL_SPEED_MAX)
        self.sense_radius = random.uniform(CELL_SENSE_RADIUS_MIN, CELL_SENSE_RADIUS_MAX)
        self.energy_efficiency = random.uniform(CELL_ENERGY_EFFICIENCY_MIN, CELL_ENERGY_EFFICIENCY_MAX)
        self.size = random.uniform(CELL_SIZE_MIN, CELL_SIZE_MAX)
        self.lifespan = random.randint(CELL_MAX_LIFESPAN // 2, CELL_MAX_LIFESPAN)

        # Ensure initial traits are within bounds
        self.speed = clamp(self.speed, CELL_SPEED_MIN, CELL_SPEED_MAX)
        self.sense_radius = clamp(self.sense_radius, CELL_SENSE_RADIUS_MIN, CELL_SENSE_RADIUS_MAX)
        self.energy_efficiency = clamp(self.energy_efficiency, CELL_ENERGY_EFFICIENCY_MIN, CELL_ENERGY_EFFICIENCY_MAX)
        self.size = clamp(self.size, CELL_SIZE_MIN, CELL_SIZE_MAX)
        self.lifespan = clamp(self.lifespan, CELL_MAX_LIFESPAN // 2, CELL_MAX_LIFESPAN)

    def get_traits(self):
        return {
            "speed": self.speed,
            "sense_radius": self.sense_radius,
            "energy_efficiency": self.energy_efficiency,
            "size": self.size,
            "lifespan": self.lifespan
        }

    def apply_mutation(self, trait_name, mutation_amount):
        if trait_name == "speed":
            self.speed = clamp(self.speed + mutation_amount, CELL_SPEED_MIN, CELL_SPEED_MAX)
        elif trait_name == "sense_radius":
            self.sense_radius = clamp(self.sense_radius + mutation_amount, CELL_SENSE_RADIUS_MIN, CELL_SENSE_RADIUS_MAX)
        elif trait_name == "energy_efficiency":
            self.energy_efficiency = clamp(self.energy_efficiency + mutation_amount, CELL_ENERGY_EFFICIENCY_MIN, CELL_ENERGY_EFFICIENCY_MAX)
        elif trait_name == "size":
            self.size = clamp(self.size + mutation_amount, CELL_SIZE_MIN, CELL_SIZE_MAX)
        elif trait_name == "lifespan":
            self.lifespan = clamp(self.lifespan + mutation_amount, CELL_MAX_LIFESPAN // 2, CELL_MAX_LIFESPAN)




