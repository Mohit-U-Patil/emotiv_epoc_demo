import json
import ssl
from websocket import create_connection

receivedData = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})
# receivedData = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})

#get Cortex info and confirm connection
receivedData.send(json.dumps({"id":1,"jsonrpc":"2.0","method":"getCortexInfo"}))
print(receivedData.recv())

receivedData.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "requestAccess",
    "params": { "clientId" : 'D8sPj2gQQj5jZ1moNhixWFAC3wsWvpoaA5Bl05cX', "clientSecret" : "HDiYXZIMsdGWs1iiHIvGm7ajx4YIQaEfjDrI7ApcPXDHEQQnl1TSLoJBhN4358DZdaEZrjoqZwObFwji687jVI67SgQkXxc8SxUILTB8aMiLN2ohwOIAjW2sdI4S7wIz"
}
}))
print(receivedData.recv())

receivedData.send(json.dumps({"id": 1,
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": { "clientId" : 'D8sPj2gQQj5jZ1moNhixWFAC3wsWvpoaA5Bl05cX', "clientSecret" : "HDiYXZIMsdGWs1iiHIvGm7ajx4YIQaEfjDrI7ApcPXDHEQQnl1TSLoJBhN4358DZdaEZrjoqZwObFwji687jVI67SgQkXxc8SxUILTB8aMiLN2ohwOIAjW2sdI4S7wIz"
},
}))

# print(receivedData.recv())

token = json.loads(receivedData.recv())['result']['cortexToken']
print(token)

# print(receivedData.recv())

#get new token in case old one expires. 2 days expiry if hasn't been extended
# receivedData.send(json.dumps({
#     "id": 1,
#     "jsonrpc": "2.0",
#     "method": "generateNewToken",
#     "params": {
#         "cortexToken": token,
#         "clientId": "D8sPj2gQQj5jZ1moNhixWFAC3wsWvpoaA5Bl05cX",
#         "clientSecret": "HDiYXZIMsdGWs1iiHIvGm7ajx4YIQaEfjDrI7ApcPXDHEQQnl1TSLoJBhN4358DZdaEZrjoqZwObFwji687jVI67SgQkXxc8SxUILTB8aMiLN2ohwOIAjW2sdI4S7wIz"
#     }
# }))
# token = json.loads(receivedData.recv())['result']['cortexToken']

print("Hello USER.")
print("\nThe following set of letters is your session token. In order maintain security, do not share this token:\n\n"+str(token))
print("\n\nThis token has been automatically registered as your session token. You may use the headset as a client")

# receivedData.send(json.dumps({
#     "id": 1,
#     "jsonrpc": "2.0",
#     "method": "controlDevice",
#     "params": {
#         "command": "refresh"
#     }
# }))

#

#from the file= Client
print("\nHeadset Query...")
receivedData.send(json.dumps({
    "jsonrpc": "2.0",
    "method": "queryHeadsets",
    "params": {},
    "id": 1
}))
print(receivedData.recv())

print("\nCreating session...")

#old cortex method to open the session.
# receivedData.send(json.dumps({
#     "jsonrpc": "2.0",
#     "method": "createSession",
#     "params": {
#         "_auth": token,
#         "status": "open",
#         "project": "test"
#     },
#     "id": 1
# }))

#new cortex method to open the session. We don't activate the session yet.
receivedData.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "createSession",
    "params": {
        "cortexToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS5tb2hpdDMubW9oaXRfcGF0aWxfYXBwMSIsImFwcFZlcnNpb24iOiIxLjAiLCJleHAiOjE1OTM3MzA4MDcsIm5iZiI6MTU5MzQ3MTYwNywidXNlcklkIjoiOWFmNjc0ZGMtNGMyMC00NjNkLTkxYTQtMzk0M2ZmNjA5N2RkIiwidXNlcm5hbWUiOiJtb2hpdDMiLCJ2ZXJzaW9uIjoiMi4wIn0=.shMkkWk2PFSMm6ekGFeKKNlGbevM1UhiWrPGLGd1RaY=",
        "headset": "EPOCPLUS-4A2C110A",
        "status": "open"
    }
}))
# print(receivedData.recv())

session_id = json.loads(receivedData.recv())['result']['id']
# 55dcde01-9066-470c-8bba-63e2bc0ed2ed
print("session_id= ", session_id)

print("\nSubscribing to session...")

#old documented method. still valid
receivedData.send(json.dumps({
    "id": 1,
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {
        "cortexToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6ImNvbS5tb2hpdDMubW9oaXRfcGF0aWxfYXBwMSIsImFwcFZlcnNpb24iOiIxLjAiLCJleHAiOjE1OTM3MzA4MDcsIm5iZiI6MTU5MzQ3MTYwNywidXNlcklkIjoiOWFmNjc0ZGMtNGMyMC00NjNkLTkxYTQtMzk0M2ZmNjA5N2RkIiwidXNlcm5hbWUiOiJtb2hpdDMiLCJ2ZXJzaW9uIjoiMi4wIn0=.shMkkWk2PFSMm6ekGFeKKNlGbevM1UhiWrPGLGd1RaY=",
        "session": session_id,
        "streams": ["sys","mot"]
    }
}))
print(receivedData.recv())

