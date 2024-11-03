# alx-backend-python

## Project: 0x03 - Unittests and Integration Tests

This project focuses on writing unit and integration tests for Python functions and classes. It emphasizes parameterization, mocking, and patching to ensure each function behaves as expected under various conditions without relying on external resources.

### Requirements

- **Environment**: Code will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- **File Standards**:
  - All files must end with a new line.
  - The first line in each file should be `#!/usr/bin/env python3`.
  - Files must be executable.
- **Coding Style**: Follow the `pycodestyle` (version 2.5) style guide.
- **Documentation**:
  - Each module, class, and function must be documented with a descriptive sentence explaining its purpose.
  - Use type annotations for all functions and coroutines.
- **Project Files**:
  - `utils.py`: Contains utility functions to test.
  - `client.py`: Contains client functions for interacting with external services.
  - `fixtures.py`: Contains data fixtures for integration tests.

### Tasks

1. **Parameterize Unit Test**: Test `utils.access_nested_map` using various nested map inputs.
2. **Exception Handling in Tests**: Ensure `access_nested_map` raises the correct `KeyError` with expected messages for missing keys.
3. **Mock HTTP Calls**: Test `utils.get_json` function with `requests.get` mocked to avoid real HTTP calls.
4. **Memoization Test**: Implement `TestMemoize` to verify caching behavior of `@memoize` decorator.
5. **Mock Property Access**: Test `GithubOrgClient._public_repos_url` by mocking `org` property.
6. **Extended Patching**: Test `GithubOrgClient.public_repos` with mocked dependencies to validate repository list retrieval.
7. **License Check Parameterization**: Verify `GithubOrgClient.has_license` functionality for different license types.
8. **Integration Test with Fixtures**: Test `GithubOrgClient.public_repos` with integration fixtures, ensuring setup and teardown for external request mocks.
9. **Advanced Integration Tests**: Perform in-depth testing on `public_repos` with license filters, ensuring results match fixture expectations.

### Repository Structure

- **GitHub Repository**: `alx-backend-python`
- **Project Directory**: `0x03-Unittests_and_integration_tests`
- **Test Files**:
  - `test_utils.py`: Contains tests for utility functions.
  - `test_client.py`: Contains tests for client functions.

### Usage

Run tests with:
```bash
python3 -m unittest discover -s tests

### Author

Victor paul

### License

Part of ALX se specialisation
