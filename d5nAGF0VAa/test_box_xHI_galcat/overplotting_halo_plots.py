import matplotlib as mpl
from matplotlib import colors

df = pd.read_csv(masfilname)
data = df.iloc[:, 1:4]  


x = data.iloc[:, 0] 
y = data.iloc[:, 1] 
z = data.iloc[:, 2]

mask = 300*z <= 1.5
x_filtered = x[mask]
y_filtered = y[mask]
extent = [0, size, 0, size]  
aspect = (extent[1] - extent[0]) / (extent[3] - extent[2]) 
# Create 2D histogram with a logarithmic color scale
plt.imshow(np.rot90(xHIcube[:,:,i_zslice]),extent=extent,aspect=aspect, cmap = "Blues")
plt.scatter(300*x_filtered, 300*y_filtered, s = 10, alpha=0.6, c = "Red")


plt.xlabel('X-axis (Column 1)')
plt.ylabel('Y-axis (Column 2)')
plt.title('Overplotted Halo posiitons')
plt.xlim([0,300])
plt.ylim([0,300])

# Show the plot
plt.show()