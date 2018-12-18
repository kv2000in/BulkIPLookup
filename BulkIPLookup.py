#!/usr/bin/python
#usage supply file and source IP address as args
#Output can be used at https://www.infobyip.com/ipbulklookup.php which searches bulk IP addresses separated by space or new line char
import sys
import re
mytxt="a"
myfile = open(sys.argv[1],'r')
myregex = re.escape(sys.argv[2])+r'\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
for eachline in myfile:
	mytxt += eachline
mytxt1=re.findall(myregex,mytxt)
myfile.close()
mytxt2=""
i=0
while i <len(mytxt1): 
	mytxt2+=mytxt1[i]+" "
	i+=1
print mytxt2

