#!/usr/local/bin/python2.7
import os
import time
DBsave = "/root/IPBlacklist.txt" #change if you don't like the path
def Filter(data):
	count = 0
	path = "/var/log/filter.log"
	f = open(path,'r')
	olddata = []
	unsorted = []
	with open(data) as old:
		for odata in old:
			if len(odata.strip()) != 0:
				olddata.append(odata.rstrip("\n"))
	sorted = []
	with open(path) as text:
		for line in text:
			if 'RULEID' in line: ### Need to change this line based on your rule number
				unsorted.append(line.split(',')[18])
	nextdata = list(set(unsorted))
	nextolddata = list(set(olddata))
	for nextline in nextdata:
		if nextline not in nextolddata:
			count += 1
			sorted.append(nextline)
	if count == 0:
		exit()
	else:
		for fileline in sorted:
			file = open(data, 'a+')
			file.write(fileline + "\n")
			file.close()
if not os.path.exists(DBsave):
	with open(DBsave, 'w'): pass
Filter(DBsave)