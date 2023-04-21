import random
import ipaddress

# Define the number of IP addresses to generate
num_ips = 10000

# Define the ratio of private to public IPs
private_ratio = 0.75
public_ratio = 0.25

# Calculate the number of private and public IPs to generate
num_private = int(num_ips * private_ratio)
num_public = num_ips - num_private

# Define the ranges of private IP addresses
private_ranges = [
    ipaddress.ip_network('10.0.0.0/8'),
    ipaddress.ip_network('172.16.0.0/12'),
    ipaddress.ip_network('192.168.0.0/16')
]

# Generate the private IP addresses
private_ips = []
while len(private_ips) < num_private:
    ip = str(ipaddress.ip_address(random.getrandbits(32)))
    for network in private_ranges:
        if ipaddress.ip_address(ip) in network:
            private_ips.append(ip)
            break

# Generate the public IP addresses
public_ips = []
while len(public_ips) < num_public:
    ip = str(ipaddress.ip_address(random.getrandbits(32)))
    if not any(ipaddress.ip_address(ip) in network for network in private_ranges):
        public_ips.append(ip)

# Combine the private and public IP addresses
ips = private_ips + public_ips

# Write the IP addresses to a file
with open('ips.txt', mode='w') as file:
    for ip in ips:
        file.write(ip + '\n')

print(f"Successfully generated {num_ips} IP addresses and wrote them to ips.txt.")
