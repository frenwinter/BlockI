# test_blockid.py
"""
Tests for BlockID module.
"""

import unittest
from blockid import BlockID

class TestBlockID(unittest.TestCase):
    """Test cases for BlockID class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockID()
        self.assertIsInstance(instance, BlockID)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockID()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
