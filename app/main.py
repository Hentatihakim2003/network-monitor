from ping3 import ping
import ipaddress
def check_valid_ip (ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
def extract_file(file):
    with open (file,"r") as file:
        devices = []
        for i in file:
            i=i.strip()
            devices.append(i)
    return devices
def check_connection(ips):
    for ip in ips :
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

devices=[]
devices=extract_file("devices.txt")
check_connection(devices)
