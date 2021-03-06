import paho.mqtt.client as mqtt
import time
from ursina import *                    # Import the ursina engine
client = mqtt.Client()
mqttmsg = ""
xval = ""
yval = ""
zval = ""
xint = 0
yint = 0
zint = 0
axint = 0
ayint = 0
azint = 0


client.connect("127.0.0.1", 1883, 60)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gyroX")
    client.subscribe("gyroY")
    client.subscribe("gyroZ")
    client.subscribe("accelerationX")
    client.subscribe("accelerationY")
    client.subscribe("accelerationZ")
client.on_connect = on_connect
# The callback for when a PUBLISH message is received from the server.

app = Ursina()  
cube = Entity(model='cube', color=color.orange, scale=(2,2,2))   
Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="Waiting for response")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = True    

def on_message(client, userdata, msg):
    time.sleep(0.01)
    msgsubstring = str(msg.payload)
    trimedstring = msgsubstring.replace('b', '')#stripping the b char from the string
    trimedstring1 = trimedstring.replace("'","") 
    info.text=trimedstring1
    

    xval=info.text.split(" ")
    #print('xval is:' + xval[0])
    #print('yval is:' + xval[1])
    #print('zval is:' + xval[2])
    #print('axval is:' + xval[3])
    #print('ayval is:' + xval[4])
    #print('azval is:' + xval[5])
    
    xint = int(float(xval[0]))
    yint = int(float(xval[1]))
    zint = int(float(xval[2]))
    axint = int(float(xval[3]))
    ayint = int(float(xval[4]))
    azint = int(float(xval[5]))
    #print('the value of cubey is :' + str(xint * 10))
    cube.rotation_y += yint *10
    cube.rotation_x += xint *10
    cube.rotation_z += zint *10
    cube.x += (axint+1) /10
    #cube.y += (ayint) /10
    cube.z += (ayint) /10

    #info.text=str(cube.rotation_x, cube.rotation_y,  cube.rotation_z)

client.on_message = on_message
client.loop_start()


def update():
    pass
    #cube.rotation_y += xint *10   # Rotate every time update is called
    

app.run()    

    





