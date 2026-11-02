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
                raise Exception("Simulated network failure")
            except Exception as e:
                response = "error"
                error_message = str(e)   
            if response=="error":
                print(f"{ip:<15}| error ⚠️  {error_message}")
                save_log(file,ip,"error ⚠️",error=error_message)
            elif response:
                response_ms = round(response * 1000, 2)
                print(f"{ip:<15}| online ✅ {response_ms} ms")          
                save_log(file,ip,"online ✅",response_ms)
            else:
                print(f"{ip:<15}| offline ❌")
                save_log(file,ip,"offline ❌")
def save_log(file, ip, result,response_ms=None,error=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if response_ms is not None:
        file.write(f"{timestamp} | {ip:<15}| {result} {response_ms} ms\n")
    elif error is not None:
        file.write(f"{timestamp} | {ip:<15}| {result} {error}\n")        
    else:
        file.write(f"{timestamp} | {ip:<15}| {result}\n")
        
devices=[]
devices=extract_file("devices.txt")
check_connection(devices)
