
import pygame
import random
import os
from cell import Cell
from food import Food, spawn_food_item
from clan import Clan # Import the Clan class
from constants import (
    INITIAL_CELL_COUNT, INITIAL_FOOD_COUNT, FOOD_SPAWN_RATE_PER_FRAME, FOOD_MAX_COUNT,
    SCREEN_WIDTH, SCREEN_HEIGHT, TOXIC_ZONE_COUNT, TOXIC_ZONE_SIZE_MIN, TOXIC_ZONE_SIZE_MAX,
    TOXIC_ZONE_DAMAGE_PER_FRAME, RESOURCE_ZONE_COUNT, RESOURCE_ZONE_SIZE_MIN, RESOURCE_ZONE_SIZE_MAX,
    RESOURCE_ZONE_FOOD_BOOST, ENVIRONMENT_CHANGE_INTERVAL, PURPLE, LIGHT_BLUE, BACKGROUND_IMAGE_PATH,
    INITIAL_CLAN_COUNT, CELLS_PER_CLAN, CLAN_COLORS
)
from utils import get_distance

# Load background image once
try:
    ORIGINAL_BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
except pygame.error:
    print(f"Warning: Could not load background image at {BACKGROUND_IMAGE_PATH}. Background will be black.")
    ORIGINAL_BACKGROUND_IMAGE = None

class Zone:
    def __init__(self, x, y, radius, color, type):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.type = type

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius), 2) # Draw outline

class Environment:
    def __init__(self):
        self.cells = []
        self.food = []
        self.clans = [] # List to hold Clan objects
        self.toxic_zones = []
        self.resource_zones = []
        self.environment_timer = 0
        self.initialize_clans()
        self.initialize_population()
        self.initialize_zones()

    def initialize_clans(self):
        for i in range(INITIAL_CLAN_COUNT):
            self.clans.append(Clan(color=CLAN_COLORS[i % len(CLAN_COLORS)])) # Assign distinct colors

    def initialize_population(self):
        # Spawn cells based on clans
        for clan in self.clans:
            # Determine a central spawning point for the clan
            center_x = random.randint(0, SCREEN_WIDTH - 1)
            center_y = random.randint(0, SCREEN_HEIGHT - 1)
            for _ in range(CELLS_PER_CLAN):
                # Spawn cells clustered around the center point
                x = center_x + random.uniform(-20, 20)
                y = center_y + random.uniform(-20, 20)
                x = max(0, min(x, SCREEN_WIDTH - 1))
                y = max(0, min(y, SCREEN_HEIGHT - 1))
                self.cells.append(Cell(x, y, clan))

        # Spawn initial food
        for _ in range(INITIAL_FOOD_COUNT):
            self.food.append(spawn_food_item())

    def initialize_zones(self):
        self.toxic_zones = []
        self.resource_zones = []
        for _ in range(TOXIC_ZONE_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            radius = random.randint(TOXIC_ZONE_SIZE_MIN, TOXIC_ZONE_SIZE_MAX)
            self.toxic_zones.append(Zone(x, y, radius, PURPLE, "toxic"))
        for _ in range(RESOURCE_ZONE_COUNT):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            radius = random.randint(RESOURCE_ZONE_SIZE_MIN, RESOURCE_ZONE_SIZE_MAX)
            self.resource_zones.append(Zone(x, y, radius, LIGHT_BLUE, "resource"))

    def update(self):
        self.environment_timer += 1
        if self.environment_timer >= ENVIRONMENT_CHANGE_INTERVAL:
            self.initialize_zones() # Re-initialize zones to simulate dynamic changes
            self.environment_timer = 0

        # Update cells
        new_cells = []
        for cell in self.cells:
            # Apply environmental effects to cells
            for zone in self.toxic_zones:
                if get_distance((cell.x, cell.y), (zone.x, zone.y)) < zone.radius:
                    cell.energy -= TOXIC_ZONE_DAMAGE_PER_FRAME

            if cell.update(self.food):
                new_cells.append(cell)
                # Check for reproduction
                offspring = cell.reproduce()
                if offspring:
                    new_cells.append(offspring)
        self.cells = new_cells

        # Update food and handle decay
        new_food = []
        for food_item in self.food:
            if food_item.update(): # Check if food has decayed
                new_food.append(food_item)
        self.food = new_food

        # Dynamic food spawning, adjusted by resource zones
        food_spawn_multiplier = 1
        for zone in self.resource_zones:
            # If a cell is in a resource zone, food spawns faster around it
            # For simplicity, we\"ll just boost overall spawn rate if any cell is in a resource zone
            # A more complex approach would be to spawn food *within* the zone
            if any(get_distance((cell.x, cell.y), (zone.x, zone.y)) < zone.radius for cell in self.cells):
                food_spawn_multiplier = RESOURCE_ZONE_FOOD_BOOST
                break

        if len(self.food) < FOOD_MAX_COUNT and random.random() < FOOD_SPAWN_RATE_PER_FRAME * food_spawn_multiplier:
            self.food.append(spawn_food_item())

    def draw(self, screen):
        if ORIGINAL_BACKGROUND_IMAGE:
            # Tile the background image across the screen
            bg_width, bg_height = ORIGINAL_BACKGROUND_IMAGE.get_size()
            for x in range(0, SCREEN_WIDTH, bg_width):
                for y in range(0, SCREEN_HEIGHT, bg_height):
                    screen.blit(ORIGINAL_BACKGROUND_IMAGE, (x, y))
        else:
            screen.fill((0, 0, 0)) # Fallback to black background

        for zone in self.toxic_zones:
            zone.draw(screen)
        for zone in self.resource_zones:
            zone.draw(screen)
        for food_item in self.food:
            food_item.draw(screen)
        for cell in self.cells:
            cell.draw(screen)


