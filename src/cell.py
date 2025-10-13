
import math
import os
import random

import pygame

from clan import Clan  # Import the Clan class
from constants import (
    CELL_ENERGY_CONSUMPTION_PER_MOVE_BASE,
    CELL_ENERGY_MAX,
    CELL_IDLE_ENERGY_DRAIN,
    CELL_MIN_AGE_TO_REPRODUCE,
    CELL_MUTATION_AMOUNT,
    CELL_MUTATION_RATE,
    CELL_REPRODUCTION_THRESHOLD,
    CELL_SIZE_MIN,
    INITIAL_REPRODUCTION_TIME,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from utils import clamp, get_distance

# Load cell image once (32x32 sprite)
CELL_IMAGE_PATH = os.path.join("assets", "cell_basic.png")
try:
    ORIGINAL_CELL_IMAGE = pygame.image.load(CELL_IMAGE_PATH).convert_alpha()
    print(f"Loaded cell sprite: {ORIGINAL_CELL_IMAGE.get_size()}")
except pygame.error:
    print(f"Warning: Could not load cell image at {CELL_IMAGE_PATH}. Falling back to drawing circles.")
    ORIGINAL_CELL_IMAGE = None

# Cache for scaled cell images by size to improve performance
_cell_image_cache = {}

def clear_cell_image_cache():
    """Clear the cell image cache to free memory if needed."""
    global _cell_image_cache
    _cell_image_cache.clear()

class Cell:
    def __init__(self, x, y, clan: Clan, energy=CELL_ENERGY_MAX):
        self.x = x
        self.y = y
        self.clan = clan # Assign the cell to a clan
        self.energy = energy
        self.age = 0
        self.reproduction_timer = 0 # Timer for initial reproduction

        # Traits are now referenced from the clan
        self.speed = self.clan.speed
        self.sense_radius = self.clan.sense_radius
        self.energy_efficiency = self.clan.energy_efficiency
        self.size = self.clan.size
        self.lifespan = self.clan.lifespan

        self.target_food = None

    def move(self):
        movement_cost = 0
        if self.target_food:
            # Move towards target food
            dx = self.target_food.x - self.x
            dy = self.target_food.y - self.y
            dist = get_distance((self.x, self.y), (self.target_food.x, self.target_food.y))

            if dist > 0:
                # Normalize direction vector and scale by speed
                direction_x = dx / dist
                direction_y = dy / dist

                move_amount = min(self.speed, dist) # Don't overshoot
                self.x += direction_x * move_amount
                self.y += direction_y * move_amount

                # Consume energy for movement, adjusted by efficiency and size
                movement_cost = CELL_ENERGY_CONSUMPTION_PER_MOVE_BASE * move_amount * self.energy_efficiency * (self.size / CELL_SIZE_MIN)
        else:
            # Random movement if no target
            angle = random.uniform(0, 2 * math.pi)
            move_amount = self.speed / 2 # Slower random movement
            self.x += math.cos(angle) * move_amount
            self.y += math.sin(angle) * move_amount
            movement_cost = CELL_ENERGY_CONSUMPTION_PER_MOVE_BASE * move_amount * self.energy_efficiency * (self.size / CELL_SIZE_MIN)

        self.energy -= movement_cost
        self.energy -= CELL_IDLE_ENERGY_DRAIN * (self.size / CELL_SIZE_MIN) # Idle energy drain adjusted by size

        # Keep cell within screen bounds
        self.x = clamp(self.x, 0, SCREEN_WIDTH - self.size)
        self.y = clamp(self.y, 0, SCREEN_HEIGHT - self.size)

        self.energy = clamp(self.energy, 0, CELL_ENERGY_MAX)

    def find_food(self, food_items):
        closest_food = None
        min_dist = float('inf')  # Initialize with a very large distance

        for food in food_items:
            dist = get_distance((self.x, self.y), (food.x, food.y))
            if dist < self.sense_radius and dist < min_dist:
                min_dist = dist
                closest_food = food
        self.target_food = closest_food

    def eat(self, food_items):
        if self.target_food and get_distance((self.x, self.y), (self.target_food.x, self.target_food.y)) < self.size:
            self.energy += self.target_food.energy_value
            self.energy = clamp(self.energy, 0, CELL_ENERGY_MAX)
            food_items.remove(self.target_food)
            self.target_food = None
            return True
        return False

    def reproduce(self):
        """
        Asexual reproduction: cell splits into two when conditions are met.
        Offspring inherits parent's clan with potential mutations applied at the clan level.
        """
        # Check for initial reproduction timer
        if self.reproduction_timer < INITIAL_REPRODUCTION_TIME:
            self.reproduction_timer += 1
            return None

        # Check if cell has enough energy and age to reproduce
        if self.energy >= CELL_REPRODUCTION_THRESHOLD and self.age >= CELL_MIN_AGE_TO_REPRODUCE:
            self.energy /= 2 # Split energy with offspring
            
            # Create offspring near parent
            offspring_x = clamp(self.x + random.uniform(-self.size, self.size), 0, SCREEN_WIDTH - self.size)
            offspring_y = clamp(self.y + random.uniform(-self.size, self.size), 0, SCREEN_HEIGHT - self.size)

            # Apply mutations to clan traits
            if random.random() < CELL_MUTATION_RATE:
                self.clan.apply_mutation("speed", random.uniform(-CELL_MUTATION_AMOUNT, CELL_MUTATION_AMOUNT))
            if random.random() < CELL_MUTATION_RATE:
                self.clan.apply_mutation("sense_radius", random.uniform(-CELL_MUTATION_AMOUNT, CELL_MUTATION_AMOUNT))
            if random.random() < CELL_MUTATION_RATE:
                self.clan.apply_mutation("energy_efficiency", random.uniform(-CELL_MUTATION_AMOUNT, CELL_MUTATION_AMOUNT))
            if random.random() < CELL_MUTATION_RATE:
                self.clan.apply_mutation("size", random.uniform(-CELL_MUTATION_AMOUNT * 5, CELL_MUTATION_AMOUNT * 5))
            if random.random() < CELL_MUTATION_RATE:
                self.clan.apply_mutation("lifespan", random.uniform(-CELL_MUTATION_AMOUNT * 100, CELL_MUTATION_AMOUNT * 100))

            # Offspring belongs to the same clan
            return Cell(offspring_x, offspring_y, self.clan, self.energy)
        return None

    def draw(self, screen):
        if ORIGINAL_CELL_IMAGE:
            # Create cache key based on size and clan color
            cache_key = (int(self.size), self.clan.id)
            
            # Check if we have a cached version of this sprite
            if cache_key not in _cell_image_cache:
                # Scale the 32x32 sprite to match cell size (multiply by 2 for diameter)
                target_size = max(int(self.size * 2), 8)  # Minimum 8 pixels
                scaled_image = pygame.transform.smoothscale(ORIGINAL_CELL_IMAGE, (target_size, target_size))
                
                # Apply clan color tint
                colored_image = scaled_image.copy()
                colored_image.fill(self.clan.color + (0,), None, pygame.BLEND_RGBA_MULT)
                
                # Cache the result
                _cell_image_cache[cache_key] = colored_image
            
            # Use cached image
            colored_image = _cell_image_cache[cache_key]
            image_rect = colored_image.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(colored_image, image_rect)
        else:
            # Fallback to circles if sprite not loaded
            pygame.draw.circle(screen, self.clan.color, (int(self.x), int(self.y)), int(self.size))
        # Optionally draw sense radius for debugging
        # pygame.draw.circle(screen, (50, 50, 50), (int(self.x), int(self.y)), int(self.sense_radius), 1)

    def update(self, food_items):
        self.age += 1
        # Update traits from clan (in case clan traits mutated)
        self.speed = self.clan.speed
        self.sense_radius = self.clan.sense_radius
        self.energy_efficiency = self.clan.energy_efficiency
        self.size = self.clan.size
        self.lifespan = self.clan.lifespan

        self.find_food(food_items)
        self.move()
        self.eat(food_items)

        # Die if out of energy or too old
        if self.energy <= 0 or self.age >= self.lifespan:
            return False # Indicate death
        return True # Indicate alive
