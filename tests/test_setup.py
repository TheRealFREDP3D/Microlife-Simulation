"""
Test setup module to handle asset loading issues in tests.
"""
import sys
import os
from unittest.mock import patch

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Mock pygame.image.load to avoid asset loading issues in tests
def mock_image_load(path):
    """Mock pygame.image.load to return a dummy surface."""
    import pygame
    # Create a small dummy surface
    return pygame.Surface((32, 32))

# Apply the mock before importing any modules that use assets
with patch('pygame.image.load', side_effect=mock_image_load):
    # Now import the modules that would normally load assets
    from cell import Cell
    from clan import Clan
    from environment import Environment
    from food import Food
