# MicroLife Evolution Simulator - Detailed Development Plan

This plan outlines the incremental development of the MicroLife Evolution Simulator, breaking down the project into manageable phases. Each phase focuses on a specific set of features, ensuring thorough implementation and verification before proceeding.

## Phase 1: Project Setup and Initial Structure (Completed)

**Overview**: Establish the foundational project structure, including directories, initial Python files, and a basic Pygame window to ensure the development environment is correctly configured.

**Task List**:

- [x] Create project directory (`microlife_evo_sim/`) and subdirectories (`src/`, `assets/`, `tests/`).
- [x] Create `todo.md` file for task tracking.
- [x] Create empty Python files for core components (`main.py`, `cell.py`, `environment.py`, `food.py`, `simulation.py`, `constants.py`, `utils.py`).
- [x] Implement basic Pygame window setup in `main.py` to display a black screen.
- [x] Plan and list required assets with descriptions (`asset_list.md`).
- [x] Create placeholder files for initial assets in `assets/` directory.
- [x] Verify that the basic Pygame window opens without errors.
- [x] Confirm project structure and asset placeholders are correctly set up.
- [x] Deliver project structure and asset list to the user.

**Expected Result**: A functional project directory with all necessary subdirectories and empty Python files. A basic Pygame window that opens and closes correctly. A `README.md` and `asset_list.md` document.

## Phase 2: Core Component Implementation - Constants, Utilities, Cell, Food, Environment, Simulation (Completed)

**Overview**: Implement the foundational classes and modules that define the core entities and mechanics of the simulation, including constants, utility functions, and the basic behavior of cells, food, and their environment.

**Task List**:

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

**Expected Result**: A runnable simulation where cells move, consume food, reproduce, and die. Basic visual representation of cells and food. The core game loop is functional, demonstrating the fundamental mechanics of the simulator.

## Phase 3: Refine Cell Movement and Energy Management (Completed)

**Overview**: Enhance the realism and strategic depth of cell behavior by refining movement patterns, optimizing energy consumption, and introducing more nuanced interactions with the environment.

**Task List**:

- [x] **Implement pathfinding/seeking behavior**: Improve `Cell.find_food()` to prioritize closer or more energy-rich food sources within its `sense_radius`.
- [x] **Refine energy consumption**: Adjust `CELL_ENERGY_CONSUMPTION_PER_MOVE` based on cell `speed` and `size` (e.g., faster/larger cells consume more energy).
- [x] **Introduce idle energy drain**: Cells should slowly lose energy even when not moving to simulate basic metabolic costs.
- [x] **Implement energy efficiency trait**: Add a new trait `energy_efficiency` that reduces energy consumption, allowing for trade-offs during mutation.
- [x] **Verify refined movement**: Observe cells moving more purposefully towards food and exhibiting varied energy levels.
- [x] **Test energy balance**: Ensure cells can sustain themselves and reproduce under reasonable conditions, but also die if resources are scarce.

**Expected Result**: Cells exhibit more intelligent and varied movement patterns. Energy management is more dynamic, reflecting cell traits and actions. The simulation feels more strategic regarding energy use.

## Phase 4: Implement Food Spawning and Consumption Logic (Completed)

**Overview**: Develop a more sophisticated food system, including varied food types, dynamic spawning, and clearer consumption mechanics to create a richer resource landscape.

**Task List**:

- [x] **Implement varied food types**: Introduce different `Food` types with varying `energy_value` and `size` (e.g., small, medium, large food).
- [x] **Dynamic food spawning**: Adjust `FOOD_SPAWN_RATE` based on current food density or cell population to prevent overpopulation or starvation.
- [x] **Food decay**: Implement a mechanism for food to disappear after a certain time if not consumed, simulating spoilage.
- [ ] **Visual feedback for consumption**: Add a small visual effect or sound when a cell consumes food. *(Deferred - low priority)*
- [x] **Verify food distribution**: Ensure food spawns logically and supports the cell population without overwhelming or starving it.
- [x] **Test food types**: Observe cells interacting differently with various food types.

**Expected Result**: A dynamic and balanced food ecosystem. Cells interact with food in more diverse ways. The simulation environment feels more alive and responsive to population changes.

## Phase 5: Enhance Cell Reproduction and Mutation (Completed)

**Overview**: Deepen the evolutionary aspect by refining reproduction conditions, introducing more complex mutation mechanics, and potentially adding new inheritable traits.

**Task List**:

- [x] **Refine reproduction conditions**: Cells might require a certain `age` or `health` in addition to `energy` to reproduce.
- [x] **Introduce new inheritable traits**: Add traits like `size` (affecting energy consumption, food capacity, and collision box) or `lifespan`.
- [x] **Implement trait boundaries**: Ensure all new traits have appropriate minimum and maximum values to prevent unrealistic extremes.
- [x] **Implement mutation impact**: Allow mutation to affect multiple traits simultaneously with varying probabilities.
- [x] **Verify inheritance**: Ensure offspring inherit traits from parents with slight variations due to mutation.
- [x] **Observe evolutionary trends**: Look for observable changes in population traits over time (e.g., cells becoming faster or more efficient).

**Expected Result**: Clearer evolutionary pressure and observable changes in cell populations over generations. Cells develop specialized traits based on environmental conditions.

## Phase 6: Develop Basic UI and Information Display (Completed)

**Overview**: Create a user interface to display key simulation metrics and allow for basic interaction, providing insights into the ongoing evolution.

**Task List**:

- [x] **Display population count**: Show the current number of living cells and food items on screen.
- [x] **Display average traits**: Show average `speed`, `sense_radius`, `energy_efficiency` of the current cell population.
- [x] **Implement pause/resume button**: Allow users to pause and resume the simulation.
- [x] **Implement speed control**: Allow users to adjust the simulation speed (e.g., 1x, 2x, 0.5x).
- [x] **Verify UI elements**: Ensure all UI elements are visible, readable, and functional.
- [x] **Test user controls**: Confirm pause/resume and speed controls work as expected.

**Expected Result**: A user-friendly interface that provides real-time information about the simulation state and allows for basic control.

## Phase 7: Implement Basic Environmental Factors (Completed)

**Overview**: Introduce simple environmental elements that influence cell behavior and survival, adding another layer of complexity to the evolutionary process.

**Task List**:

- [x] **Implement environmental hazards**: Introduce areas on the map that cause energy drain or damage to cells (e.g., 'toxic zones').
- [x] **Implement resource rich zones**: Introduce areas on the map where food spawns more frequently or provides more energy.
- [x] **Dynamic environment changes**: Allow environmental factors to change over time (e.g., toxic zones appear/disappear, food rich zones shift).
- [x] **Verify environmental impact**: Observe cells avoiding hazards and congregating in resource-rich areas.
- [x] **Test dynamic changes**: Ensure the environment changes as expected and cells adapt.

**Expected Result**: The environment plays a more active role in shaping cell evolution, leading to more complex adaptive strategies.

## Phase 8: Add User Interaction (Pause/Resume, Spawn) (Completed)

**Overview**: Enhance user control over the simulation, allowing for direct manipulation of the environment and population.

**Task List**:

- [x] **Implement manual cell spawning**: Allow users to click on the screen to spawn new cells with default or randomized traits. *(Intentionally removed to maintain clan mechanic integrity - cells must belong to a clan)*
- [x] **Implement manual food spawning**: Allow users to click on the screen to spawn new food items.
- [x] **Implement selected cell inspection**: When paused, allow users to click on a cell to view its current traits (speed, energy, sense radius, etc.).
- [x] **Verify user input handling**: Ensure mouse clicks and keyboard presses are correctly registered and trigger the intended actions.
- [x] **Test inspection**: Confirm that cell details are displayed accurately upon selection.

**Note**: Manual cell spawning was intentionally disabled to maintain consistency with the clan mechanic. All cells must belong to a clan and inherit clan-specific traits.

**Expected Result**: Users can directly influence the simulation, experimenting with different starting conditions and observing immediate effects.

## Phase 9: Implement Basic Statistics and Logging (Completed)

**Overview**: Collect and display quantitative data about the simulation, providing deeper insights into evolutionary trends and population dynamics.

**Task List**:

- [x] **Track population history**: Record cell and food counts over time.
- [x] **Track average trait values**: Record average `speed`, `sense_radius`, `energy_efficiency` over time.
- [ ] **Implement simple data visualization**: Display historical data as basic line graphs within the simulation window or save to a file. *(Deferred to future enhancement)*
- [x] **Log significant events**: Record events like reproduction, death, and major mutations to a log file.
- [x] **Verify data accuracy**: Ensure collected statistics accurately reflect the simulation state.
- [x] **Test logging**: Confirm log files are created and contain relevant information.

**Note**: Graphical data visualization is deferred as a future enhancement. Current implementation logs all data to timestamped files in the `logs/` directory.

**Expected Result**: Quantitative data is available to analyze evolutionary patterns. Users can review historical trends and significant events.

## Phase 10: Integrate Visual Assets (Completed)

**Overview**: Replace placeholder graphics with user-provided visual assets to enhance the aesthetic appeal and clarity of the simulation.

**Task List**:

- [x] **Load `cell_basic.png`**: Replace `pygame.draw.circle` for cells with loaded image.
- [x] **Load `food_basic.png`**: Replace `pygame.draw.circle` for food with loaded image.
- [x] **Load `background_tile.png`**: Implement tiling background for the simulation area.
- [x] **Adjust rendering**: Ensure images are scaled and positioned correctly based on cell/food size and position.
- [x] **Verify visual integration**: Confirm that all placeholder graphics are replaced with the provided assets and render correctly.
- [x] **Test performance with assets**: Ensure loading and rendering assets does not significantly degrade simulation performance.

**Note**: Implementation includes graceful fallback to basic shapes if asset files are missing.

**Expected Result**: The simulation has a polished visual appearance, using the custom assets provided by the user.

## Phase 11: Performance Optimization and Bug Fixing

**Overview**: Identify and resolve performance bottlenecks and bugs to ensure a smooth, stable, and accurate simulation experience.

**Task List**:

- [ ] **Profile code**: Use Python's profiling tools to identify slow functions or sections of code.
- [ ] **Optimize rendering**: Implement techniques like dirty rects or sprite groups for more efficient drawing.
- [ ] **Optimize collision detection**: Use spatial partitioning (e.g., a grid system) to speed up `find_food` and other proximity checks.
- [ ] **Review and fix bugs**: Address any identified issues or unexpected behaviors in the simulation logic.
- [ ] **Verify stability**: Run the simulation for extended periods to check for crashes or memory leaks.
- [ ] **Test accuracy**: Ensure the simulation adheres to the defined rules and evolutionary principles.

**Expected Result**: A stable, performant, and bug-free simulation that runs smoothly even with large populations.

## Phase 12: Final Review and Deliverable Packaging

**Overview**: Conduct a final review of the entire project, ensure all documentation is up-to-date, and package the project for easy distribution.

**Task List**:

- [ ] Code review: Ensure code adheres to best practices, is well-commented, and easy to understand.
- [ ] Update `README.md`: Include instructions for running the final simulation, a summary of features, and any known issues.
- [ ] Update `asset_list.md`: Ensure it accurately reflects all used assets.
- [ ] Clean up `todo.md`: Mark all completed tasks.
- [ ] Create final `.zip` archive: Package all source code, assets, and documentation into a single, ready-to-distribute archive.
- [ ] Verify archive integrity: Ensure the `.zip` file is not corrupted and contains all necessary files.
- [ ] Deliver final package: Provide the user with the final `.zip` archive and a summary of the completed project.

**Expected Result**: A complete, well-documented, and easily deployable MicroLife Evolution Simulator project, ready for user review and further development.

---

### Phase 13: Implement Clan Mechanic - Core Logic (Completed)

**Overview**: Introduce the fundamental concept of clans, including a `Clan` class to manage shared traits and unique identification.

**Tasks**:

- Define `Clan` class: Create a new class to hold clan-specific data, including a unique ID, a color, and a set of shared traits (speed, sense_radius, energy_efficiency, size, lifespan).
- Modify `Cell` class: Update `Cell` to include a `clan_id` attribute and reference its clan's shared traits instead of individual traits for mutation and inheritance.
- Update `constants.py`: Add `INITIAL_CLAN_COUNT` and `CELLS_PER_CLAN`.

**Expected Result**: A `Clan` class that can manage shared traits and cells that are associated with a specific clan, inheriting their characteristics from it.

---

### Phase 14: Implement Clan Mechanic - Initial Spawning and Grouping (Completed)

**Overview**: Adjust the initial population generation to create multiple clans, with cells from each clan spawning in proximity.

**Tasks**:

- [x] Modify `Environment.initialize_population()`: Instead of spawning individual cells, spawn `INITIAL_CLAN_COUNT` clans.
- [x] For each clan, spawn `CELLS_PER_CLAN` cells in a clustered area, assigning them the same `clan_id` and initial traits from their clan.
- [x] Ensure initial clan colors are distinct for visual identification.

**Expected Result**: The simulation starts with distinct groups of cells, each representing a clan, visually grouped and identifiable by color.

---

### Phase 15: Implement Clan Mechanic - Initial Reproduction and Mating Rules (Completed)

**Overview**: Enforce mating rules where cells can only reproduce with other cells from the same clan.

**Tasks**:

- [x] Modify `Cell.reproduce()`: Ensure that when a cell reproduces, its offspring inherits the parent's `clan_id`.
- [x] Implement a check in `Cell.reproduce()` (or a new `mate` method) to only allow reproduction if the potential mate shares the same `clan_id`.
- [x] Implement the initial reproduction trigger: After 20 seconds (or a defined number of frames), initial cells should attempt to reproduce.

**Expected Result**: Clans maintain their genetic lineage, and initial cells quickly establish their clan's presence through reproduction.

---

### Phase 16: Implement Clan Mechanic - Shared Traits and Mutations (Completed)

**Overview**: Centralize trait management within the `Clan` class, so mutations affect all members of a clan.

**Tasks**:

- [x] Modify `Cell.reproduce()`: When a mutation occurs, update the trait directly in the `Clan` object associated with the reproducing cell, rather than mutating the individual cell's trait.
- [x] Ensure all cells of a clan dynamically reflect these shared trait changes (e.g., by accessing `self.clan.speed` instead of `self.speed`).
- [x] Update `Cell` initialization to fetch traits from its assigned `Clan` object.

**Expected Result**: Evolutionary changes (mutations) propagate across entire clans, leading to distinct clan-specific adaptations over time.

---

### Phase 17: Verify Clan Mechanic and Update UI (Completed)

**Overview**: Test the new clan system thoroughly and update the UI to display clan-specific information.

**Tasks**:

- [x] Verify clan spawning: Confirm cells are grouped by clan and have distinct colors.
- [x] Verify mating rules: Ensure cells only reproduce within their clan.
- [x] Verify shared traits: Observe if mutations in one cell of a clan affect all other cells in that clan (e.g., all cells of a clan suddenly become faster).
- [x] Update UI: Display clan information (e.g., clan ID, average traits per clan, clan population count).
- [x] Add visual distinction for clans: Use `Clan.color` for drawing cells.

**Expected Result**: A fully functional clan system with observable clan behaviors and clear UI feedback.

---

### Phase 18: Final Review and Deliverable Packaging for Clan Mechanic

**Overview**: Review the implemented clan mechanic, update documentation, and prepare a new project package.

**Tasks**:

- Code review: Ensure clan-related code is clean, efficient, and well-documented.
- Update `README.md`: Add a section detailing the clan mechanic, its rules, and how it affects the simulation.
- Update `development_plan.md`: Mark all clan-related phases as completed.
- Clean up `todo.md`: Mark all clan-related tasks as completed.
- Create final `.zip` archive: Package the updated project into a new distributable archive.
- Verify archive integrity: Ensure the `.zip` file is not corrupted and contains all necessary files.
- Deliver final package: Provide the user with the updated `.zip` archive and a summary of the new features.

**Expected Result**: A complete, well-documented, and distributable version of the simulator with the clan mechanic fully integrated and explained.
