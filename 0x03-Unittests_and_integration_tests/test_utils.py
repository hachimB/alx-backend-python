#!/usr/bin/env python3
"""Python Unittests"""
from parameterized import parameterized
from utils import access_nested_map
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any) -> Any:
        """Test for access_nested_map method from utils"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
