import pytest
from pylot import loader
from pylot.loader import LoaderError
from tests.fixtures.sample_app import SampleAppConfiguration, pod


def test_loader_single_module():
    """Test that the file loader will correctly a Configuration and Pod spec."""
    specs, configuration_cls = loader.import_('tests.fixtures.sample_app')

    assert configuration_cls is SampleAppConfiguration
    assert specs == [pod]


def test_loader_rejects_multiple_configurations():
    """Test that the file loader will raise an error if there are multiple Configurations."""
    with pytest.raises(LoaderError):
        loader.import_('tests.fixtures.double_config_app')
