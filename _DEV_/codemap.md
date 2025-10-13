Perfect — here’s the **full Markdown document** with a clickable Table of Contents and a **Mermaid diagram** at the top to visualize the simulation flows.

You can drop this straight into a `.md` file, and both GitHub and Obsidian will render it properly (Mermaid diagrams work natively in both now).

---

````markdown
# MicroLife Simulation Ecosystem Interactions

Traces the core flows of cellular life simulation including initialization, update cycles, food-seeking, reproduction, and environmental interactions.  

**Key flows:**  
- Simulation bootstrap [1c]  
- Cell food pursuit [3d]  
- Clan-based reproduction [4e]  
- Environmental zone effects [5b]  

---

## Table of Contents
- [Mermaid Flow Diagram](#mermaid-flow-diagram)
- [1. Simulation Bootstrap and Ecosystem Initialization](#1-simulation-bootstrap-and-ecosystem-initialization)
  - [1a. Create Simulation Instance](#1a-create-simulation-instance)
  - [1b. Initialize Environment](#1b-initialize-environment)
  - [1c. Create Initial Clans](#1c-create-initial-clans)
  - [1d. Spawn Initial Cells](#1d-spawn-initial-cells)
  - [1e. Spawn Initial Food](#1e-spawn-initial-food)
- [2. Main Simulation Update Cycle](#2-main-simulation-update-cycle)
  - [2a. Environment Update Call](#2a-environment-update-call)
  - [2b. Update Each Cell](#2b-update-each-cell)
  - [2c. Handle Reproduction](#2c-handle-reproduction)
  - [2d. Update Food Items](#2d-update-food-items)
  - [2e. Dynamic Food Spawning](#2e-dynamic-food-spawning)
- [3. Cell Food-Seeking and Consumption Behavior](#3-cell-food-seeking-and-consumption-behavior)
  - [3a. Find Nearby Food](#3a-find-nearby-food)
  - [3b. Detect Food in Range](#3b-detect-food-in-range)
  - [3c. Move Towards Target](#3c-move-towards-target)
  - [3d. Execute Movement](#3d-execute-movement)
  - [3e. Attempt to Eat](#3e-attempt-to-eat)
  - [3f. Gain Energy](#3f-gain-energy)
- [4. Cell Reproduction and Clan Mutation](#4-cell-reproduction-and-clan-mutation)
  - [4a. Check Reproduction Conditions](#4a-check-reproduction-conditions)
  - [4b. Split Energy](#4b-split-energy)
  - [4c. Check for Mutation](#4c-check-for-mutation)
  - [4d. Apply Clan Mutations](#4d-apply-clan-mutations)
  - [4e. Create Offspring](#4e-create-offspring)
- [5. Environmental Zone Effects on Ecosystem](#5-environmental-zone-effects-on-ecosystem)
  - [5a. Detect Zone Overlap](#5a-detect-zone-overlap)
  - [5b. Apply Toxic Damage](#5b-apply-toxic-damage)
  - [5c. Check Resource Zone Usage](#5c-check-resource-zone-usage)
  - [5d. Apply Food Boost](#5d-apply-food-boost)
  - [5e. Regenerate Zones](#5e-regenerate-zones)

---

## Mermaid Flow Diagram

```mermaid
flowchart TD
    A[Simulation Bootstrap] --> B[Main Update Cycle]
    B --> C[Food-Seeking Behavior]
    C --> D[Reproduction & Mutation]
    D --> E[Environmental Zone Effects]
    E --> B
````

---

## 1. Simulation Bootstrap and Ecosystem Initialization

How the simulation starts up and creates the initial population of cells, food, and environmental zones.

### Simulation Bootstrap Process

* **main() entry point**

#### 1a. Create Simulation Instance

* **File:** `main.py:7`

```python
sim = Simulation()
```

* Calls `__init__()` constructor

#### 1b. Initialize Environment

* **File:** `simulation.py:12`

```python
self.environment = Environment()
```

* Calls `__init__()` constructor

#### 1c. Create Initial Clans

* **File:** `environment.py:43`

```python
self.initialize_clans()
for i in range(INITIAL_CLAN_COUNT):
    self.clans.append(Clan(...))
self.initialize_population()
```

* Spawns cells for each clan

#### 1d. Spawn Initial Cells

* **File:** `environment.py:63`

```python
self.cells.append(Cell(x, y, clan))
```

#### 1e. Spawn Initial Food

* **File:** `environment.py:67`

```python
self.food.append(spawn_food_item())
```

* `sim.run()` starts main loop
* `pygame.init()` setup

---

## 2. Main Simulation Update Cycle

The core loop that drives all organism behaviors and ecosystem changes each frame.

### Simulation Update Cycle

#### 2a. Environment Update Call

* **File:** `simulation.py:196`

```python
self.environment.update()
```

* Updates all cells
* Applies toxic zone damage

#### 2b. Update Each Cell

* **File:** `environment.py:97`

```python
if cell.update(self.food):
```

* Cell finds food & moves

#### 2c. Handle Reproduction

* **File:** `environment.py:100`

```python
offspring = cell.reproduce()
```

#### 2d. Update Food Items

* **File:** `environment.py:108`

```python
if food_item.update():
    # remove expired
```

#### 2e. Dynamic Food Spawning

* **File:** `environment.py:123`

```python
self.food.append(spawn_food_item())
```

* Periodic zone regeneration

---

## 3. Cell Food-Seeking and Consumption Behavior

How cells detect, pursue, and consume food resources.

### Cell Food-Seeking Behavior

#### 3a. Find Nearby Food

* **File:** `cell.py:186`

```python
self.find_food(food_items)
```

#### 3b. Detect Food in Range

* **File:** `cell.py:101`

```python
if dist < self.sense_radius and dist < min_dist:
    self.target_food = food
```

#### 3c. Move Towards Target

* **File:** `cell.py:187`

```python
self.move()
```

#### 3d. Execute Movement

* **File:** `cell.py:73`

```python
self.x += direction_x * move_amount
```

* Applies energy cost

#### 3e. Attempt to Eat

* **File:** `cell.py:188`

```python
self.eat(food_items)
```

#### 3f. Gain Energy

* **File:** `cell.py:108`

```python
self.energy += self.target_food.energy_value
```

* Removes food from environment

---

## 4. Cell Reproduction and Clan Mutation

Cells divide and pass on mutated clan traits.

### Cell Reproduction Process

#### 4a. Check Reproduction Conditions

* **File:** `cell.py:126`

```python
if self.energy >= CELL_REPRODUCTION_THRESHOLD and self.age >= CELL_MIN_AGE_TO_REPRODUCE:
```

#### 4b. Split Energy

* **File:** `cell.py:127`

```python
self.energy /= 2
```

#### 4c. Check for Mutation

* **File:** `cell.py:134`

```python
if random.random() < CELL_MUTATION_RATE:
```

#### 4d. Apply Clan Mutations

* **File:** `cell.py:135`

```python
self.clan.apply_mutation("speed", random.uniform(-CELL_MUTATION_AMOUNT, CELL_MUTATION_AMOUNT))
```

* Mutates: `sense_radius`, `energy_efficiency`, `size`, `lifespan`

#### 4e. Create Offspring

* **File:** `cell.py:146`

```python
return Cell(offspring_x, offspring_y, self.clan, self.energy)
```

---

## 5. Environmental Zone Effects on Ecosystem

How toxic and resource zones impact survival and food availability.

### Environmental Zone System

#### 5a. Detect Zone Overlap

* **File:** `environment.py:94`

```python
if get_distance((cell.x, cell.y), (zone.x, zone.y)) < zone.radius:
```

#### 5b. Apply Toxic Damage

* **File:** `environment.py:95`

```python
cell.energy -= TOXIC_ZONE_DAMAGE_PER_FRAME
```

#### 5c. Check Resource Zone Usage

* **File:** `environment.py:118`

```python
if any(get_distance((cell.x, cell.y), (zone.x, zone.y)) < zone.radius for cell in self.cells):
```

#### 5d. Apply Food Boost

* **File:** `environment.py:119`

```python
food_spawn_multiplier = RESOURCE_ZONE_FOOD_BOOST
```

#### 5e. Regenerate Zones

* **File:** `environment.py:86`

```python
self.initialize_zones()
```

* Creates toxic zones
* Creates resource zones

---

```

---

✅ That’s the complete `.md` file with a **TOC** and **Mermaid flowchart** at the top.  

Do you want me to also generate **separate Mermaid diagrams for each section** (like food-seeking, reproduction, environment) so it’s not just one high-level flow but also visual per-process?
```
