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
dataK = []
dataL = []
dataM = []

#-------------------------------------------------------------------------------
with open("nodeA_edited", "r") as f:
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

			if line[i]=="K":
				dataK.append(-int(line[i+2:i+4]))
				avg=sum(dataK)/len(dataK)  
       	
			if line[i]=="L":
				dataL.append(-int(line[i+2:i+4]))
				avg=sum(dataL)/len(dataL)
	
			if line[i]=="M":
				dataM.append(-int(line[i+2:i+4]))
				avg=sum(dataM)/len(dataM)  
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
avgK=sum(dataK)/len(dataK)
avgNodeA.append(avgK)
avgL=sum(dataL)/len(dataL)
avgNodeA.append(avgL)
avgM=sum(dataM)/len(dataM)
avgNodeA.append(avgM)

print avgNodeA


with open('empty.csv', 'wb') as csvfile:
   writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
   #for row in avgNodeA:
   writer.writerow(avgNodeA)


