import numpy as np
import matplotlib.pyplot as plt 

#-------------------------------------------------------------------------------
with open("../data/5mWithTr.txt", "r") as f:

	rssi_manT = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="ESPap":
			print "hhhhhhhhh"
			#time_man.append(int(row[0]))        		
	        	rssi_manT.append(int(row[1]))
		else:
			continue


#-------------------------------------------------------------------------------
with open("../data/5mWith.txt", "r") as f:
	#time_noman = []
	rssi_man = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="ESPap":
			print "kkkkk"
			#time_man.append(int(row[0]))        		
	        	rssi_man.append(int(row[1]))
		else:
			continue

#-------------------------------------------------------------------------------
with open("../data/5mWithRc.txt", "r") as f:

	rssi_manR = []
	for line in f:
		row = line.split(',')
		print len(row[0]);
		#if "3Com" in row[0]:
		if row[0]=="ESPap":
			print "mmmmmm"
			#time_man.append(int(row[0]))        		
	        	rssi_manR.append(int(row[1]))
		else:
			continue


#rssi_man = [3,4,5,6,8]
count= range(0, len(rssi_manT))
count2= range(0, len(rssi_man))
count3= range(0, len(rssi_manR))
#print count
#print rssi_man
	#x = np.array([])

plt.title('RSSI variation over position (5m) ')
plt.xlabel('Time(s)')
plt.ylabel('RSSI (dBm)')
plt.ylim(-100, -20)
plt.plot(count, rssi_manT)
plt.plot(count2, rssi_man)
plt.plot(count3, rssi_manR)
plt.legend(['NearTransmitter', 'Middle', 'NearReceiver' ], loc='upper left')
plt.show()
#plt.savefig("text.png", dpi=300)


