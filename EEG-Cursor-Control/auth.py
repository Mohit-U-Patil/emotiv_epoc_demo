import json
import ssl
from websocket import create_connection

receivedData = create_connection("wss://localhost:6868", sslopt={"cert_reqs": ssl.CERT_NONE})
# receivedData = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})

#get Cortex info and confirm connection
receivedData.send(json.dumps({"id":1,"jsonrpc":"2.0","method":"getCortexInfo"}))

receivedData.send(json.dumps({"id": 1,
    "jsonrpc": "2.0",
    "method": "authorize",
    "params": { "client_id" : 'D8sPj2gQQj5jZ1moNhixWFAC3wsWvpoaA5Bl05cX', "client_secret" : "HDiYXZIMsdGWs1iiHIvGm7ajx4YIQaEfjDrI7ApcPXDHEQQnl1TSLoJBhN4358DZdaEZrjoqZwObFwji687jVI67SgQkXxc8SxUILTB8aMiLN2ohwOIAjW2sdI4S7wIz"
},
}))

token = json.loads(receivedData.recv())["result"]  #["_auth"]

print("Hello USER.")
print("\nThe following set of letters is your session token. In order maintain security, do not share this token:\n\n"+str(token))
print("\n\nThis token has been automatically registered as your session token. You may use the headset as a client")
