import requests
import demjson
import time

while True:

	selection = int(raw_input("\n\nEnter 1 for gethistory and 2 for getlatest \n"))

	if (selection == 1):

		primarykey = raw_input("\nEnter the datestring from where you want to fetch the data in the following format\n\t\t\tyyyy-mm-dd=HH:MM:SS")
		primarykey = str(primarykey)
		# primarykey = '2017-03-2411:18:54'
		print primarykey

		amazon_aws_api = requests.get('https://j1p9w1cwng.execute-api.ap-southeast-1.amazonaws.com/gethistory/datestring/'+primarykey+'')

		amazon_aws_data =  amazon_aws_api.text
		amazon_aws_dict = demjson.decode(amazon_aws_data)
		print amazon_aws_dict

	elif(selection == 2):
		amazon_aws_api = requests.get('https://j1p9w1cwng.execute-api.ap-southeast-1.amazonaws.com/gethistory/datestring/*')
		amazon_aws_data =  amazon_aws_api.text
		amazon_aws_dict = demjson.decode(amazon_aws_data)
		print amazon_aws_dict

	else:
		print "Wrong selection"

	time.sleep(20)			