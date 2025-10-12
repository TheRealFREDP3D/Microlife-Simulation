
import pygame
import random
import os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_TYPES, FOOD_SPAWN_RATE_PER_FRAME, FOOD_MAX_COUNT, FOOD_IMAGE_PATH

# Load food image once
try:
    ORIGINAL_FOOD_IMAGE = pygame.image.load(FOOD_IMAGE_PATH).convert_alpha()
except pygame.error:
    print(f"Warning: Could not load food image at {FOOD_IMAGE_PATH}. Falling back to drawing circles.")
    ORIGINAL_FOOD_IMAGE = None

class Food:
    def __init__(self, x, y, food_type_data):
        self.x = x
        self.y = y
        self.color = food_type_data["color"]
        self.size = food_type_data["size"]
        self.energy_value = food_type_data["energy_value"]
        self.lifespan = food_type_data["lifespan"]
        self.age = 0

    def draw(self, screen):
        if ORIGINAL_FOOD_IMAGE:
            scaled_image = pygame.transform.scale(ORIGINAL_FOOD_IMAGE, (self.size * 2, self.size * 2))
            image_rect = scaled_image.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(scaled_image, image_rect)
        else:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def update(self):
        self.age += 1
        if self.age > self.lifespan:
            return False # Indicate decay
        return True # Indicate alive

def spawn_food_item(x=None, y=None):
    food_type_data = random.choice(FOOD_TYPES)
    if x is None:
        x = random.randint(0, SCREEN_WIDTH - food_type_data["size"])
    if y is None:
        y = random.randint(0, SCREEN_HEIGHT - food_type_data["size"])
    return Food(x, y, food_type_data)


