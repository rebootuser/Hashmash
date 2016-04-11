#!/usr/bin/python
import itertools
import sys
import hashlib
import getopt
from datetime import timedelta, datetime

infile=""
delim=1	
hashtype=1
intimes=""
intimef=""
match=""
stype="s"

def usage():
	print '''

 /$$   /$$                     /$$                                         /$$      
 | $$  | $$                    | $$                                        | $$      
 | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$| $$$$$$$ 
 | $$$$$$$$ |____  $$ /$$_____/| $$__  $$| $$_  $$_  $$ |____  $$ /$$_____/| $$__  $$
 | $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$ \ $$ \ $$  /$$$$$$$|  $$$$$$ | $$  \ $$
 | $$  | $$ /$$__  $$ \____  $$| $$  | $$| $$ | $$ | $$ /$$__  $$ \____  $$| $$  | $$
 | $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$| $$ | $$ | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
 |__/  |__/ \_______/|_______/ |__/  |__/|__/ |__/ |__/ \_______/|_______/ |__/  |__/

									version 0.1
 -h 		You're here

 --alg		Hash algorithm to use 
			1 MD5 (default)
			2 SHA1
			3 SHA256
			4 SHA512

 --delim	Include a delimiter between values
			1 None (default)
			2 Colon
			3 Space
			4 Ampersand

 --match	Specify a hash to match i.e. --match e23e4ae268f4ba432e74e625e6600e59
 
 --file		File containing values (one per line)
		
		Example:
			name 
			surname
			email@rebootuser.com
			phone_number

 		Generate Epochs (unix timestamps) between specified dates/times.
 		Each timestamp will be tested with defined values from --file

 --st 		Define a start time [used with --et]

 --et 		Define an end time [used with --st]

 --sec 		Seconds since Epoch (default)

 --milli 	Milliseconds since Epoch 

 		Example:
 			--st "2016-01-01 09:23:01" --et "2016-01-01 09:25:01" --milli

	'''

def md5hash(suppliedhash):
	hashed=hashlib.md5(suppliedhash).hexdigest()
	return hashed

def sha1hash(suppliedhash):
	hashed=hashlib.sha1(suppliedhash).hexdigest()
	return hashed

def sha256hash(suppliedhash):
	hashed=hashlib.sha256(suppliedhash).hexdigest()
	return hashed

def sha512hash(suppliedhash):
	hashed=hashlib.sha512(suppliedhash).hexdigest()
	return hashed

def epochcalc():
	epoch = datetime(1970,1,1)
	start_time = datetime.strptime(intimes, '%Y-%m-%d %H:%M:%S')
	end_time = datetime.strptime(intimef, '%Y-%m-%d %H:%M:%S')

	if stype == "s":
		timeint = timedelta(seconds=1)
	else:
		timeint = timedelta(milliseconds=1)	

	global testtimes
	global epochtimes
	testtimes = []
	epochtimes = []

	while start_time <= end_time:
		testtimes.append(start_time.strftime('%H:%M:%S'))
		if stype == "s":
			epochtimes.append(str("{0:.0f}".format((start_time - epoch).total_seconds())))
		else:
			epochtimes.append(str("{0:.0f}".format((start_time - epoch).total_seconds()*1000)))
		start_time += timeint

def itterate():
	for val in range(1, len(combos)+1):
		for subval in itertools.permutations(combos, val):

			if delim == 1: 
				subvaljoin="".join(subval)
			elif delim == 2:
				subvaljoin=":".join(subval)
			elif delim == 3:
				subvaljoin=" ".join(subval)
			elif delim == 4:
				subvaljoin="&".join(subval)
			else:
				sys.exit()
			
			print "Cleartext Value: " + subvaljoin

			if hashtype == 1:
				hashed = md5hash(subvaljoin)
				print hashed
			elif hashtype == 2:
				hashed = sha1hash(subvaljoin)
				print hashed
			elif hashtype == 3:
				hashed = sha256hash(subvaljoin)
				print hashed
			elif hashtype == 4:
				hashed = sha512hash(subvaljoin)
				print hashed
			else:
				sys.exit()

			if match == hashed:
				print ("\n[+] Gotya! \n%s\n")%subvaljoin
				sys.exit()

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h",["match=","alg=","delim=","file=","st=","et=","sec","milli"])
		if len(sys.argv) < 2:
			usage()
			sys.exit()

	except getopt.GetoptError:
		usage()
		sys.exit()

	try:	
		for opt, arg in opts:
			if opt == "-h":
				usage()
				print "[+] Looks like you need some help here!"
				sys.exit()
			elif opt == "--match":
				global match
				match = str(arg)
			elif opt == "--st":
				global intimes
				intimes = str(arg)
			elif opt == "--et":
				global intimef
				intimef = str(arg)
			elif opt == "--sec":
				global stype
				stype = 's'
			elif opt == '--milli':
				stype = 'm'
			elif opt == "--file":
				global infile
				infile = str(arg)
				try:
					open(infile)
				except IOError:
					print "[+] Error opening the file %s - does this exist?" %infile
					return	
			elif opt == "--alg":
				global hashtype
				hashtype = int(arg)
				if 1 <= hashtype <= 4:
					pass
				else:
					usage()
					print "[+] Hash algorithm not defined!"
					sys.exit()
			elif opt == "--delim":
				global delim
				delim = int(arg)
				if 1 <= delim <= 4:
					pass
				else:
					usage()
					print "[+] Delimeter not defined!"
					sys.exit()
			else:
				print "[+] errrr something went wrong bob!"
				sys.exit()		
			
	except SystemExit:
		sys.exit()
	
	if not infile:
		usage()
		print "[+] You need to specify an input file containing your variables (--file)"
		sys.exit()
	if not match:
		usage()
		print "[+] Where's the hash I need to --match?"
		sys.exit()

	else:
		pass

	with open(infile) as inputvals:
		global combos
		combos = inputvals.read().splitlines()

	if intimes:
		if intimef:
			epochcalc()
			for t in epochtimes:
				combos.insert(0,t)
				itterate()
				combos.remove(t)
		else:
			print "[+] Finish time not defined!"
	else:
		itterate()
	

if __name__ == "__main__":
	main()
