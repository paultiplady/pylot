import vcr
from pylot import commands

TEST_MODULE = 'tests.fixtures.sample_app'
DEFAULTED_TEST_MODULE = 'tests.fixtures.all_default_app'


# Enable the capsys py.test fixture, to capture stdout/stderr.
def test_deploy_dry_run(capsys):
    """Test that a deploy dry-run outputs the config and spec to stdout."""
    commands.deploy(module_=DEFAULTED_TEST_MODULE, dry_run=True)

    stdout, stderr = capsys.readouterr()
    assert 'FOO' in stdout
    assert 'BAR' in stdout
    assert not stderr


@vcr.use_cassette('tests/fixtures/test_deploy.yml', record_mode='none')
def test_deploy():
    """Test that the deploy command successfully creates k8s API resources."""
    commands.deploy(module_=DEFAULTED_TEST_MODULE)
