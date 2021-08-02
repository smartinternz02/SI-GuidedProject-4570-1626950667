import wiotp.sdk.device
import time
import random
#import people_counter
import os


#count=people_counter.print( 'UP:',cnt_up)
#count=people_counter.print ('DOWN:',cnt_down)
myConfig = { 
    "identity": {
        "orgId": "mawtlg",
        "typeId": "VIT-IOT-device",
        "deviceId":"12345"
    },
    "auth": {
        "token": "12345678"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()


while True:
    seconds=int(input("how many seconds to wait-"))
    def time_display():
      #seconds=int(0)
      
      #seconds=int(input("how many seconds to wait"))
      for i in range(seconds):
       print(str(seconds-i) +"seconds remain")
       time.sleep(1)
      
           
      
   
    peoplecrossing=people_counter.cnt_up+people_counter.cnt_down
    if peoplecrossing<=10:
        print('Red light is ONN')
        print('green light is OFF')
        print('orange light os OFF')
        print('waiting time is one minute')
        time_display()
        myData={'Peoplewaiting':peoplecrossing, 'Signaltime':seconds}
        print("Published data Successfully: ", myData)
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        client.commandCallback = myCommandCallback
        time.sleep(2)
        if peoplecrossing>=10:
            print('RED light is ONN')
            print('green light is OFF')
            print('orange light is OFF')
            print('waiting time is 2 minutes')
            time_display()
            myData={'Peoplewaiting':peoplecrossing, 'Signaltime':seconds}
            print("Published data Successfully: ", myData)
            client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
            client.commandCallback = myCommandCallback
            time.sleep(2)
    
     
client.disconnect()
