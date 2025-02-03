import numpy as np
import matplotlib.pyplot as plt

def gaussian(velocity, delta_v, sigma, amplitude=1):
    return amplitude * np.exp(-0.5 * ((velocity - delta_v) / sigma)**2)

def instrinsic_gaussians(velocity, v_separation, sigma, l_red_l_total):
    l_red = l_red_l_total
    l_blue = 1 - l_red

    # First Gaussian (blueshifted)
    gaussian_blue = gaussian(velocity, -v_separation / 2, sigma, amplitude=l_blue)

    # Second Gaussian (redshifted)
    gaussian_red = gaussian(velocity, v_separation / 2, sigma, amplitude=l_red)

    # Combining them
    combined_profile = gaussian_blue + gaussian_red
    return velocity, combined_profile


