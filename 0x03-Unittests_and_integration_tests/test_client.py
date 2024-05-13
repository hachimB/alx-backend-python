#!/usr/bin/env python3
"""test for client.py"""
from client import GithubOrgClient
from parameterized import parameterized
from typing import (
    List,
    Dict,
)
from utils import (
    get_json,
    access_nested_map,
    memoize,
)
import unittest
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch.object(GithubOrgClient, 'org', return_value={})
    def test_org(self,
                 org_name: str,
                 mock_org: Mock) -> None:
        """test_org method"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """test_public_repos_url"""
        mock_playload = {"payload_key": "payload_value"}
        with patch.object(GithubOrgClient, "org",
                          return_value=mock_playload) as mock_org:
            test_client = GithubOrgClient("mock_org")
            response = test_client.org()
            self.assertEqual(response, mock_playload)
            mock_org.assert_called_once()
