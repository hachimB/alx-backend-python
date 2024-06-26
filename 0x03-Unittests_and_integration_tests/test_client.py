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
from unittest.mock import Mock, patch, PropertyMock


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

    payload = [{"name": "repo1"}, {"name": "repo2"}]

    @patch("client.get_json", return_value=payload)
    def test_public_repos(self, mock_get_json):
        """test_public_repos"""
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="http://example.com"
                          ) as mock_property:
            test_client = GithubOrgClient("mock_org")
            response = test_client.public_repos()
            self.assertEqual(response, ["repo1", "repo2"])
            mock_property.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "other_license"),
    ])
    def test_has_license(self, repo, license_key):
        """test_has_licence"""
        self.assertEqual(repo['license']['key'], license_key)
