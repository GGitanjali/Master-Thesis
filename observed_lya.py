import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d 
import csv



file = "files/taudamp_z008.00_nf0.62378_1000_300Mpc_master_bubnoadded.csv"
df = pd.read_csv("files/taudamp_z008.00_nf0.62378_1000_300Mpc_master_bubnoadded.csv")  

muv_array = df["Muv"].to_numpy()



def velocity_offset(Muv, z):
    gamma = -0.3 if Muv >= (-20.0 - 0.26 * z) else -0.7
    delta_v = 10**(0.32 * gamma * (Muv + 20.0 + 0.26 * z) + 2.34)
    return delta_v


delta_v_array = np.array([velocity_offset(muv, 2) for muv in muv_array])


file_path = 'files/output'

def gaussian(velocity, delta_v, sigma, amplitude=1):
    return amplitude * np.exp(-0.5 * ((velocity - delta_v) / sigma) ** 2)

def two_gaussians_with_asymmetry(velocity, v_offset, sigma, l_red_l_total):
    l_red = l_red_l_total
    l_blue = 1 - l_red
    gaussian_blue = gaussian(velocity, -v_offset / 2, sigma, amplitude=l_blue)
    gaussian_red = gaussian(velocity, v_offset / 2, sigma, amplitude=l_red)
    return gaussian_blue + gaussian_red


def plot_transmission_curves(row_number, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines[2:]: 
            columns = list(map(float, line.strip().split()[:5]))  
            matrix.append(columns)
        
        row1 = list(map(float, lines[0].strip().split()[5:])) 
        row = list(map(float, lines[row_number+2].strip().split()[5:]))   ## Adding 2 because data starts from 2 not 0, iteration problem in the next step

    velocity_offsets = np.array(row1[::2]) 
    transmission = np.exp(-np.array(row))
    return velocity_offsets, transmission

def combined_plot(T, I):
    return T * I


observed_gaussians = []
transmission_curves = []
gaussians = []
valid_indices = []


for i in range(len(delta_v_array)): 
    velocity_offsets, T = plot_transmission_curves(i, 'files/output')
    if len(T) == 0:
        print(f"Skipping row {i} due to empty transmission curve.")
        continue


velocity_common = np.linspace(-1000, 3000, len(T))

while True:
    try:
        velocity_offsets, T = plot_transmission_curves(i, 'files/output')
        if len(T) == 0:
            print(f"Skipping row {i} due to empty transmission curve.")
        i += 1
    except ValueError:  # Replace with the actual exception, like FileNotFoundError
        print("No more data to process.")
        break

i = 0
while True:
    try:
        velocity_offsets, T = plot_transmission_curves(i, 'files/output')
        
        if len(T) == 0:
            print(f"Skipping row {i} due to empty transmission curve.")
        else:
            print(i)
            transmission_curves.append(T)
            I = two_gaussians_with_asymmetry(velocity_common, delta_v_array[i], sigma=50, l_red_l_total=0.6)
            gaussians.append(I)
            valid_indices.append(i)

        i += 1  # Move to the next row

    except IndexError:  # Stops when data runs out
        print("No more data to process.")
        break

print("Saving done yayy")






for idx, i in enumerate(valid_indices):
    T = transmission_curves[idx]
    I = gaussians[idx]

    TI = combined_plot(T, I)

    integral_TI = np.trapz(TI, velocity_common)
    integral_I = np.trapz(I, velocity_common)

    observed_gaussian_value = integral_TI / integral_I
    observed_gaussians.append(observed_gaussian_value)
    print(f"Done with index {i}")

observed_gaussians = np.array(observed_gaussians)
np.savetxt('observed_gaussians.csv', observed_gaussians, delimiter=',')

print("Observed Gaussians saved to 'observed_gaussians.csv'.")

    