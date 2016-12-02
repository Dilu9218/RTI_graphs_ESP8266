import numpy as np
import matplotlib.pyplot as plt 
import csv


dataB = []
dataC = []
dataD = []
dataE = []
dataF = []
dataG = []
dataH = []
dataI = []
dataJ = []
dataK = []
dataL = []

#-------------------------------------------------------------------------------
with open("A.txt", "r") as f:
	for line in f:
		for i in range(0,len(line)):	
			if line[i]=="B":
				dataB.append(-int(line[i+2:i+4]))
				avg=sum(dataB)/len(dataB)
 
			if line[i]=="C":
				dataC.append(-int(line[i+2:i+4]))
				avg=sum(dataC)/len(dataC) 
			
			if line[i]=="D":
				dataD.append(-int(line[i+2:i+4]))
				avg=sum(dataD)/len(dataD) 

			if line[i]=="E":
				dataE.append(-int(line[i+2:i+4]))
				avg=sum(dataE)/len(dataE)
			
			if line[i]=="F":
				dataF.append(-int(line[i+2:i+4]))
				avg=sum(dataF)/len(dataF)

			if line[i]=="G":
				dataG.append(-int(line[i+2:i+4]))
				avg=sum(dataG)/len(dataG)
			
			if line[i]=="H":
				dataH.append(-int(line[i+2:i+4]))
				avg=sum(dataH)/len(dataH)    
			
			if line[i]=="I":
				dataI.append(-int(line[i+2:i+4]))
				avg=sum(dataI)/len(dataI)

			if line[i]=="J":
				dataJ.append(-int(line[i+2:i+4]))
				avg=sum(dataJ)/len(dataJ)  
       	
			if line[i]=="K":
				dataK.append(-int(line[i+2:i+4]))
				avg=sum(dataK)/len(dataK)  
	
			if line[i]=="L":
				dataL.append(-int(line[i+2:i+4]))
				avg=sum(dataL)/len(dataL)  
			else:
				continue

avgNodeA=[]
avgNodeA.append(-45)
avgB=sum(dataB)/len(dataB)
avgNodeA.append(avgB)
avgC=sum(dataC)/len(dataC)
avgNodeA.append(avgC)
avgD=sum(dataD)/len(dataD)
avgNodeA.append(avgD)
avgE=sum(dataE)/len(dataE)
avgNodeA.append(avgE)
avgF=sum(dataF)/len(dataF)
avgNodeA.append(avgF)
avgG=sum(dataG)/len(dataG)
avgNodeA.append(avgG)
avgH=sum(dataH)/len(dataH)
avgNodeA.append(avgH)
avgI=sum(dataI)/len(dataI)
avgNodeA.append(avgI)
avgJ=sum(dataJ)/len(dataJ)
avgNodeA.append(avgJ)
avgK=sum(dataK)/len(dataK)
avgNodeA.append(avgK)
avgL=sum(dataL)/len(dataL)
avgNodeA.append(avgL)

print avgNodeA
def mode(data):
	hits = []
	for item in data:
	    tally = data.count(item)
	    #Makes a tuple that is the number of huts paired with the relevant number
	    values = (tally, item)
	    # Only add one entry for each number in the set
	    if values not in hits:
		hits.append(values)
	hits.sort(reverse=True)
	if hits[0][0]>=hits[1][0]:
	    print("\n\nThe mode is:", hits[0][1], "hit appeared", hits[0][0], "times.")
	else:
	    print("There is not a mode")
	return hits[0][1]
listmode=[]
listmode.append(-45)
listmode.append(mode(dataB))
listmode.append(mode(dataC))
listmode.append(mode(dataD))
listmode.append(mode(dataE))
listmode.append(mode(dataF))
listmode.append(mode(dataG))
listmode.append(mode(dataH))
listmode.append(mode(dataI))
listmode.append(mode(dataJ))
listmode.append(mode(dataK))
listmode.append(mode(dataL))
print listmode

with open('man1_1.csv', 'wb') as csvfile:
   writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
   #for row in avgNodeA:
   writer.writerow(listmode)


