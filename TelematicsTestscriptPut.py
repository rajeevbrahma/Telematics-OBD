import requests
import time

sampledata_fromdevice = '$$CLIENT_1ZF,130329214,1,12.962985,77.576484,140127165433,A,22,0,0,140,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1253,420,1,0,1,200*26'


data_fromdevice_starseperated = sampledata_fromdevice[2:].split('*')

data_fromdevice_commaseperated = data_fromdevice_starseperated[0].split(',')

print data_fromdevice_commaseperated

d = data_fromdevice_commaseperated

while True:
	d[0] = raw_input("Enter clientid")
	d[1] = raw_input("Enter Serial_Number_of_the_Device")
	d[3] = raw_input("Enter Latitude ")
	d[4] = raw_input("Enter Longitude")
	d[5] = raw_input("Enter Date_and_time ")
	d[8]= raw_input("Enter Speed ")
	d[12]= raw_input("Enter Throttle_Position")
	d[16]= raw_input("Enter Odometer_Reading")
	d[17] = raw_input("Enter Vehicle_Speed")
	d[18]= raw_input("Enter Engine_Rpm ")
	d[21]= raw_input("Enter Engine_Coolant_Temparature ")
	d[23]= raw_input("Enter Ignition_Status ")
	d[41]= raw_input("Enter Engine_Fuel_Rate")
	d[42]= raw_input("Enter Engine_load_value")
	d[43]= raw_input("Enter Engine_Oil_Temparature")
	d[44]= raw_input("Enter Engine_Run_time")

	formedstring = ''
	for val in d:
		formedstring = formedstring+val+','
	# del formedstring[]
	payload = '"'+'$$'+formedstring[0:len(formedstring)-1]+'*26'+'"'

	print payload

	amazon_aws_api = requests.post('https://5ei70sqx23.execute-api.ap-southeast-1.amazonaws.com/putdevicedata/datestring/',data=payload)
	print amazon_aws_api.text

	time.sleep(20)

