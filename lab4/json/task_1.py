import json

json_path = "./sample-data.json"


#Reading from file to json object
with open(json_path) as json_data:
    data = json.load(json_data)


#print(data["imdata"])

col = []
for x in data["imdata"]:
    col.append((x["l1PhysIf"]["attributes"]["dn"],x["l1PhysIf"]["attributes"]["descr"], x["l1PhysIf"]["attributes"]["speed"], x["l1PhysIf"]["attributes"]["mtu"]))



print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for x in col:
    print((x[0]).ljust(50), (x[1]).ljust(20), (x[2]).rjust(7), (x[3]).rjust(6))
