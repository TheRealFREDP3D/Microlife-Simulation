## MicroLife Evolution Simulator - TODO

### Phase 1: Project Setup and Initial Structure

- [x] Create project directory (`microlife_evo_sim/`) and subdirectories (`src/`, `assets/`, `tests/`).
- [x] Create `todo.md` file for task tracking.
- [x] Create empty Python files for core components (`main.py`, `cell.py`, `environment.py`, `food.py`, `simulation.py`, `constants.py`, `utils.py`).
- [x] Implement basic Pygame window setup in `main.py` to display a black screen.
- [x] Plan and list required assets with descriptions (`asset_list.md`).
- [x] Create placeholder files for initial assets in `assets/` directory.
- [x] Verify that the basic Pygame window opens without errors.
- [x] Confirm project structure and asset placeholders are correctly set up.
- [x] Deliver project structure and asset list to the user.

### Phase 2: Core Component Implementation - Constants, Utilities, Cell, Food, Environment, Simulation

- [x] Implement `constants.py` with all global configuration values (screen dimensions, colors, cell/food properties, simulation parameters).
- [x] Implement `utils.py` with helper functions like `clamp` and `get_distance`.
- [x] Define `Cell` class structure in `cell.py` with basic attributes (position, energy, speed, sense radius, color, size).
- [x] Implement cell movement logic in `Cell.move()` (towards food if found, else random movement) and energy consumption.
- [x] Implement cell reproduction logic in `Cell.reproduce()` including energy splitting and basic trait mutation (simple additive/subtractive with boundaries).
- [x] Define `Food` class structure in `food.py` with attributes (position, energy value, color, size).
- [x] Implement `spawn_food` function in `food.py` to create new food items at random positions.
- [x] Define `Environment` class structure in `environment.py` to manage lists of cells and food.
- [x] Implement `Environment.initialize_population()` to create initial cells and food.
- [x] Implement `Environment.update()` to iterate through cells, update their state, handle reproduction, and spawn new food.
- [x] Implement `Environment.draw()` to render all cells and food items.
- [x] Define `Simulation` class structure in `simulation.py` to encapsulate the main game loop, Pygame initialization, and environment management.
- [x] Integrate all components into the main simulation loop in `main.py` by instantiating `Simulation` and calling its `run()` method.
- [x] Debug and optimize simulation logic to ensure basic interactions (movement, eating, reproduction, death) function correctly.
- [x] Implement basic visualization for cells (circles) and food (circles) using Pygame drawing primitives.

### Phase 3: Refine Cell Movement and Energy Management

- [x] Implement pathfinding/seeking behavior: Improve `Cell.find_food()` to prioritize closer or more energy-rich food sources within its `sense_radius` (Done).
- [x] Refine energy consumption: Adjust `CELL_ENERGY_CONSUMPTION_PER_MOVE` based on cell `speed` and `size` (e.g., faster/larger cells consume more energy) (Done).
- [x] Introduce idle energy drain: Cells should slowly lose energy even when not moving to simulate basic metabolic costs (Done).
- [x] Implement energy efficiency trait: Add a new trait `energy_efficiency` that reduces energy consumption, allowing for trade-offs during mutation (Done).
- [x] Verify refined movement: Observe cells moving more purposefully towards food and exhibiting varied energy levels (Done).
- [x] Test energy balance: Ensure cells can sustain themselves and reproduce under reasonable conditions, but also die if resources are scarce (Done).

### Phase 4: Implement Food Spawning and Consumption Logic

- [x] Implement varied food types: Introduce different `Food` types with varying `energy_value` and `size` (e.g., small, medium, large food) (Done).
- [x] Dynamic food spawning: Adjust `FOOD_SPAWN_RATE` based on current food density or cell population to prevent overpopulation or starvation (Done).
- [x] Food decay: Implement a mechanism for food to disappear after a certain time if not consumed, simulating spoilage (Done).
- [ ] Visual feedback for consumption: Add a small visual effect or sound when a cell consumes food (Deferred - low priority).
- [x] Verify food distribution: Ensure food spawns logically and supports the cell population without overwhelming or starving it (Done).
- [x] Test food types: Observe cells interacting differently with various food types (Done).

### Phase 5: Enhance Cell Reproduction and Mutation

- [x] Refine reproduction conditions: Cells might require a certain `age` or `health` in addition to `energy` to reproduce (Done).
- [x] Introduce new inheritable traits: Add traits like `size` (affecting energy consumption, food capacity, and collision box) or `lifespan` (Done).
- [x] Implement trait boundaries: Ensure all new traits have appropriate minimum and maximum values to prevent unrealistic extremes (Done).
- [x] Implement mutation impact: Allow mutation to affect multiple traits simultaneously with varying probabilities (Done).
- [x] Verify inheritance: Ensure offspring inherit traits from parents with slight variations due to mutation (Done).
- [x] Observe evolutionary trends: Look for observable changes in population traits over time (e.g., cells becoming faster or more efficient) (Done).

### Phase 6: Develop Basic UI and Information Display

- [x] Display population count: Show the current number of living cells and food items on screen (Done).
- [x] Display average traits: Show average `speed`, `sense_radius`, `energy_efficiency` of the current cell population (Done).
- [x] Implement pause/resume button: Allow users to pause and resume the simulation (Done).
- [x] Implement speed control: Allow users to adjust the simulation speed (e.g., 1x, 2x, 0.5x) (Done).
- [x] Verify UI elements: Ensure all UI elements are visible, readable, and functional (Done).
- [x] Test user controls: Confirm pause/resume and speed controls work as expected (Done).

### Phase 7: Implement Basic Environmental Factors

- [x] Implement environmental hazards: Introduce areas on the map that cause energy drain or damage to cells (e.g., 'toxic zones') (Done).
- [x] Implement resource rich zones: Introduce areas on the map where food spawns more frequently or provides more energy (Done).
- [x] Dynamic environment changes: Allow environmental factors to change over time (e.g., toxic zones appear/disappear, food rich zones shift) (Done).
- [x] Verify environmental impact: Observe cells avoiding hazards and congregating in resource-rich areas (Done).
- [x] Test dynamic changes: Ensure the environment changes as expected and cells adapt (Done).

### Phase 8: Add User Interaction (Pause/Resume, Spawn)

- [x] Implement manual cell spawning: Allow users to click on the screen to spawn new cells with default or randomized traits (Intentionally removed - conflicts with clan mechanic).
- [x] Implement manual food spawning: Allow users to click on the screen to spawn new food items (Done).
- [x] Implement selected cell inspection: When paused, allow users to click on a cell to view its current traits (speed, energy, sense radius, etc.) (Done).
- [x] Verify user input handling: Ensure mouse clicks and keyboard presses are correctly registered and trigger the intended actions (Done).
- [x] Test inspection: Confirm that cell details are displayed accurately upon selection (Done).

### Phase 9: Implement Basic Statistics and Logging

- [x] Track population history: Record cell and food counts over time (Done).
- [x] Track average trait values: Record average `speed`, `sense_radius`, `energy_efficiency` over time (Done).
- [ ] Implement simple data visualization: Display historical data as basic line graphs within the simulation window or save to a file (Deferred to future enhancement).
- [x] Log significant events: Record events like reproduction, death, and major mutations to a log file (Done).
- [x] Verify data accuracy: Ensure collected statistics accurately reflect the simulation state (Done).
- [x] Test logging: Confirm log files are created and contain relevant information (Done).

### Phase 10: Integrate Visual Assets

- [x] Load `cell_basic.png`: Replace `pygame.draw.circle` for cells with loaded image (Done).
- [x] Load `food_basic.png`: Replace `pygame.draw.circle` for food with loaded image (Done).
- [x] Load `background_tile.png`: Implement tiling background for the simulation area (Done).
- [x] Adjust rendering: Ensure images are scaled and positioned correctly based on cell/food size and position (Done).
- [x] Verify visual integration: Confirm that all placeholder graphics are replaced with the provided assets and render correctly (Done).
- [x] Test performance with assets: Ensure loading and rendering assets does not significantly degrade simulation performance (Done).

### Phase 11: Performance Optimization and Bug Fixing

- [ ] Profile code: Use Python's profiling tools to identify slow functions or sections of code (To be done locally).
- [ ] Optimize rendering: Implement techniques like dirty rects or sprite groups for more efficient drawing (To be done locally).
- [ ] Optimize collision detection: Use spatial partitioning (e.g., a grid system) to speed up `find_food` and other proximity checks (To be done locally).
- [ ] Review and fix bugs: Address any identified issues or unexpected behaviors in the simulation logic (To be done locally).
- [ ] Verify stability: Run the simulation for extended periods to check for crashes or memory leaks (To be done locally).
- [ ] Test accuracy: Ensure the simulation adheres to the defined rules and evolutionary principles (To be done locally).

### Phase 12: Final Review and Deliverable Packaging

- [ ] Code review: Ensure code adheres to best practices, is well-commented, and easy to understand (Ongoing).
- [x] Update `README.md`: Include instructions for running the final simulation, a summary of features, and any known issues (Done).
- [ ] Update `asset_list.md`: Ensure it accurately reflects all used assets (To be verified).
- [x] Clean up `todo.md`: Mark all completed tasks (Done).
- [ ] Create final `.zip` archive: Package all source code, assets, and documentation into a single, ready-to-distribute archive.
- [ ] Verify archive integrity: Ensure the `.zip` file is not corrupted and contains all necessary files.
- [ ] Deliver final package: Provide the user with the final `.zip` archive and a summary of the completed project.

### Phase 13: Implement Clan Mechanic - Core Logic

- [x] Define `Clan` class: Create a new class to hold clan-specific data, including a unique ID, a color, and a set of shared traits (speed, sense_radius, energy_efficiency, size, lifespan) (Done).
- [x] Modify `Cell` class: Update `Cell` to include a `clan_id` attribute and reference its clan's shared traits instead of individual traits for mutation and inheritance (Done).
- [x] Update `constants.py`: Add `INITIAL_CLAN_COUNT` and `CELLS_PER_CLAN` (Done).

### Phase 14: Implement Clan Mechanic - Initial Spawning and Grouping

- [x] Modify `Environment.initialize_population()`: Instead of spawning individual cells, spawn `INITIAL_CLAN_COUNT` clans (Done).
- [x] For each clan, spawn `CELLS_PER_CLAN` cells in a clustered area, assigning them the same `clan_id` and initial traits from their clan (Done).
- [x] Ensure initial clan colors are distinct for visual identification (Done).

### Phase 15: Implement Clan Mechanic - Initial Reproduction and Mating Rules

- [x] Modify `Cell.reproduce()`: Ensure that when a cell reproduces, its offspring inherits the parent's `clan_id` (Done).
- [x] Implement a check in `Cell.reproduce()` (or a new `mate` method) to only allow reproduction if the potential mate shares the same `clan_id` (Done).
- [x] Implement the initial reproduction trigger: After 20 seconds (or a defined number of frames), initial cells should attempt to reproduce (Done).

### Phase 16: Implement Clan Mechanic - Shared Traits and Mutations

- [x] Modify `Cell.reproduce()`: When a mutation occurs, update the trait directly in the `Clan` object associated with the reproducing cell, rather than mutating the individual cell's trait (Done).
- [x] Ensure all cells of a clan dynamically reflect these shared trait changes (e.g., by accessing `self.clan.speed` instead of `self.speed`) (Done).
- [x] Update `Cell` initialization to fetch traits from its assigned `Clan` object (Done).

### Phase 17: Verify Clan Mechanic and Update UI

- [x] Verify clan spawning: Confirm cells are grouped by clan and have distinct colors (Done).
- [x] Verify mating rules: Ensure cells only reproduce within their clan (Done).
- [x] Verify shared traits: Observe if mutations in one cell of a clan affect all other cells in that clan (e.g., all cells of a clan suddenly become faster) (Done).
- [x] Update UI: Display clan information (e.g., clan ID, average traits per clan, clan population count) (Done).
- [x] Add visual distinction for clans: Use `Clan.color` for drawing cells. (Done).

### Phase 18: Final Review and Deliverable Packaging for Clan Mechanic

- [x] Code review: Ensure clan-related code is clean, efficient, and well-documented (Done).
- [x] Update `README.md`: Add a section detailing the clan mechanic, its rules, and how it affects the simulation (Done).
- [x] Update `development_plan.md`: Mark all clan-related phases as completed (Done).
- [x] Clean up `todo.md`: Mark all clan-related tasks as completed (Done).
- [ ] Create final `.zip` archive: Package the updated project into a new distributable archive.
- [ ] Verify archive integrity: Ensure the `.zip` file is not corrupted and contains all necessary files.
- [ ] Deliver final package: Provide the user with the updated `.zip` archive and a summary of the new features.
