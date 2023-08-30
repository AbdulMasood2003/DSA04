import matplotlib.pyplot as plt
months=['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
temp=[20,21,22,23,30,40,60,70,90,75,85,55]
plt.plot(months,temp,marker='o')
plt.xlabel('Months')
plt.ylabel('Data in (mm)')
plt.title('Monthly Rainfall Data')
plt.grid(True)
plt.show()
print()
plt.scatter(months,temp)
plt.xlabel('Months')
plt.ylabel('Data in (mm)')
plt.title('Monthly Rainfall Data')
plt.grid(True)
plt.show()
