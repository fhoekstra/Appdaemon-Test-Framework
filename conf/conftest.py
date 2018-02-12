import pytest
from appdaemon_test_framework.assert_that import AssertThatWrapper
from appdaemon_test_framework.given import GivenWrapper
from appdaemon_test_framework.setup_hass import patch_hass


@pytest.fixture
def hass_functions(request):
    patched_hass_functions, unpatch_callback = patch_hass()
    request.addfinalizer(unpatch_callback)
    return patched_hass_functions


@pytest.fixture
def given(hass_functions):
    return GivenWrapper(hass_functions)


@pytest.fixture
def assert_that(hass_functions):
    return lambda thing_to_check: AssertThatWrapper(thing_to_check, hass_functions)
