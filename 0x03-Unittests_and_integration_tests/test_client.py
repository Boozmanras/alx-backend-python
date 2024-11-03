#!/usr/bin/env python3
"""Unit and integration tests for client module."""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for client.GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value."""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url property."""
        expected_payload = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        with patch('client.GithubOrgClient.org',
                  new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_payload
            test_client = GithubOrgClient("test-org")
            self.assertEqual(
                test_client._public_repos_url,
                expected_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                  new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://test.url"
            test_client = GithubOrgClient("test-org")

            self.assertEqual(
                test_client.public_repos(),
                ["repo1", "repo2"])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://test.url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Unit-test GithubOrgClient.has_license."""
        test_client = GithubOrgClient("test-org")
        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures before running tests."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mock get."""
            mock_response = Mock()

            if url.endswith("/orgs/test-org"):
                payload = cls.org_payload
            elif url.endswith("/repos"):
                payload = cls.repos_payload
            else:
                payload = {}

            mock_response.json.return_value = payload
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class fixtures after running tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test: public repos"""
        test_client = GithubOrgClient("test-org")
        self.assertEqual(test_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test: public repos with License"""
        test_client = GithubOrgClient("test-org")
        self.assertEqual(
            test_client.public_repos(license="apache-2.0"),
            self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
