# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
# This takes one parameter that is forwarded from the test
@pytest.fixture
def element_list(num_elements):
    return list(range(num_elements))
