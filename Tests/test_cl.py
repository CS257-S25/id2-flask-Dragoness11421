"""Test for functions in both production codes and command line tool."""

import unittest
import sys
from unittest.mock import patch, mock_open
from io import StringIO
from ProductionCode.processor import (
    display_results, filter_by_shape, get_sightings_by_shape
)
class TestProcessorMethods(unittest.TestCase):
    """Unit tests for functions in ProductionCode and CLI."""
    def setUp(self):
        """Redirect stdout and prepare sample UFO data for testing."""
        self.sample_data = [
            {'datetime': '10/10/1949 20:30', 'city': 'san marcos', 'shape': 'cylinder'},
            {'datetime': '10/10/1949 21:00', 'city': 'lackland afb', 'shape': 'light'},
            {'datetime': '10/10/1956 21:00', 'city': 'edna', 'shape': 'cylinder'}
        ]
        self._stdout = sys.stdout
        self.held_output = StringIO()
        sys.stdout = self.held_output
    def tearDown(self):
        """Restore original stdout."""
        sys.stdout = self._stdout
    def test_display_results(self):
        """Test that display_results prints each row in the data."""
        display_results(self.sample_data)
        self.assertIn('san marcos', self.sample_data)
        self.assertIn('lackland afb', self.sample_data)
        self.assertIn('edna', self.sample_data)
        self.assertEqual(self.sample_data, list)
    def test_filter_by_shape(self):
        """Test filtering sightings by shape returns matching entries."""
        result_cylinder = filter_by_shape(self.sample_data, "cylinder")
        self.assertEqual(len(result_cylinder), 2)
        self.assertSetEqual({row['city'] for row in result_cylinder}, {'san marcos', 'edna'})

        result_light = filter_by_shape(self.sample_data, "light")
        self.assertEqual(len(result_light), 1)
        self.assertEqual(result_light[0]['city'], 'lackland afb')

        result_empty = filter_by_shape(self.sample_data, "disk")
        self.assertEqual(len(result_empty), 0)
    @patch("builtins.open", new_callable=mock_open, read_data=
           "datetime,city,state,shape,duration,comments\n"
           "10/10/1949 20:30,san marcos,tx,cylinder,5 mins,\"desc\"\n"
           "10/10/1956 21:00,edna,tx,cylinder,5 mins,\"desc\"\n")
    def test_get_sightings_by_shape(self):
        """Test wrapper that loads data and filters by shape correctly."""
        result = get_sightings_by_shape("cylinder")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["shape"], "cylinder")
if __name__ == '__main__':
    unittest.main()
