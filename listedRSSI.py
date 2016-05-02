import numpy as np
import matplotlib.pyplot as plt


#this is for 5m

rssi_noman = []
rssi_man = []

#values devided as, 50-55, 55-60, 60-65, 65-70, 70-75, 75-80, 80-85, 85-90


with open("../data/5mWithout.txt", "r") as f:	
	sum_rssi = 0
	countnoman=0
	for line in f:
		if not line.strip() or line.startswith('@') or line.startswith('#') or line.startswith(' '): 
			continue
		else:
			row = line.split(',')  
			if row[0]=="ESPap":    	
				value= int(row[1])
				#sum_rssi = sum_rssi + int(row[1])
				countnoman = countnoman + 1
				rssi_noman.append(value)
			else:
				continue

with open("../data/5mWith.txt", "r") as f:	
	sum_rssi = 0
	countman =0
	for line in f:
		if not line.strip() or line.startswith('@') or line.startswith('#') or line.startswith(' '): 
			continue
		else:
			row = line.split(',')  
			if row[0]=="ESPap":     	
				value= int(row[1])
				#sum_rssi = sum_rssi + int(row[1])
				countman = countman + 1
				rssi_man.append(value)
			else:
				continue

#print rssi_man
#print rssi_noman
a= []
b= []
c= []
d= []
e= []
f= []
g= []
h= []
for i in rssi_man:
	if i< -85:
		a.append(i)
	elif i<-80:
		b.append(i)
	elif i<-75:
		c.append(i)
	elif i<-70:
		d.append(i)
	elif i<-65:
		e.append(i)
	elif i<-60:
		f.append(i)
	elif i<-55:
		g.append(i)
	else:
		h.append(i)	
print "a is", a
print "b is",b
print "c is",c
print "d is",d
print "e is",e
print "f is",f
print "g is",g
print "h is",h

an= []
bn= []
cn= []
dn= []
en= []
fn= []
gn= []
hn= []
for i in rssi_noman:
	if i< -85:
		an.append(i)
	elif i<-80:
		bn.append(i)
	elif i<-75:
		cn.append(i)
	elif i<-70:
		dn.append(i)
	elif i<-65:
		en.append(i)
	elif i<-60:
		fn.append(i)
	elif i<-55:
		gn.append(i)
	else:
		hn.append(i)	
print "an is -->",an
print "bn is -->",bn
print "cn is -->",cn
print "dn is -->",dn
print "en is -->",en
print "fn is -->",fn
print "gn is -->",gn
print "hn is -->",hn

print "\ncount values\n"
print "count of link without man --> ", countnoman 
print "count of link with man --> ", countman 




