import ipaddress

ip = input("Enter IPv4 Address (e.g., 192.168.0.1): ")
cidr = input("Enter CIDR Prefix (e.g., 27): ")

# Combine IP and CIDR into a network object
network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)

# Get all usable host IPs
hosts = list(network.hosts())

print("\n--- SUBNET DETAILS ---")
print("Subnet Mask       :", network.netmask)
print("Network ID        :", network.network_address)
print("Broadcast Address :", network.broadcast_address)

if len(hosts) > 0:
    print("Usable Host Range :", hosts[0], "to", hosts[-1])
    print("Total Usable IPs  :", len(hosts))
else:
    print("Usable Host Range : N/A")
    print("Total Usable IPs  : 0")