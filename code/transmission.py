import numpy as np
import matplotlib.pyplot as plt


file_path = 'D:/Thesis/21cmFAST-master/Output/Tot_Tau_lists/output'

def transmission_curves(row_number, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines[2:]:
            columns = list(map(float, line.strip().split()[:5]))
            matrix.append(columns)

        row1 = list(map(float, lines[0].strip().split()[5:]))
        row = list(map(float, lines[row_number+2].strip().split()[5:]))# starting with 3 row

    velocity_offsets = np.array(row1[::2])
    transmission = np.exp(-np.array(row))
    return velocity_offsets, transmission

