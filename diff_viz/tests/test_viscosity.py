import hypothesis.strategies as st
from hypothesis.extra.pandas import columns, column, data_frames, range_indexes
import numpy as np
from hypothesis import given, settings
import pandas as pd
import math

# import diff_viz.tests.hypothesis_util_functions as hf

# Import the function you want to test
from diff_viz.viscosity import viscosity_from_diffusion_coefficient

# Define a strategy for generating valid input values
# dataframe_strategy = hf.hypothesis_features_dataframe(include_target_col=False)
temperature_strategy = st.floats(min_value=0.1, max_value=1000)
particle_radius_strategy = st.floats(min_value=0.1, max_value=1000)

float_with_nan_st = st.floats(allow_nan=True, allow_infinity=False)
int_st = st.integers(min_value=0, max_value=1000)


# Define the hypothesis test
@given(
    diffusion_coefficient=st.floats(
        min_value=0.1, max_value=100.0, allow_infinity=False
    ),
    temperature=temperature_strategy,
    particle_radius=particle_radius_strategy,
)
@settings(max_examples=10)
def test_viscosity_from_diffusion_coefficient(
    diffusion_coefficient, temperature, particle_radius
):
    # Calculate viscosity using the function
    test_dataframe = pd.DataFrame({"Deff1": [diffusion_coefficient]})
    viscosity_series = viscosity_from_diffusion_coefficient(
        test_dataframe, "Deff1", temperature, particle_radius
    )

    # Check if the length of the resulting Series matches the length of the input DataFrame
    assert len(viscosity_series) == len(test_dataframe)

    # Properties to check for each row
    for index, row in test_dataframe.iterrows():
        diffusion_coefficient = row["Deff1"]
        # temperature = row['Temperature']
        # particle_radius = row['Particle Radius']

        expected_viscosity = (1.380649e-23 * temperature) / (
            6 * math.pi * diffusion_coefficient * particle_radius
        )

        # Check if calculated viscosity is close to expected viscosity for each row
        assert math.isclose(viscosity_series[index], expected_viscosity, rel_tol=1e-6)
