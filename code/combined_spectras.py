import matplotlib.pyplot as plt
import numpy as np
from intrinsic_gaussians import instrinsic_gaussians
from transmission import plot_transmission_curves



def combined_plot():
    # Transmission curve
    row_number = int(input("Enter Row Number : "))# Example row number; change as needed
    x_transmission, y_transmission = plot_transmission_curves(row_number)

    v_separation = float(input("Velocity separation (v_separation): "))
    sigma = float(input("Sigma (width): "))
    asymmetry = float(input("Asymmetry (0 to 1): "))
    velocity_min = float(input("Minimum velocity for plot range: ")) ## have to put (-200, 200) otherwise the dimensions are not same
    velocity_max = float(input("Maximum velocity for plot range: "))
    num_points_velocity = int(input("Number of points to compute in the range: "))

    # Generate velocity range
    #velocity =  np.linspace(-500, 500, 1000)
    x_gaussian, y_gaussian = instrinsic_gaussians(velocity, v_separation, sigma, asymmetry)

    # Multiply the curves
    y_combined = y_transmission * y_gaussian

    # Plot all curves
    plt.figure(figsize=(10, 6))
    plt.plot(x_transmission, y_transmission, label="Transmission Curves", color="blue")
    plt.plot(x_gaussian, y_gaussian, label="Intrinsic Gaussians", color="green")
    plt.plot(x_transmission, y_combined, label="Combined Curve", color="red", linestyle="--")
    plt.xlabel("Velocity")
    plt.ylabel("Intensity")
    plt.title("Combined Plot of Transmission Curves and Intrinsic Gaussians")
    plt.legend()
    plt.grid()
    plt.show()
