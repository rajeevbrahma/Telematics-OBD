import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('dynamodb',region_name='ap-southeast-1')
    datestring = str(datetime.datetime.now().replace(microsecond=0))
    datestring = datestring.split(' ')
    newdatestring = datestring[0]+"="+datestring[1]
    
    data_fromdevice_starseperated = event[2:].split('*')
    
    data_fromdevice_commaseperated = data_fromdevice_starseperated[0].split(',')
    
    print data_fromdevice_commaseperated
    
    d = data_fromdevice_commaseperated
    
    
    	
    
    response = client.put_item(
    Item={
        'datestring': {'S': newdatestring,},
        'Client_ID': {'S': d[0],},
        'Serial_Number_of_the_Device':{'S': d[1],},
        'Latitude':{'S': d[3],},
    	'Longitude':{'S': d[4],},
    	'Date_and_time':{'S': d[5],},
    	'Speed':{'S': d[8],},
    	'Throttle_Position':{'S': d[12],},
    	'Odometer_Reading':{'S': d[16],},
    	'Vehicle_Speed':{'S': d[17],},
    	'Engine_Rpm':{'S': d[18],},
    	'Engine_Coolant_Temparature':{'S': d[21],},
    	# 'Ignition_ON_event':{'S': d[22],},
    	# 'Ignition_OFF_event':{'S': d[24],},
    	'Ignition_Status':{'S': d[23],},
    	'Engine_Fuel_Rate':{'S': d[41],},
    	'Engine_load_value':{'S': d[42],},
    	'Engine_Oil_Temparature':{'S': d[43],},
    	'Engine_Run_time':{'S': d[44],},
    	
    	
        
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='telematicsdb',
    )
    
    
    return 'Hello from Lambda',str(event)