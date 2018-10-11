import pylab
import pandas as pd
import csv

df = pd.read_csv("E:\\Machine_Learns_Logistic_Reg\\data\\train.csv")
data = df.values.T.tolist()

#print(data)
#cln_data= df[np.isfinite(data[3])]

# if (data[4]/data[3]) > 2:
	# plt.plot(data[3], data[4], 'ro')
# else:
pylab.scatter(data[0], data[1], c=data[2], cmap=pylab.cm.cool)

plt.xlabel('Lot Frontage')
plt.ylabel('Lot Area')

pylab.show()