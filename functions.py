def message():
    print("Hello, World!")

message()

def add(a, b):
    return a + b
result=add(5, 3)
print("The sum is:", result)
#no spaces for function so use underscopr eg: fun deive = fun_deive

def configure_device(device_name, ip_address):
    print(f"Configuring {device_name} with IP address {ip_address}")
    print("Deviceconnecting...",device_name)
    print("Device configured successfully!")    

configure_device("Router", "192.168.1.1")   

devices=["Router","switch","firewall"]

def configure_device(device_name, ip_address):
    print("Configuring {device_name} with IP address {ip_address}")
    print("Device connecting...", device_name)
    print("Device configured successfully!")    

def my_function(name, age):
    print(Hello {name}, you are {age} years old.")
my_function("Alice", 30)
my_function("Bob", 25)  
my_function(name="Charlie", age=35) 