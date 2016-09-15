import numpy as np
import matplotlib.pyplot as plt 

'''
A sample text file would contain,

Node A,-81,07-09-2016 12:37:13:PM
Node B,-65,07-09-2016 12:37:13:PM

etc.
'''

#-------------------------------------------------------------------------------
with open("Node5 - Grand1/Left_Above_node5.txt", "r") as f:

	rssi_man = []
	for line in f:
		row = line.split(',')
		if row[0]=="Node B":       		
	        	rssi_man.append(int(row[1]))
		else:
			continue


#-------------------------------------------------------------------------------
with open("Node5 - Grand1/Cali_node5.txt", "r") as f:
	
	rssi_noman = []
	for line in f:
		row = line.split(',')
		if row[0]=="Node B":
	        	rssi_noman.append(int(row[1]))
		else:

			continue

#-------------------------------------------------------------------------------
with open("Node5 - Grand1/Left_Below_node5_part1.txt", "r") as f:

	rssi_left_below = []
	for line in f:
		row = line.split(',')
		if row[0]=="Node B":
	        	rssi_left_below.append(int(row[1]))
		else:
			continue


#-------------------------------------------------------------------------------
with open("Node5 - Grand1/Right_Below_node5.txt", "r") as f:

	rssi_right_below = []
	for line in f:
		row = line.split(',')
		if row[0]=="Node B":
	        	rssi_right_below.append(int(row[1]))
		else:
			continue


count= range(0, len(rssi_man))
count2= range(0, len(rssi_noman))
count3= range(0, len(rssi_left_below))
count4= range(0, len(rssi_right_below))


arr = np.array([rssi_man])
mean= np.mean(arr, axis=None)
stdD= np.std(arr, axis=None)

SNR= mean/stdD

print "mean:",mean
print "SNR:",SNR


plt.title('RSSI variation 4m grid Node 5B')
plt.xlabel('Count')
plt.ylabel('RSSI (dBm)')
plt.ylim(-90, -30)
plt.plot(count, rssi_man)
plt.plot(count2, rssi_noman)
plt.plot(count3, rssi_left_below)
plt.plot(count4, rssi_right_below)
plt.legend(['Left Above', 'Clear LOS', 'Left Below', 'Right Below'], loc='upper left')
plt.show()

