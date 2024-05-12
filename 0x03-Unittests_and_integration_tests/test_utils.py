#!/usr/bin/env python3
"""Python Unittests"""
from parameterized import parameterized
from utils import access_nested_map, get_json
import unittest
from unittest.mock import Mock
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Type
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Type[BaseException]):
        """Test for access_nested_map method from utils"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """TestGetJson"""
    @parameterized.expand([
         ("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False}),
    ])
    @unittest.mock.patch('requests.get')
    def test_get_json(
            self,
            test_payload: Dict[str, Any],
            test_url: str,
            mock_get: Mock) -> Mock:
        """Test for get_json method"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)
