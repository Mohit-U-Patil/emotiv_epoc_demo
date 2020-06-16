from cortex2 import EmotivCortex2Client

url = "wss://localhost:6868"
client_id = 'D8sPj2gQQj5jZ1moNhixWFAC3wsWvpoaA5Bl05cX',
client_secret = "HDiYXZIMsdGWs1iiHIvGm7ajx4YIQaEfjDrI7ApcPXDHEQQnl1TSLoJBhN4358DZdaEZrjoqZwObFwji687jVI67SgQkXxc8SxUILTB8aMiLN2ohwOIAjW2sdI4S7wIz",

# Remember to start the Emotiv App before you start!
# Start client with authentication
'''client = EmotivCortex2Client(url,
                             client_id='CLIENT_ID',
                             client_secret="CLIENT_SECRET",
                             check_response=True,
                             authenticate=True,
                             debug=False)'''

client = EmotivCortex2Client(url,
                             client_id=client_id,
                             client_secret=client_secret,
                             check_response=True,
                             authenticate=True,
                             debug=False)
# Test API connection by using the request access method
client.request_access()

# Explicit call to Authenticate (approve and get Cortex Token)
client.authenticate()

# Connect to headset, connect to the first one found, and start a session for it
client.query_headsets()
client.connect_headset(0)
client.create_session(0)

# Subscribe to the motion and mental command streams
# Spins up a separate subscription thread
client.subscribe(streams=["mot", "com"])

# Test message handling speed
a = client.subscriber_messages_handled
time.sleep(5)
b = client.subscriber_messages_handled
print((b - a) / 5)

# Grab a single instance of data
print(client.receive_data())

# Continously grab data, while making requests periodically
while True:
    counter += 1
    # time.sleep(0.1)

    if counter % 5000 == 0:
        print(client.request_access())

    # Try stopping the subscriber thread
    if counter == 50000:
        client.stop_subscriber()
        break

    try:
        # Check the latest data point from the motion stream, from the first session
        print(list(client.data_streams.values())[0]['mot'][0])
    except:
        pass