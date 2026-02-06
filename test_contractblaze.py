# test_contractblaze.py
"""
Tests for contractBlaze module.
"""

import unittest
from contractblaze import contractBlaze

class TestcontractBlaze(unittest.TestCase):
    """Test cases for contractBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = contractBlaze()
        self.assertIsInstance(instance, contractBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = contractBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
