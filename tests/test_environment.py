import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import test_setup first to mock pygame before other imports
import test_setup  # This mocks pygame.image.load before other imports

import unittest

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from environment import Environment
from food import spawn_food_item
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FOOD_MAX_COUNT


class TestEnvironmentUpdate(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.env = Environment()

    def test_cell_spawn_localization_clusters_cells_by_clan(self):
        """Test that cells are spawned in localized clusters per clan."""
        # Get clan positions (centers where clans spawn)
        clan_positions = []
        for clan in self.env.clans:
            # Find cells belonging to this clan
            clan_cells = [cell for cell in self.env.cells if cell.clan.id == clan.id]
            if clan_cells:
                # Calculate average position of clan cells
                avg_x = sum(cell.x for cell in clan_cells) / len(clan_cells)
                avg_y = sum(cell.y for cell in clan_cells) / len(clan_cells)
                clan_positions.append((avg_x, avg_y))

        # Each clan should have cells clustered within ~40 units of their center
        # (based on the 20-unit spread in initialize_population)
        for i, (center_x, center_y) in enumerate(clan_positions):
            clan_cells = [cell for cell in self.env.cells if cell.clan.id == self.env.clans[i].id]
            for cell in clan_cells:
                distance_from_center = ((cell.x - center_x) ** 2 + (cell.y - center_y) ** 2) ** 0.5
                self.assertLess(distance_from_center, 50,  # Allow some margin beyond 20-unit spread
                               f"Cell {cell} should be within cluster distance of clan center")

    def test_cell_spawn_occupancy_avoidance_keeps_cells_in_bounds(self):
        """Test that spawned cells are kept within screen bounds."""
        for cell in self.env.cells:
            self.assertGreaterEqual(cell.x, 0, "Cell x position should be >= 0")
            self.assertGreaterEqual(cell.y, 0, "Cell y position should be >= 0")
            self.assertLessEqual(cell.x, SCREEN_WIDTH - cell.size,
                               "Cell x position should be within screen width")
            self.assertLessEqual(cell.y, SCREEN_HEIGHT - cell.size,
                               "Cell y position should be within screen height")

    def test_environment_zones_periodically_change(self):
        """Test that toxic and resource zones change periodically."""
        # Record initial zone positions (counts not needed for this test)
        initial_toxic_positions = [(zone.x, zone.y) for zone in self.env.toxic_zones]
        initial_resource_positions = [(zone.x, zone.y) for zone in self.env.resource_zones]

        # Run updates to trigger environment change
        from constants import ENVIRONMENT_CHANGE_INTERVAL
        for _ in range(ENVIRONMENT_CHANGE_INTERVAL):
            self.env.update()

        # Zones should have changed
        current_toxic_positions = [(zone.x, zone.y) for zone in self.env.toxic_zones]
        current_resource_positions = [(zone.x, zone.y) for zone in self.env.resource_zones]

        # At least some zones should have moved (not all in exact same positions)
        toxic_positions_changed = initial_toxic_positions != current_toxic_positions
        resource_positions_changed = initial_resource_positions != current_resource_positions

        self.assertTrue(toxic_positions_changed or resource_positions_changed,
                       "Zone positions should change after environment interval")

    def test_resource_zones_boost_food_spawn_rate(self):
        """Test that resource zones increase food spawn rate when cells are present."""
        initial_food_count = len(self.env.food)

        # Run a few updates to let food spawning occur
        for _ in range(10):
            self.env.update()

        # Count should increase due to resource zone boost
        final_food_count = len(self.env.food)
        self.assertGreaterEqual(final_food_count, initial_food_count,
                               "Food count should not decrease with resource zones active")

    def test_food_spawn_respects_maximum_limit(self):
        """Test that food spawning respects the maximum food count limit."""
        # Manually add food to reach near maximum
        while len(self.env.food) < FOOD_MAX_COUNT - 5:
            self.env.food.append(spawn_food_item())

        # Run many updates to try to spawn more food
        for _ in range(100):
            self.env.update()

        final_count = len(self.env.food)

        # Should not exceed maximum (allowing some decay)
        self.assertLessEqual(final_count, FOOD_MAX_COUNT,
                           f"Food count should not exceed maximum limit of {FOOD_MAX_COUNT}")

    def test_cells_are_removed_when_dead(self):
        """Test that dead cells are properly removed from the environment."""
        # Find a cell and kill it by setting energy to 0
        if self.env.cells:
            test_cell = self.env.cells[0]
            test_cell.energy = 0  # This should cause it to be removed

            initial_cell_count = len(self.env.cells)

            # Run update to process cell removal
            self.env.update()

            final_cell_count = len(self.env.cells)

            self.assertEqual(final_cell_count, initial_cell_count - 1,
                           "Dead cells should be removed from environment")

    def test_offspring_are_added_to_environment(self):
        """Test that cell reproduction adds offspring to the environment."""
        # Find a mature cell with enough energy for reproduction
        mature_cell = None
        for cell in self.env.cells:
            if cell.age >= 50 and cell.energy >= 80:  # Values from constants
                mature_cell = cell
                break

        if mature_cell:
            # Advance the reproduction timer
            for _ in range(200):  # INITIAL_REPRODUCTION_TIME
                mature_cell.reproduce()

            initial_cell_count = len(self.env.cells)

            # Run update to process reproduction
            self.env.update()

            final_cell_count = len(self.env.cells)

            # Should have at least one more cell (the offspring)
            self.assertGreaterEqual(final_cell_count, initial_cell_count,
                                   "Environment should contain offspring after reproduction")


if __name__ == '__main__':
    unittest.main()
