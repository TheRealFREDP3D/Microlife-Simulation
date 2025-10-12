# MicroLife Evolution Simulator

This project is an evolution simulator built using Pygame, designed to explore basic principles of natural selection and adaptation in a simplified environment.

## Project Structure

```
microlife_evo_sim/
├── README.md
├── asset_list.md
├── assets
│   ├── background_tile.png
│   ├── cell_basic.png
│   └── food_basic.png
├── src
│   ├── cell.py
│   ├── clan.py
│   ├── constants.py
│   ├── environment.py
│   ├── food.py
│   ├── main.py
│   ├── simulation.py
│   ├── utils.py
│   └── logs/ (automatically created for simulation logs)
├── tests
├── development_plan.md
└── todo.md
```

## Getting Started

### Prerequisites

To run this simulator, you will need Python 3.x and Pygame installed.

```bash
pip install pygame
```

### Running the Simulator

1.  **Add Assets**: Please place the actual image files for `cell_basic.png`, `food_basic.png`, and `background_tile.png` into the `assets/` directory. Placeholder files have been created for you. If images are not provided, the simulation will fall back to drawing colored circles and a black background.

2.  **Execute `main.py`**:

    ```bash
    cd microlife_evo_sim/src
    python3.11 main.py
    ```

### User Controls

*   `P`: Pause/Resume the simulation.
*   `Up Arrow`: Increase simulation speed.
*   `Down Arrow`: Decrease simulation speed.
*   `Left Click` (on simulation area): Selects a cell to display its traits when paused. (Manual cell spawning removed to support clan mechanics).
*   `Right Click` (on simulation area): Spawn a new food item at the mouse position.

## Current Status & Features

This project is a functional prototype with core simulation mechanics and basic UI. Key features implemented include:

*   **Clan Mechanic**: Organisms are grouped into clans. All descendants of initial specimens belong to the same clan. Clans have shared traits that mutate collectively. Cells only mate with specimens of the same clan.
    *   Initial simulation starts with `INITIAL_CLAN_COUNT` (default 3) clans, each spawning `CELLS_PER_CLAN` (default 2) cells grouped together.
    *   Initial cells automatically reproduce after `INITIAL_REPRODUCTION_TIME` (default 20 seconds).
*   **Cell Mechanics**: Movement towards food, energy consumption (movement and idle), reproduction with energy splitting, age-based death, and mutation of traits (speed, sense radius, energy efficiency, size, lifespan).
*   **Food System**: Varied food types with different energy values, sizes, and lifespans. Dynamic spawning based on food density and decay over time.
*   **Environmental Factors**: Toxic zones (damage cells) and resource zones (boost food spawning). Zones dynamically shift over time.
*   **Basic UI**: Displays cell and food counts, simulation speed, pause status, and average traits of the cell population. Allows inspection of individual cell traits when paused. Now also displays clan-specific information (ID, population, average traits) with distinct colors.
*   **Statistics & Logging**: Tracks population history and average trait values. Logs significant events and user actions to a timestamped file in the `logs/` directory.
*   **Visual Assets Integration**: Placeholder images for cells, food, and background are integrated. The simulation will use these if provided, otherwise it falls back to basic drawing. Cells are tinted with their clan's color.

## Next Steps (Future Enhancements)

*   **Performance Optimization**: Further optimize rendering and collision detection (best done locally with profiling tools).
*   **Advanced UI**: Implement graphical plots for statistics, more detailed cell inspection, and configurable simulation parameters.
*   **Predator/Prey Dynamics**: Introduce a predator species to add another layer of evolutionary pressure.
*   **Genetic Algorithms**: Implement more sophisticated genetic algorithms for trait inheritance and mutation.
*   **Persistence**: Save/load simulation states.

## Development Plan

The detailed development plan, outlining all phases and tasks, can be found in `development_plan.md`.

## Known Issues

*   Graphical output is not visible in the sandbox environment. Verification of visual elements and performance requires local execution.
*   Performance optimizations and bug fixing are best handled with local profiling and testing.


