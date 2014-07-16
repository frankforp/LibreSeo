#!/usr/bin/python2.7

# Imports
import urllib2
import random 
import time

# Set Query words
searchTerms = ["Hopefully", "this", "code", "will", "run"]

# Makes the string for the request
def randWords():
	Query = "http://duckduckgo.com/?q=" + (random.choice(searchTerms)) 
	return Query

req = urllib2.Request(url=randWords())
f = urllib2.urlopen(req)


# Sends Query using the calls above
def sendQuery():
	# Prints query to check if its random	 
	print randWords() 
	return f.read()

# Reads the contents of the severs message
# To check if it is connected
def checkconnect():
	if f.read() == None:
		return False
	else:
		return True

# Checks to make sure that
# CheckConnect returned results
def checkCheckconnect():
	if checkconnect() == True:
		print "Connected"
	else:
		print "Error"

def ranTime():
	# Makes the wait bewteen querys
	time.sleep(random.randint(1,3))



# My main function 
def main():
	print "Attempting to query to" # Looks Cool

	sendQuery() # Sends Query 

	checkCheckconnect() # Makes sure query went through

# Calls main
if __name__ == '__main__':
	
	print " \n \n 	This software is liscensed under Gpl-3 \n "

	

	print """
	 ___________ _____ _   _     _____ _____ _____ 
	|  _  | ___ \  ___| \ | |   /  ___|  ___|  _  |
	| | | | |_/ / |__ |  \| |   \ `--.| |__ | | | |
	| | | |  __/|  __|| . ` |    `--. \  __|| | | |
	\ \_/ / |   | |___| |\  |   /\__/ / |___\ \_/ /
	 \___/\_|   \____/\_| \_/   \____/\____/ \___/ 

	 """
	                                               
	                                               
	                  
	while 1:
		# Makes it wait
		ranTime() 
		# Calls main
		main()
		print "#################################### \n"


