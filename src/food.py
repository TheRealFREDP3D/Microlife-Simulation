
import random

import pygame

from constants import FOOD_IMAGE_PATH, FOOD_TYPES, SCREEN_HEIGHT, SCREEN_WIDTH

# Load food image once (32x32 sprite)
try:
    ORIGINAL_FOOD_IMAGE = pygame.image.load(FOOD_IMAGE_PATH).convert_alpha()
    print(f"Loaded food sprite: {ORIGINAL_FOOD_IMAGE.get_size()}")
except pygame.error:
    print(f"Warning: Could not load food image at {FOOD_IMAGE_PATH}. Falling back to drawing circles.")
    ORIGINAL_FOOD_IMAGE = None

# Cache for scaled food images by size and color to improve performance
_food_image_cache = {}

def clear_food_image_cache():
    """Clear the food image cache to free memory if needed."""
    global _food_image_cache
    _food_image_cache.clear()

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
            # Create cache key based on size and color
            cache_key = (self.size, self.color)
            
            # Check if we have a cached version of this sprite
            if cache_key not in _food_image_cache:
                # Scale the 32x32 sprite to match food size (multiply by 2 for diameter)
                target_size = max(self.size * 2, 8)  # Minimum 8 pixels
                scaled_image = pygame.transform.smoothscale(ORIGINAL_FOOD_IMAGE, (target_size, target_size))
                
                # Apply color tint to food
                colored_image = scaled_image.copy()
                colored_image.fill(self.color + (0,), None, pygame.BLEND_RGBA_MULT)
                
                # Cache the result
                _food_image_cache[cache_key] = colored_image
            
            # Use cached image
            colored_image = _food_image_cache[cache_key]
            image_rect = colored_image.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(colored_image, image_rect)
        else:
            # Fallback to circles if sprite not loaded
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
