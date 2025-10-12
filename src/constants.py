
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
PURPLE = (128, 0, 128) # For toxic zones
LIGHT_BLUE = (173, 216, 230) # For resource zones

# Clan properties
INITIAL_CLAN_COUNT = 3
CELLS_PER_CLAN = 2
CLAN_COLORS = [
    (255, 0, 0),    # Red
    (0, 0, 255),    # Blue
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255)   # Cyan
] # A list of distinct colors for clans

# Cell properties
INITIAL_CELL_COUNT = 10 # This will be overridden by clan spawning
CELL_SIZE_MIN = 5
CELL_SIZE_MAX = 15
CELL_COLOR = GREEN # Default color, will be overridden by clan color
CELL_ENERGY_MAX = 100
CELL_ENERGY_CONSUMPTION_PER_MOVE_BASE = 0.05 # Base energy consumption per unit of movement
CELL_IDLE_ENERGY_DRAIN = 0.002 # Energy drained per frame when idle (reduced from 0.01)
CELL_REPRODUCTION_THRESHOLD = 60 # Energy required for reproduction (reduced from 80)
CELL_MIN_AGE_TO_REPRODUCE = 30 # Minimum age in frames before a cell can reproduce (reduced from 100)
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
INITIAL_FOOD_COUNT = 50
FOOD_TYPES = [
    {"size": 5, "energy_value": 20, "color": BLUE, "lifespan": 300}, # Small, low energy, short lifespan
    {"size": 8, "energy_value": 40, "color": RED, "lifespan": 600}, # Medium, medium energy, medium lifespan
    {"size": 12, "energy_value": 60, "color": PURPLE, "lifespan": 900}  # Large, high energy, long lifespan
]
FOOD_SPAWN_RATE_PER_FRAME = 0.05 # Average number of food items to spawn per frame (e.g., 0.05 means 1 food every 20 frames)
FOOD_MAX_COUNT = 100 # Maximum number of food items on screen

# Environmental factors
TOXIC_ZONE_COUNT = 2
TOXIC_ZONE_SIZE_MIN = 50
TOXIC_ZONE_SIZE_MAX = 150
TOXIC_ZONE_DAMAGE_PER_FRAME = 0.5
RESOURCE_ZONE_COUNT = 2
RESOURCE_ZONE_SIZE_MIN = 50
RESOURCE_ZONE_SIZE_MAX = 150
RESOURCE_ZONE_FOOD_BOOST = 2 # Multiplier for food spawn rate in resource zones
ENVIRONMENT_CHANGE_INTERVAL = 600 # Frames after which environment zones might shift

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
