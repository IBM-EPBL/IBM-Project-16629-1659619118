import random
import time
import sys
import ibmiotf.application
import ibmiotf.device


# Provide your IBM Watson Device Credentials

organization = "kuhkhy"
deviceType = "smartwaste"
deviceId = "waste"
authMethod= "token"
authToken= "keerthi@2002"


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status == 'lighton':
        print("LIGHT ON")
    elif status == 'lightoff':
        print("LIGHT OFF")
    else:
        print ("please send proper command")


try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
# ..............................................

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:
    w= random.randint(0,100)
    l = random.randint(0,100)
   
    # Send Temperature & Humidity to IBM Watson
    data = {'weight': w,'level':l}


    # print data
    def myOnPublishCallback():
        print("Published data",data, "to IBM Watson")


    success = deviceCli.publishEvent("event", "json", data, 0, myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(5)

    deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
devicecli.disconnect()
