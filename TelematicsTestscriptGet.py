import requests
import demjson
import time

while True:

	selection = int(raw_input("\n\nEnter 1 for getlatest and 2 for gethistory  \n"))

	if (selection == 1):

		primarykey = raw_input("\nEnter the Serial_Number_of_the_Device\n\t")
		primarykey = str(primarykey)
		print primarykey

		amazon_aws_api = requests.get('https://qktfz1u0b6.execute-api.ap-southeast-1.amazonaws.com/getlatest/telematics?Serial_Number_of_the_Device='+primarykey+'')

		amazon_aws_data =  amazon_aws_api.text
		amazon_aws_dict = demjson.decode(amazon_aws_data)
		print amazon_aws_dict

	elif(selection == 2):
		primarykey = str(raw_input("\nEnter the Serial_Number_of_the_Device\n\t"))
		sortkey = str(raw_input("\nEnter the datestring from where you want to fetch the data in the following format\n\t\t\tyyyy-mm-dd=HH:MM:SS"))
		print primarykey,sortkey
		amazon_aws_api = requests.get('https://faya0pk284.execute-api.ap-southeast-1.amazonaws.com/gethistory/telematics?Serial_Number_of_the_Device='+primarykey+'&datestring='+sortkey+'')
		amazon_aws_data =  amazon_aws_api.text
		amazon_aws_dict = demjson.decode(amazon_aws_data)
		print amazon_aws_dict

	else:
		print "Wrong selection"

	time.sleep(20)			

# https://faya0pk284.execute-api.ap-southeast-1.amazonaws.com/gethistory/telematics?Serial_Number_of_the_Device=130329214&datestring=2017-04-01=06:07:03	
# https://qktfz1u0b6.execute-api.ap-southeast-1.amazonaws.com/getlatest/telematics?Serial_Number_of_the_Device=130329214