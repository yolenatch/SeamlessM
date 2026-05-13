# test_seamlessm4t.py
"""
Tests for SeamlessM4T module.
"""

import unittest
from seamlessm4t import SeamlessM4T

class TestSeamlessM4T(unittest.TestCase):
    """Test cases for SeamlessM4T class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SeamlessM4T()
        self.assertIsInstance(instance, SeamlessM4T)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SeamlessM4T()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
