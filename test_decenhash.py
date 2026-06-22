# test_decenhash.py
"""
Tests for DecenHash module.
"""

import unittest
from decenhash import DecenHash

class TestDecenHash(unittest.TestCase):
    """Test cases for DecenHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecenHash()
        self.assertIsInstance(instance, DecenHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecenHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
