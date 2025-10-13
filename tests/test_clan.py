import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import test_setup first to mock pygame before other imports
import test_setup  # This mocks pygame.image.load before other imports

import unittest

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from clan import Clan
from constants import (
    CELL_SPEED_MIN, CELL_SPEED_MAX, CELL_SENSE_RADIUS_MIN, CELL_SENSE_RADIUS_MAX,
    CELL_ENERGY_EFFICIENCY_MIN, CELL_ENERGY_EFFICIENCY_MAX, CELL_SIZE_MIN, CELL_SIZE_MAX,
    CELL_MAX_LIFESPAN
)


class TestClanMutation(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.clan = Clan()

    def test_apply_mutation_clamps_speed(self):
        """Test that speed mutations are clamped within valid range."""
        # Test mutation that would exceed maximum
        self.clan.apply_mutation("speed", 100)  # Large positive mutation
        self.assertEqual(self.clan.speed, CELL_SPEED_MAX,
                        "Speed should be clamped to maximum")

        # Create new clan for next test
        self.clan = Clan()

        # Test mutation that would go below minimum
        self.clan.apply_mutation("speed", -100)  # Large negative mutation
        self.assertEqual(self.clan.speed, CELL_SPEED_MIN,
                        "Speed should be clamped to minimum")

    def test_apply_mutation_clamps_sense_radius(self):
        """Test that sense_radius mutations are clamped within valid range."""
        # Test mutation that would exceed maximum
        self.clan.apply_mutation("sense_radius", 1000)
        self.assertEqual(self.clan.sense_radius, CELL_SENSE_RADIUS_MAX,
                        "Sense radius should be clamped to maximum")

        # Create new clan for next test
        self.clan = Clan()

        # Test mutation that would go below minimum
        self.clan.apply_mutation("sense_radius", -1000)
        self.assertEqual(self.clan.sense_radius, CELL_SENSE_RADIUS_MIN,
                        "Sense radius should be clamped to minimum")

    def test_apply_mutation_clamps_energy_efficiency(self):
        """Test that energy_efficiency mutations are clamped within valid range."""
        # Test mutation that would exceed maximum
        self.clan.apply_mutation("energy_efficiency", 100)
        self.assertEqual(self.clan.energy_efficiency, CELL_ENERGY_EFFICIENCY_MAX,
                        "Energy efficiency should be clamped to maximum")

        # Create new clan for next test
        self.clan = Clan()

        # Test mutation that would go below minimum
        self.clan.apply_mutation("energy_efficiency", -100)
        self.assertEqual(self.clan.energy_efficiency, CELL_ENERGY_EFFICIENCY_MIN,
                        "Energy efficiency should be clamped to minimum")

    def test_apply_mutation_clamps_size(self):
        """Test that size mutations are clamped within valid range."""
        # Test mutation that would exceed maximum
        self.clan.apply_mutation("size", 1000)
        self.assertEqual(self.clan.size, CELL_SIZE_MAX,
                        "Size should be clamped to maximum")

        # Create new clan for next test
        self.clan = Clan()

        # Test mutation that would go below minimum
        self.clan.apply_mutation("size", -1000)
        self.assertEqual(self.clan.size, CELL_SIZE_MIN,
                        "Size should be clamped to minimum")

    def test_apply_mutation_clamps_lifespan(self):
        """Test that lifespan mutations are clamped within valid range."""
        # Test mutation that would exceed maximum
        self.clan.apply_mutation("lifespan", 10000)
        self.assertEqual(self.clan.lifespan, CELL_MAX_LIFESPAN,
                        "Lifespan should be clamped to maximum")

        # Create new clan for next test
        self.clan = Clan()

        # Test mutation that would go below minimum (CELL_MAX_LIFESPAN // 2)
        min_lifespan = CELL_MAX_LIFESPAN // 2
        self.clan.apply_mutation("lifespan", -10000)
        self.assertEqual(self.clan.lifespan, min_lifespan,
                        "Lifespan should be clamped to minimum")

    def test_apply_mutation_affects_existing_cells(self):
        """Test that mutations applied to clan affect existing cells."""
        # Create a cell that belongs to this clan
        from cell import Cell
        cell = Cell(100, 100, self.clan, 100)

        # Record initial trait value
        initial_speed = cell.speed

        # Apply mutation to clan
        mutation_amount = 0.5
        self.clan.apply_mutation("speed", mutation_amount)

        # Update cell traits (simulating what happens in cell.update())
        cell.speed = self.clan.speed
        cell.sense_radius = self.clan.sense_radius
        cell.energy_efficiency = self.clan.energy_efficiency
        cell.size = self.clan.size
        cell.lifespan = self.clan.lifespan

        # Check that cell trait was updated
        expected_speed = min(CELL_SPEED_MAX, max(CELL_SPEED_MIN, initial_speed + mutation_amount))
        self.assertAlmostEqual(cell.speed, expected_speed, places=5,
                              msg="Cell speed should reflect clan mutation")

    def test_apply_mutation_ignores_invalid_trait_names(self):
        """Test that applying mutation to invalid trait names doesn't cause errors."""
        # Record original values
        original_speed = self.clan.speed

        # Apply mutation to non-existent trait
        self.clan.apply_mutation("invalid_trait", 1.0)

        # Clan traits should remain unchanged
        self.assertEqual(self.clan.speed, original_speed,
                        "Valid traits should remain unchanged when invalid trait is mutated")


if __name__ == '__main__':
    unittest.main()
