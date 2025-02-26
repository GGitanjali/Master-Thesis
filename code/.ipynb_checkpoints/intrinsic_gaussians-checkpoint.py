import numpy as np
import matplotlib.pyplot as plt

def gaussian(velocity, delta_v, sigma, amplitude=1):
    return amplitude * np.exp(-0.5 * ((velocity - delta_v) / sigma)**2)

def two_gaussians_with_asymmetry(velocity, v_offset, sigma, l_red_l_total):
    l_red = l_red_l_total
    l_blue = 1 - l_red
    gaussian_blue = gaussian(velocity, -v_offset / 2, sigma, amplitude=l_blue)
    gaussian_red = gaussian(velocity, v_offset / 2, sigma, amplitude=l_red)
    return gaussian_blue + gaussian_red

