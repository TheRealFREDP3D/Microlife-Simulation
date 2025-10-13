# Repository Guidelines

## Project Structure & Module Organization
Core runtime code resides in `src/`, notably `simulation.py` (game loop), `environment.py` (world state), and `cell.py`/`clan.py` (organism rules). Configuration constants live in `src/constants.py`; keep balance tweaks centralized there. Store visual and audio assets in `assets/` and replace files in place to ship higher-resolution art. Temporary logs and profiler output are written to `logs/`; never commit this directory. Tests belong under `tests/`, while design notes and experiments go in `_DEV_/`. Use `data/` only for checked-in reference datasets such as `mutation_data.json`.

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: set up an isolated environment.
- `pip install -r requirements.txt` (or `requirements-dev.txt` for tooling): install runtime and dev dependencies, including `pygame`.
- `cd src && python main.py`: launch the simulator with the current assets.
- `cd src && python -m pytest`: run the full automated test suite.
- `cd src && python -m cProfile -o ../logs/profile.out simulation.py`: record a profiling session when investigating performance.

## Coding Style & Naming Conventions
Follow standard PEP 8 formatting with four-space indentation, `snake_case` functions/modules, and `CapWords` classes. Keep constants uppercase and defined in `constants.py`. Split gameplay logic between `Environment`, `Simulation`, and helpers in `utils.py` for clarity. Mirror existing resource-loading fallbacks seen in `cell.py` and `food.py` to fail gracefully when assets are missing.

## Testing Guidelines
Adopt `pytest` modules under `tests/` and give files descriptive names such as `test_environment.py`. Seed randomness (`random.seed(...)`) so clan behaviour stays reproducible across runs. Prefer headless checks that instantiate `Environment` and advance a few ticks, then assert on entity counts or energy totals. When UI changes resist automation, drop frame counts or summary notes in PR descriptions and attach relevant logs from `logs/`.

## Commit & Pull Request Guidelines
Use Conventional Commit subjects (`feat`, `fix`, `perf`, etc.) and include optional scopes, e.g., `feat(environment): add toxin field`. Each pull request should outline behavioural changes, list demo commands, link any tracking issues, and mention updated constants so reviewers can reproduce the same configuration. Add screenshots or short captures when modifying visuals or asset fidelity.

## Security & Configuration Tips
Do not commit API keys or system-specific paths; load sensitive values through environment variables. Keep local overrides in untracked files. When sharing binaries or new assets, ensure filenames remain identical to existing entries so runtime loaders continue to resolve them without code changes.
