"""Test that the __main__ CLI entrypoint connects to the command implementations."""
import sys
from unittest.mock import patch

from pylot.__main__ import main

TEST_MODULE = 'tests.fixtures.sample_app'
DEFAULTED_TEST_MODULE = 'tests.fixtures.all_default_app'


@patch('pylot.__main__.commands')
def test_main_deploy(m_commands):
    """Test that a dry-run deploy outputs the correct Spec."""
    sys.argv = ['pylot', 'deploy', TEST_MODULE, '--dry-run']
    main()
    assert m_commands.deploy.called


def test_main_deploy_error_message(capsys):
    """Test that the deploy command renders error messages nicely."""
    sys.argv = ['pylot', 'deploy', TEST_MODULE, '--dry-run']
    main()

    stdout, stderr = capsys.readouterr()
    assert stderr == 'ERROR: Configuration field "bar" was not provided in values, and there is no default value.\n'


@patch('pylot.__main__.commands')
def test_main_dump(m_commands):
    """Test that the `dump` debug command is triggered correctly."""
    sys.argv = ['pylot', 'dump', 'tests.fixtures.sample_app']
    main()
    assert m_commands.dump.called
