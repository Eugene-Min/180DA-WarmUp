import paho.mqtt.client as mqtt
import numpy as np
import time
import random
import sys
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("p1_logi")

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

opponent_choice = ""
# The default message callback.
# (won’t be used if only publishing, but can still exist)
def on_message(client, userdata, message):
    global opponent_choice
    opponent_choice = message.payload.decode()

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# 4. use subscribe() to subscribe to a topic and receive messages.

# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.
while(True):
    while(True):
        player_choice = input('Please choose rock (r), paper (p), or scissors (s) or q to quit. \n')
        if(player_choice == 'r'):
            print("You chose rock.\n")
            client.publish("EugeneMin2", player_choice, 1)
            break
        elif(player_choice == 'p'):
            print("You chose paper.\n")
            client.publish("EugeneMin2", player_choice, 1)
            break
        elif(player_choice == 's'):
            print("You chose scissors.\n")
            client.publish("EugeneMin2", player_choice, 1)
            break
        elif(player_choice == 'q'):
            print("Quitting Game! Thanks for playing.\n")
            client.publish("EugeneMin2", player_choice, 1)
            sys.exit()
        else:
            print("Invalid Input")
    while(opponent_choice == ""):
        print("Waiting for player input.")
        time.sleep(3)
    if(opponent_choice == 'q'):
        print("Opponent quit game. Quitting gmae too!")
        sys.exit()
    if(player_choice == 'r'):
        if(opponent_choice == 'r'): #rock
            print("The opponent chose rock.\n")
            print("You tied.\n")
        elif(opponent_choice == 'p'): #paper
            print("The opponent chose paper.\n")
            print("You lost.\n")
        elif(opponent_choice == 's'): #scissors
            print("The opponent chose scissors.\n")
            print("You win!\n")
    elif(player_choice == 'p'):
        if(opponent_choice == 'r'): #rock
            print("The opponent chose rock.\n")
            print("You win!\n")
        elif(opponent_choice == 'p'): #paper
            print("The opponent chose paper.\n")
            print("You tied.\n")
        elif(opponent_choice == 's'): #scissors
            print("The opponent chose scissors.\n")
            print("You lost.\n")
    elif(player_choice == 's'):
        if(opponent_choice == 'r'): #rock
            print("The opponent chose rock.\n")
            print("You lost.\n")
        elif(opponent_choice == 'p'): #paper
            print("The opponent chose paper.\n")
            print("You win!\n")
        elif(opponent_choice == 's'): #scissors
            print("The opponent chose scissors.\n")
            print("You tied.\n")
    opponent_choice = ''
# 6. use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()