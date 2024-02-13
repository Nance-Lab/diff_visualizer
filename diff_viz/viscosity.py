# Assisted by chatGPT

import pandas as pd
import math

def viscosity_from_diffusion_coefficient(dataframe, diffusion_coefficient_column, temperature, particle_radius):
    """
    Calculate viscosity of a fluid using the Stokes-Einstein equation.

    Parameters:
        dataframe (pandas.DataFrame): DataFrame containing diffusion coefficients.
        diffusion_coefficient_column (str): Name of the column containing diffusion coefficients.
        temperature (float): Temperature in Kelvin.
        particle_radius (float): Radius of the particles in meters.

    Returns:
        pandas.Series: Series containing viscosity values for each diffusion coefficient.
    Raises:
        ValueError: If any input is non-positive.


        # Example usage
        data = {'Diffusion Coefficient (m^2/s)': [1.5e-9, 2.0e-9, 1.8e-9]}
        df = pd.DataFrame(data)
        temperature = 298.15  # Temperature in Kelvin
        particle_radius = 1e-9  # Particle radius in meters

        viscosity_series = viscosity_from_diffusion_coefficient(df, 'Diffusion Coefficient (m^2/s)', temperature, particle_radius)
        print(viscosity_series)
    """
    # Validate inputs
    if (dataframe[diffusion_coefficient_column] <= 0).any():
        raise ValueError("Diffusion coefficient must be positive.")
    if temperature <= 0:
        raise ValueError("Temperature must be positive.")
    if particle_radius <= 0:
        raise ValueError("Particle radius must be positive.")

    # Boltzmann constant
    k_b = 1.380649e-23  # m^2 kg / (s^2 K)

    def calculate_viscosity(diffusion_coefficient):
        # Calculate viscosity using Stokes-Einstein equation
        return (k_b * temperature) / (6 * math.pi * diffusion_coefficient * particle_radius)

    # Apply the function to the specified column
    if diffusion_coefficient_column not in dataframe.columns:
        raise ValueError("Diffusion coefficient column not found in DataFrame.")
    else:
        viscosity_series = dataframe[diffusion_coefficient_column].apply(calculate_viscosity)

    return viscosity_series

