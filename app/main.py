from ping3 import ping
import ipaddress
from datetime import datetime

def check_valid_ip (ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
def extract_file(file):
    try:
        with open (file,"r") as file:
            devices = []
            for i in file:
                i=i.strip()
                devices.append(i)
        return devices
    except FileNotFoundError : 
        print("file not found.")
        return([])
def check_connection(ips):
    with open("test.log", "a", encoding="utf-8") as file:
        for ip in ips :
            if not check_valid_ip (ip) :
                if ip=="":
                    continue
                else :
                    print(f"{ip:<15}| ignored")
                    save_log(file,ip,"ignored")
                    continue
            try : 

                response = ping(ip)
                
                if response:
                    response_ms = round(response * 1000, 2)
                    print(f"{ip:<15}| online ✅ {response_ms} ms")          
                    save_log(file,ip,"online ✅")
                else:
                    print(f"{ip:<15}| offline ❌")
                    save_log(file,ip,"offline ❌")
            except Exception:
                print(f"{ip:<15}| error ⚠️")
                save_log(file,ip,"error ⚠️")

                continue
def save_log(file, ip, result):
    file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {ip:<15}| {result}\n")

devices=[]
devices=extract_file("devices.txt")
check_connection(devices)
