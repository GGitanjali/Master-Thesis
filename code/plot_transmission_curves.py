import numpy as np
import matplotlib.pyplot as plt

file_path = 'D:/Thesis/21cmFAST-master/Output/Tot_Tau_lists/output'

def plot_t_curves(row_number, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines[2:]:
            columns = list(map(float, line.strip().split()[:5]))
            matrix.append(columns)

        row1 = list(map(float, lines[0].strip().split()[5:]))
        row = list(map(float, lines[row_number+2].strip().split()[5:]))  # starting with 3rd row

    velocity_offsets = np.array(row1[::2])
    transmission = np.exp(-np.array(row))
    
    plt.figure(figsize=(8, 5))
    plt.plot(velocity_offsets, transmission, label=f'Row {row_number}')
    plt.xlabel('Velocity Offset')
    plt.ylabel('Transmission')
    plt.title('Transmission Curve')
    plt.legend()
    plt.grid()
    plt.show()

row_num = int(input('Enter row number : '))
plot_t_curves(row_num, file_path)
