import json

with open("json/data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DN                                                 Description          Speed    MTU")
print("-" * 50, "-" * 20, "-" * 7, "-" * 7)

for x in data["imdata"]:
    values = x['l1PhysIf']['attributes']
    abc = values['dn']
    if (len(abc) == 42):
        print(f"{values['dn']}            {values['descr']}                  {values['speed']}  {values['mtu']}")
    else:
        print(f"{values['dn']}             {values['descr']}                  {values['speed']}  {values['mtu']}")