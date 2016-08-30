# HashMash
For more information visit www.rebootuser.com

## Version 0.2
* Added support for more hashing algorithms and delimiters
* Now can select '--alg 11' to use all delimiters in a single attack

### Description:
HashMash has been created to aid in generating various hashes from user supplied values. Occasionally on a test you'll see some dodgy looking functionality that you might look at and say *'that looks vulnerable'*. For example password reset functionality that returns an MD5 hash of something. Here's where Hashmash comes in.

For further information on usage and all else, visit http://www.rebootuser.com

### General usage:

 	--alg		Hashing algorithm to use 
				1 MD5 (default)
				2 SHA1
				3 SHA224
				4 SHA256
				5 SHA384
				6 SHA512

 	--delim		Include a delimiter between values
				1 None (default)
				2 Colon
				3 Space
				4 Ampersand
				5 Comma
				6 Period
				7 Hyphen
				8 Underscore
				9 Pipe
				10 Semi-colon
				11 All of the above (slow)

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

### Example Usage:

* Generate MD5 hashes from values in values.txt:

		python hashmash.py --match e23e4ae268f4ba432e74e625e6600e59 --file values.txt


* As above but also generate Epoch values between 01/01/2016 @ 9:23:01 am and 01/01/2016 @ 9:25:01 am:

 		python hashmash.py --match e23e4ae268f4ba432e74e625e6600e59 --file values.txt --st "2016-01-01 09:23:01" --et "2016-01-01 09:25:01"

* As above but to millisecond percision (slow) and use & as a delimiter between supplied values:

		python hashmash.py --match e23e4ae268f4ba432e74e625e6600e59 --file values.txt --delim 4 --st "2016-01-01 09:23:01" --et "2016-01-01 09:25:01" --milli

* By default all hashes will be shown on screen - this does slow the script down so perhaps redirect output to a file, i.e. > out.txt
