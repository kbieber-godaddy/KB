import ipaddress
print ("hello world")
print ("What is the subnet")
mySubnet = input() 
print ("here is the subnet you added " + mySubnet)

ipaddress.ip_address('192.168.1.1')

net4 = ipaddress.ip_network('192.0.2.0/24') 
for x in net4.hosts():
    print(x)
    i =len(net4.hosts)
    print (i)

    