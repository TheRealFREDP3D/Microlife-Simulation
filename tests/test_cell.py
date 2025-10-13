import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Import test_setup first to mock pygame before other imports
import test_setup  # This mocks pygame.image.load before other imports

import unittest

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cell import Cell
from clan import Clan
from constants import CELL_ENERGY_MAX, CELL_REPRODUCTION_THRESHOLD, CELL_MIN_AGE_TO_REPRODUCE, INITIAL_REPRODUCTION_TIME


class TestCellReproduction(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.clan = Clan()
        self.cell = Cell(100, 100, self.clan, CELL_ENERGY_MAX)

    def test_reproduction_timer_initially_blocks_reproduction(self):
        """Test that cells cannot reproduce until the initial reproduction timer expires."""
        # Set cell to be ready for reproduction (enough energy and age)
        self.cell.energy = CELL_REPRODUCTION_THRESHOLD
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE

        # Initially, reproduction should return None due to timer
        for _ in range(INITIAL_REPRODUCTION_TIME - 1):
            offspring = self.cell.reproduce()
            self.assertIsNone(offspring, "Cell reproduced before timer expired")

    def test_reproduction_timer_allows_reproduction_after_expiry(self):
        """Test that cells can reproduce once the initial reproduction timer expires."""
        # Set cell to be ready for reproduction
        self.cell.energy = CELL_REPRODUCTION_THRESHOLD
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE

        # Advance the timer to completion
        for _ in range(INITIAL_REPRODUCTION_TIME):
            self.cell.reproduce()

        # Now reproduction should be possible
        offspring = self.cell.reproduce()
        self.assertIsNotNone(offspring, "Cell should be able to reproduce after timer expiry")
        self.assertIsInstance(offspring, Cell, "Offspring should be a Cell instance")

    def test_reproduction_requires_sufficient_energy(self):
        """Test that cells need sufficient energy to reproduce."""
        # Set age to minimum but energy below threshold
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE
        self.cell.energy = CELL_REPRODUCTION_THRESHOLD - 1

        # Advance timer
        for _ in range(INITIAL_REPRODUCTION_TIME):
            self.cell.reproduce()

        # Should not reproduce due to insufficient energy
        offspring = self.cell.reproduce()
        self.assertIsNone(offspring, "Cell should not reproduce with insufficient energy")

    def test_reproduction_requires_minimum_age(self):
        """Test that cells need minimum age to reproduce."""
        # Set energy to sufficient but age below minimum
        self.cell.energy = CELL_REPRODUCTION_THRESHOLD
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE - 1

        # Advance timer
        for _ in range(INITIAL_REPRODUCTION_TIME):
            self.cell.reproduce()

        # Should not reproduce due to insufficient age
        offspring = self.cell.reproduce()
        self.assertIsNone(offspring, "Cell should not reproduce before minimum age")

    def test_successful_reproduction_reduces_parent_energy(self):
        """Test that successful reproduction splits parent energy with offspring."""
        initial_energy = CELL_REPRODUCTION_THRESHOLD + 10  # Extra energy above threshold
        self.cell.energy = initial_energy
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE

        # Advance timer
        for _ in range(INITIAL_REPRODUCTION_TIME):
            self.cell.reproduce()

        expected_energy = initial_energy / 2

        offspring = self.cell.reproduce()
        self.assertIsNotNone(offspring, "Reproduction should succeed")
        self.assertAlmostEqual(self.cell.energy, expected_energy, places=5,
                              msg="Parent energy should be halved after reproduction")

    def test_offspring_inherits_parent_clan(self):
        """Test that offspring belongs to the same clan as parent."""
        self.cell.energy = CELL_REPRODUCTION_THRESHOLD
        self.cell.age = CELL_MIN_AGE_TO_REPRODUCE

        # Advance timer
        for _ in range(INITIAL_REPRODUCTION_TIME):
            self.cell.reproduce()

        offspring = self.cell.reproduce()
        self.assertIsNotNone(offspring, "Reproduction should succeed")
        self.assertEqual(offspring.clan.id, self.cell.clan.id,
                        "Offspring should inherit parent's clan")


if __name__ == '__main__':
    unittest.main()
