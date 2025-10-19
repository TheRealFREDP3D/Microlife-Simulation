# MicroLife Evolution Simulator

A Pygame-based evolution simulator that explores natural selection, adaptation, and clan-based evolution in a dynamic environment. This project simulates microorganisms competing for resources, reproducing, and evolving over generations.

---  

<iframe width="560" height="315" src="https://www.youtube.com/embed/_LaB4yQZgFE?si=Ft6XFWCquz5-Igz2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---  

## Project Structure

```text
Microlife-Simulation/
├── _DEV_/                      # Development documentation and planning
│   └── development_plan.md     # Detailed development roadmap
├── assets/                     # Visual assets (images, sprites)
│   ├── background_tile.png     # Background texture
│   ├── cell_basic.png          # Base cell sprite
│   └── food_basic.png          # Base food sprite
├── data/
│   └── mutation_data.json      # Configuration for mutation parameters
├── logs/                       # Auto-generated simulation logs
├── src/                        # Source code
│   ├── cell.py                 # Cell class and behavior
│   ├── clan.py                 # Clan management and traits
│   ├── constants.py            # Game configuration
│   ├── environment.py          # World state and management
│   ├── food.py                 # Food generation and behavior
│   ├── main.py                 # Entry point
│   ├── simulation.py           # Main simulation loop
│   └── utils.py                # Helper functions
├── tests/                      # Test suite
├── .gitignore
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

## Features

### Core Mechanics

- **Clan-based Evolution**: Organisms belong to clans with shared, heritable traits
- **Dynamic Environment**: Shifting resource zones and hazards
- **Energy System**: Cells consume energy for movement and reproduction
- **Trait Inheritance**: Offspring inherit and mutate traits from parent cells

### Simulation Controls

- `P`: Pause/Resume simulation
- `↑/↓`: Adjust simulation speed (0.5x to 4x)
- `Left Click`: Select cell (when paused) to view traits
- `Right Click`: Spawn food at cursor position
- `Reset Button`: Restart simulation with new random seed

### Visual Feedback

- Color-coded clans for easy identification
- Real-time statistics panel
- Cell selection highlights and info display
- Environmental zone visualization

## Getting Started

### Prerequisites

- Python 3.11+
- Pygame 2.5+

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Microlife-Simulation.git
   cd Microlife-Simulation
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulation:

   ```bash
   cd src
   python main.py
   ```

## Configuration

Key parameters can be adjusted in `src/constants.py`:

- World dimensions and scale
- Initial population settings
- Energy and reproduction rules
- Mutation rates and ranges
- Environmental factors

## Development Status

### Current Version: 1.0.0 (Stable)

### Recent Updates

- Implemented clan-based evolution mechanics
- Added dynamic environmental zones
- Improved performance and stability
- Enhanced visualization and UI

### Known Issues

- High cell populations may impact performance
- Occasional food spawning overlap
- Detailed statistics visualization pending

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Pygame
- Inspired by classic artificial life simulations
- Special thanks to all contributors
