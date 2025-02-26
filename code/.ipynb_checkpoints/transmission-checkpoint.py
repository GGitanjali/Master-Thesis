import numpy as np
import matplotlib.pyplot as plt


file_path = 'D:/Thesis/21cmFAST-master/Output/Tot_Tau_lists/output'


with open(file_path, 'r') as file:
    lines = file.readlines()    
    matrix = []
    for line in lines[2:]: 
        columns = list(map(float, line.strip().split()[:5]))  
        matrix.append(columns)

matrix = np.array(matrix)


def plot_transmission_curves(row_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        row1 = list(map(float, lines[0].strip().split()[5:])) #this is special for the first row(x-axis)
        row = list(map(float, lines[row_number].strip().split()[5:]))
    
    
    x_values_1 = np.array(row1[::2])  #this is special for the first row
    y_values = np.exp(-np.array(row)) #transmission
    
    
    return x_values_1, y_values
