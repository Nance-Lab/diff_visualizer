from diff_viz.utils import *
import pytest

class TestGetExperiment:
  """
    Test class for the get_experiment function.

    This class contains tests for the get_experiment function, which generates a string
    representing the title of a Traj csv folder based on input parameters.

    Assumptions:
    - The input date, donor, DIV, stimulus, and level parameters are all strings.
    - The input parameters do not contain any invalid characters for folder naming conventions.

    Dependencies:
    - The get_experiment function must be defined in the same module as this class.

    Limitations:
    - This class only tests a limited range of input parameter values.
    - Additional tests may be needed to ensure full coverage of the get_experiment function.

    Usage:
    - Create an instance of the TestGetExperiment class to run the tests.
    - Call the pytest.main() method to run the tests using the pytest framework.
    """
  
    def test_get_experiment(self):
        date = "2023-04-26"
        donor = "John"
        DIV = "2"
        stimulus = "light"
        level = "high"

        result = get_experiment(date, donor, DIV, stimulus, level)
        expected = "2023-04-26_John_2_light_high"

        assert result == expected

    def test_long_input(self):
        date = "2023-04-26" * 1000
        donor = "John"
        DIV = "2"
        stimulus = "light"
        level = "high"

        result = get_experiment(date, donor, DIV, stimulus, level)
        expected = date + '_John_2_light_high'

        assert result == expected

if __name__ == '__main__':
    pytest.main()

