import pandas as pd
import matplotlib.pylab as plt

def load_xHI_cube(xHI_cube_file):
    # Get box dimensions (pixels) and size (cMpc)
    DIM  = int(xHI_cube_file.split(‘Mpc’)[0].split(‘_’)[-2])
    size = int(xHI_cube_file.split(‘Mpc’)[0].split(‘_’)[-1])
    #print(DIM, size)

    # Reshape cube (is 1D array --> make it 3D)
    xHI_cube = load_binary_data(xHI_cube_file)

    xHI_cube.shape = (DIM, DIM, DIM)
    xHI_cube = xHI_cube.reshape((DIM, DIM, DIM), order=‘F’)
    return xHI_cube, DIM, size

# read xHI cube
xHIboxfilname=‘xH_nohalos_z008.00_nf0.623784_eff1359.2_effPLindex0_HIIfilter1_Mmin1.0e+11_RHIImax50_200_300Mpc’
xHIcube, DIM, size =load_xHI_cube(xHIboxdir+xHIboxfilname)

# read galaxy catalog
masfilname=‘taudamp_z008.00_nf0.62378_1000_300Mpc_master_bubnoadded.csv’
galcat = pd.read_csv(mascatdir+masfilname)

# plot a slice of the xHIcube
i_zslice= int(input("Enter slice number : "))
extent=[0,size,0,size]
aspect =(extent[1]-extent[0])/(extent[3]-extent[2])
plt.imshow(np.rot90(xHIcube[:,:,i_zslice]),extent=extent,aspect=aspect)
