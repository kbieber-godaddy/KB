import ipaddress
def process(line):
    # Output network with mask bits (192.168.0.0/24)
    try:
        return print(ipaddress.IPv4Interface(line).network)
    except Exception:
        
        return print("FAIL_OR_EMPTY")
with open('in.txt', 'r') as f:
    for line in f:
        line = "".join(line.split())
        process(line)