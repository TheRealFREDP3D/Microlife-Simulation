Here’s your document reformatted cleanly into Markdown with hierarchy, code references, and structure preserved:

````markdown
# MicroLife Evolution Simulator - Core Mechanics

Complete evolutionary simulation system tracing from startup through organism life cycles, genetic mutation, environmental pressures, and food dynamics.  
Key locations include:

- Simulation initialization [1a]  
- Cell behavior orchestrator [2d]  
- Mutation mechanics [3c]  
- Environmental effects [4c]  
- Food ecosystem [5c]  

---

## 1. Simulation Startup & Initialization
Main entry point and world setup process. See guide.

### Simulation Initialization Flow
- **File:** `main.py` (entry point)

#### 1a. Create Simulation Instance
- **Location:** `main.py:7`
```python
sim = Simulation()
__init__() constructor
````

#### 1b. Initialize Environment

* **Location:** `simulation.py:12`

```python
self.environment = Environment()
__init__() constructor
initialize_clans()
```

#### 1c. Create Initial Clans

* **Location:** `environment.py:47`

```python
for i in range(INITIAL_CLAN_COUNT):
    Clan()  # instantiation
initialize_population()
```

#### 1d. Spawn Initial Cells

* **Location:** `environment.py:57`

```python
self.cells.append(Cell(x, y, clan))
initialize_zones()
```

#### 1e. Main Game Loop

* **Location:** `simulation.py:147`

```python
while running:
    pygame.event handling
    environment.update() loop
```

* **Setup:** `pygame.init()`

---

## 2. Cell Behavior & Life Cycle

Individual cell actions and survival mechanics. See guide.

### Cell Life Cycle Execution

* **Loop:** `Environment.update()`

#### 2a. Food Detection

* **Location:** `cell.py:78`

```python
def find_food(self, food_items):
    distance check & target set
```

#### 2b. Movement Logic

* **Location:** `cell.py:42`

```python
def move(self):
    target pursuit or random walk
    energy consumption calculation
```

#### 2c. Energy Consumption

* **Location:** `cell.py:89`

```python
def eat(self, food_items):
    food removal on contact
```

#### 2d. Cell Update Cycle

* **Location:** `cell.py:142`

```python
def update(self, food_items):
    age increment & trait sync
```

#### 2e. Death Conditions

* **Location:** `cell.py:156`

```python
if self.energy <= 0 or self.age >= self.lifespan:
    # Cell dies
```

* **Note:** `Environment` filters dead cells

---

## 3. Evolution & Reproduction System

Genetic inheritance and mutation mechanics. See guide.

### Evolution & Reproduction Flow

* **Trigger:** `Cell.update()` calls `reproduce()`

#### 3a. Reproduction Trigger

* **Location:** `cell.py:98`

```python
def reproduce(self, mate=None):
    # Energy threshold + Age check
```

#### 3b. Energy Splitting

* **Location:** `cell.py:108`

```python
self.energy /= 2
# Calculate offspring position
```

#### 3c. Mutation Check

* **Location:** `cell.py:114`

```python
if random.random() < CELL_MUTATION_RATE:
    # Mutate traits (speed, sense radius, energy efficiency, size, lifespan)
```

#### 3d. Trait Mutation

* **Location:** `clan.py:41`

```python
def apply_mutation(self, trait_name, mutation_amount):
    # Apply clan-level mutation
```

#### 3e. Offspring Creation

* **Location:** `cell.py:126`

```python
return Cell(offspring_x, offspring_y, self.clan, self.energy)
```

* Clan-level trait inheritance
* Traits stored in clan object
* All cells reference clan traits

---

## 4. Environmental Pressure System

Dynamic zones and their effects on organisms. See guide.

### Environmental System

* **Init:** `Environment.__init__()`

#### 4a. Zone Generation

* **Location:** `environment.py:69`

```python
def initialize_zones(self):
    Create toxic zones
    Create resource zones
```

#### 4b. Zone Dynamics

* **Location:** `environment.py:85`

```python
if self.environment_timer >= ENVIRONMENT_CHANGE_INTERVAL:
    Reinitialize zones
```

#### 4c. Toxic Damage

* **Location:** `environment.py:94`

```python
cell.energy -= TOXIC_ZONE_DAMAGE_PER_FRAME
# Check if cell is inside toxic zone
```

#### 4d. Resource Boost

* **Location:** `environment.py:119`

```python
food_spawn_multiplier = RESOURCE_ZONE_FOOD_BOOST
# Boost for cells in resource zones
```

---

## 5. Food Ecosystem Dynamics

Food spawning, decay, and consumption mechanics. See guide.

### Food Ecosystem Dynamics

* **Loop:** `Environment.update()` (main loop)
* Updates existing food items

#### 5a. Food Creation

* **Location:** `food.py:38`

```python
def spawn_food_item(x=None, y=None):
    # Called by environment or user (right click)
```

#### 5b. Food Decay

* **Location:** `food.py:32`

```python
def update(self):
    # Handles natural food decay
```

#### 5c. Dynamic Spawning

* **Location:** `environment.py:122`

```python
if len(self.food) < FOOD_MAX_COUNT and random.random() < FOOD_SPAWN_RATE_PER_FRAME * food_spawn_multiplier:
    # Spawn new food
```

#### 5d. Food Consumption

* **Location:** `cell.py:93`

```python
food_items.remove(self.target_food)
```

* Triggered in `cell.update()` via `cell.eat()`

---
