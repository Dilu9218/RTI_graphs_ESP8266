import numpy as np
import matplotlib.pyplot as plt

#sage /*dilushi: search */

#this is probability for 5m

rssi_noman = []
rssi_man = []

#values should be from, 50-55, 55-60, 60-65, 65-70, 70-75, 75-80, 80-85, 85-90


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
print "f is",f, "No of list Items", len(f)
print "g is",g, "No of list Items", len(g)
print "h is",h, "No of list Items", len(h)

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
print "an is -->",an, len(an)
print "bn is -->",bn
print "cn is -->",cn
print "dn is -->",dn
print "en is -->",en
print "fn is -->",fn, "No of list Items", len(fn)
print "gn is -->",gn, "No of list Items", len(gn)
print "hn is -->",hn, "No of list Items", len(hn)

Pgn= float(len(gn))/float(countnoman)
Pg= float(len(g))/float(countman)
Pfn= float(len(fn))/float(countnoman)
Pf= float(len(f))/float(countman)
print "Probabilty of cateory g-> Pgn is", Pgn, "  Pg is", Pg
print "Probabilty of cateory f-> Pfn is", Pfn, "  Pf is", Pf

print "\ncount values\n"
print "count of data in link without man --> ", countnoman 
print "count of data in link with man --> ", countman 
count= countman + countnoman
print "whole count --> ", count 
#finding probability of man ,give RSSI`-`
#find to which category/list RSSI value belongs to. Using bayesian probabilty, find following 

#hardcode example RSSI= -56 belonging to gn and g
RSSI= -56
RSSI= -60

#probability of RSSI (category), given man
Pgvnman= float(len(g))/float(countman)
Pgvnman2= float(len(f))/float(countman)
print "\n\nprobability of RSSI (category g), given man", Pgvnman 
print "\nprobability of RSSI (category f), given man", Pgvnman2
 
#probability of RSSI (category), given all data 
Pgvndata= float((len(g)+len(gn)))/float(count)
Pgvndata2= float((len(f)+len(fn)))/float(count)
print "\n\nprobability of RSSI (category g), given data" ,Pgvndata
print "\nprobability of RSSI (category f), given data" ,Pgvndata2

#probability of Man-> this is assumed as 0.5. Use recursive bayesian for convergence
Pm= 0.5 

#bayesian probabilty, probability of man, given RSSI
Pgvnrssi=  Pgvnman*Pm/Pgvndata
Pgvnrssi2=  Pgvnman2*Pm/Pgvndata2
print "\n\nprobability of man, given RSSI= -56 is ", Pgvnrssi
print "\nprobability of man, given RSSI= -61 is ", Pgvnrssi2



