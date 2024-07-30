import netifaces as ni

def get_local_ip_addresses():
    ip_addresses = []
    try:
        # Get all network interfaces
        interfaces = ni.interfaces()
        
        # Iterate over each interface and get its IP addresses
        for interface in interfaces:
            addresses = ni.ifaddresses(interface)
            if ni.AF_INET in addresses:
                ip = addresses[ni.AF_INET][0]['addr']
                if ip not in ip_addresses:
                    ip_addresses.append(ip)
    except Exception as e:
        print(f"Error: {e}")
    return ip_addresses

# Example usage
local_ips = get_local_ip_addresses()
print("Local IP addresses:")
for ip in local_ips:
    print(ip)
