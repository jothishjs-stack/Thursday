# file=open("file.text","w")
# file.write("Hello World")
# file.close()
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))

# with open("file.text","a") as file:
#     # file.write(f"\nMy name is {name} and I am {age} years old.")
#     file.write(f"\nMy name is {name}\n")
#     file.write(f"I am {age} years old.\n") 
# print("Data has been written to the file.")          
############################################

# with open("devices.txt","r") as file:
#     devices=file.readlines()
   
# for ip in devices:
#     print("connecting to",ip.strip())

############################################

# device_ip="192.168.0.15"
# config_data="""
# hostname Router1
# interface GigabitEthernet0/0
#  ip address 192.168.0.1 255.255.255.0"""

# filename=device_ip+"_backup.txt"
# with open(filename,"w") as file:
#     file.write(config_data)
# print(f"Configuration data s been saved to {filename}.")
#################################################

# results= "ping to 192.168.0.1 succeessful"
# with open("ping_results.txt","a") as file:
#     file.write(results+ "\n")

##########################################33

# with open("commands.txt","r") as file:
#     commands=file.readlines()
# for command in commands:
#     print("Executing command:",command.strip())
##############################################
with open("devices.txt","r") as file:
    devices=file.readlines()
for ip in devices:
    ip=ip.strip()
        if ip.endswith("1"):
            with open("success.txt","a") as success:
            success.write(f"Successfully connected to {ip}\n")
        else:
            with open("failure.txt","a") as failure:
            failure.write(f"Failed to connect to {ip}\n")