import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------
with open("../data/rssiOverDistance.txt", "r") as f:
	#time_noman = []
	rssi_noman = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="ESPap":
			print "kkkkk"
			#time_man.append(int(row[0]))        		
	        	rssi_noman.append(int(row[1]))
		else:
			continue



plt.title('RSSI variation over the distance(20m-100m) ')
count2= range(0, len(rssi_noman))
plt.xlabel('Distance (s)')
plt.ylabel('RSSI (dBm)')
plt.ylim(-100, -50)
#plt.xlim(20, 100)
plt.plot(count2, rssi_noman)
#plt.legend(['No Man in LOS', 'Clear LOS'], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


