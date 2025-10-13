
import os

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GREY = (100, 100, 100)
PURPLE = (180, 50, 180) # For toxic zones - brighter, more visible
LIGHT_BLUE = (100, 200, 255) # For resource zones - more vibrant blue

# Clan properties
INITIAL_CLAN_COUNT = 3
CELLS_PER_CLAN = 2
CLAN_COLORS = [
    (255, 80, 80),    # Coral Red - softer, more visible
    (80, 150, 255),   # Sky Blue - brighter, easier to see
    (100, 255, 100),  # Lime Green - more vibrant
    (255, 200, 50),   # Golden Yellow - warmer tone
    (255, 100, 200),  # Hot Pink - more distinct than magenta
    (100, 255, 255)   # Bright Cyan - more luminous
] # A list of distinct, vibrant colors for clans

# Cell properties
INITIAL_CELL_COUNT = 10 # This will be overridden by clan spawning
CELL_SIZE_MIN = 5
CELL_SIZE_MAX = 15
CELL_COLOR = GREEN # Default color, will be overridden by clan color
CELL_ENERGY_MAX = 150 # Increased from 100 to improve survival
CELL_ENERGY_CONSUMPTION_PER_MOVE_BASE = 0.03 # Reduced from 0.05 - cells use less energy moving
CELL_IDLE_ENERGY_DRAIN = 0.001 # Reduced from 0.002 - slower idle drain
CELL_REPRODUCTION_THRESHOLD = 80 # Increased from 60 to prevent overpopulation
CELL_MIN_AGE_TO_REPRODUCE = 50 # Increased from 30 to allow cells to mature
CELL_MAX_LIFESPAN = 1000 # Maximum age in frames before a cell dies naturally
CELL_MUTATION_RATE = 0.1 # Probability of a trait mutating
CELL_MUTATION_AMOUNT = 0.1 # Max change in trait value
CELL_SPEED_MIN = 1
CELL_SPEED_MAX = 5
CELL_SENSE_RADIUS_MIN = 50
CELL_SENSE_RADIUS_MAX = 150
CELL_ENERGY_EFFICIENCY_MIN = 0.5 # Multiplier for energy consumption (lower is better)
CELL_ENERGY_EFFICIENCY_MAX = 1.5 # Multiplier for energy consumption (higher is worse)
INITIAL_REPRODUCTION_TIME = 200 # 200 frames = ~3.3 seconds at 60 FPS (reduced from 1200 frames = 20 seconds)

# Food properties
INITIAL_FOOD_COUNT = 80 # Increased from 50 to provide more initial food
FOOD_TYPES = [
    {"size": 6, "energy_value": 30, "color": (150, 200, 255), "lifespan": 400}, # Small, better energy, light blue
    {"size": 9, "energy_value": 50, "color": (255, 180, 100), "lifespan": 700}, # Medium, good energy, orange
    {"size": 13, "energy_value": 80, "color": (200, 100, 255), "lifespan": 1000}  # Large, high energy, purple
]
FOOD_SPAWN_RATE_PER_FRAME = 0.10 # Doubled from 0.05 - food spawns twice as fast
FOOD_MAX_COUNT = 150 # Increased from 100 to support larger populations

# Environmental factors
TOXIC_ZONE_COUNT = 1 # Reduced from 2 to make environment less hostile
TOXIC_ZONE_SIZE_MIN = 40
TOXIC_ZONE_SIZE_MAX = 100 # Reduced maximum size
TOXIC_ZONE_DAMAGE_PER_FRAME = 0.3 # Reduced from 0.5 - less deadly
RESOURCE_ZONE_COUNT = 3 # Increased from 2 to provide more resource-rich areas
RESOURCE_ZONE_SIZE_MIN = 60
RESOURCE_ZONE_SIZE_MAX = 180 # Increased maximum size
RESOURCE_ZONE_FOOD_BOOST = 3 # Increased from 2 - more food in resource zones
ENVIRONMENT_CHANGE_INTERVAL = 900 # Increased from 600 - zones change less frequently

# Simulation parameters
FPS = 60

# UI parameters
FONT_SIZE = 20
TEXT_COLOR = WHITE
UI_PANEL_HEIGHT = 100

# Asset paths
CELL_IMAGE_PATH = os.path.join("assets", "cell_basic.png")
FOOD_IMAGE_PATH = os.path.join("assets", "food_basic.png")
BACKGROUND_IMAGE_PATH = os.path.join("assets", "background_tile.png")
