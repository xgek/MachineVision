# test_machinevision.py
"""
Tests for MachineVision module.
"""

import unittest
from machinevision import MachineVision

class TestMachineVision(unittest.TestCase):
    """Test cases for MachineVision class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MachineVision()
        self.assertIsInstance(instance, MachineVision)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MachineVision()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
