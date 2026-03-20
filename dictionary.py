devices={
    "router": "Cisco",
    "switch": "Juniper",
    "firewall": "Palo Alto",
    "ip_address": "192.168.1.1",
    "Device_count": 4,
    "Device_count": 40,
    "colors": ["red", "green", "blue"]
}
print(devices["colors"][2])
print(type(devices))
new1=devices.keys()
new2=devices.values()
print(new1)
devices["access point"]="Ubiquiti"
print(new1)
print(new2)
new3=devices.items()
print(new3)
#oonditional statements
if "router" in devices:
    print("Router is present in the dictionary")
else:
    print("Router is not present in the dictionary")
    devices.update({"access point":"ap1"})
print(devices)
# del devices["switch"]
# #     print(devices)
# # del devices
#  print(devices)  
for x in devices:
    print(x)
    for key in devices:
        print(devices[key])