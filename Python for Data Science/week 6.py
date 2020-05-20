"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
 """


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
a=list()
for line in handle:
   	if "From" in line.split():
    	a.append(line.split(":")[0][len(line.split(":")[0])-2:len(line.split(":")[0])+1])
d=dict()
for i in a:
    d[i]=d.get(i,0)+1
    
b=d.items()
b=sorted(b)
for i,j in b:
    print(i,j)
    
	
