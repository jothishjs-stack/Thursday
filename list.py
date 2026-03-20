myDevices=["llaptop", "smarphones", "Table"]
print(myDevices[1])
myDevices[1]="iphone"
print(myDevices)
myDevices[1:2]="android", "micromax"
print(myDevices)
myDevices.insert(3,"chrome")
myDevices.append("AP")
print(myDevices)
list2=["car", "bike"]
list2.extend(myDevices)
print(list2)