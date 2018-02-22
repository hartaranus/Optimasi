import numpy as np
import matplotlib.pyplot as plt

# Import APM Python library
from APMonitor import apm

# Select the server
server = 'http://xps.apmonitor.com'

# Give the application a name
app = 'production'

# Clear any previous applications by that name
apm.apm(server,app,'clear all')

# Load the model file
apm.apm_load(server,app,'softdrink.apm')

# Solve on APM server
solver_output = apm.apm(server,app,'solve')

# Display solver output
print(solver_output)

# Retrieve results
res_dict = apm.apm_sol(server,app)

print(res_dict)

print('')
print('--- Results of the Optimization Problem ---')
print('Spring production (x1): ', res_dict['x1'])
print('Nebsi production  (x2): ', res_dict['x2'])
print('Profit (Swiss Francs) : ', res_dict['profit'])

# Display Results in Web Viewer 
url = apm.apm_web_var(server,app)

# Design variables at mesh points
x = np.arange(-1.0, 8.0, 0.02)
y = np.arange(-1.0, 6.0, 0.02)
x1, x2 = np.meshgrid(x, y)

# Equations and Constraints
profit = 100.0 * x1 + 125.0 * x2
A_usage = 3 * x1 + 6 * x2
B_usage = 8 * x1 + 4 * x2

plt.figure()

# Weight contours
lines = np.linspace(100.0,800.0,8)
CS = plt.contour(x1, x2,profit,lines,colors='g')
plt.clabel(CS, inline=1, fontsize=10)

# A usage < 30
CS = plt.contour(x1, x2,A_usage,colors='r',linewidths=[4.0, 1.0, 0.5])
plt.clabel(CS, inline=1, fontsize=10)

# B usage < 44
CS = plt.contour(x1, x2,B_usage,colors='b',linewidths=[4.0, 1.0, 0.5])
plt.clabel(CS, inline=1, fontsize=10)

# Container for 0 <= Spring <= 500 L
CS = plt.contour(x1, x2,x1 ,[0.0, 0.1, 4.9, 5.0],colors='k',linewidths=[4.0, 1.0, 1.0, 4.0])
plt.clabel(CS, inline=1, fontsize=10)

# Container for 0 <= Nebsi <= 400 L
CS = plt.contour(x1, x2,x2 ,[0.0, 0.1, 3.9, 4.0],colors='k',linewidths=[4.0, 1.0, 1.0, 4.0])
plt.clabel(CS, inline=1, fontsize=10)

# Add some labels
plt.title('Soft Drink Production Problem')
plt.xlabel('Spring Production (100 L)')
plt.ylabel('Nebsi Production (100 L)')

# Save the figure as a PNG
plt.savefig('contour.png')

# Show the plots
plt.show()
