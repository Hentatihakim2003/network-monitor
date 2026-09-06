from ping3 import ping
import ipaddress
def check_valid_ip (ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False 
with open ("devices.txt","r") as file:
    print("Checking devices...\n")
    for ip in file:
        ip=ip.strip()
        if not check_valid_ip (ip) :
            if ip=="":
                continue
            else :
                print(f"{ip:<15}| ignored") 
                continue 
        response = ping(ip)
        
        if response:
            response_ms = round(response * 1000, 2)
            print(f"{ip:<15}| online ✅ {response_ms} ms")
        else:
            print(f"{ip:<15}| offline ❌")