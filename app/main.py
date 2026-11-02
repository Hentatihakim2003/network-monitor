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
        online=0
        offline=0
        ignored=0
        errors=0
        for ip in ips :
            if not check_valid_ip (ip) :
                if ip=="":
                    continue
                else :
                    print(f"{ip:<15}| ignored")
                    save_log(file,ip,"ignored")
                    ignored+=1
                    continue
            try : 
                response = ping(ip)
            except Exception as e:
                response = "error"
                error_message = str(e)  
                errors+=1
            if response=="error":
                print(f"{ip:<15}| error ⚠️  {error_message}")
                save_log(file,ip,"error ⚠️",error=error_message)
            elif response:
                response_ms = round(response * 1000, 2)
                print(f"{ip:<15}| online ✅ {response_ms} ms")          
                save_log(file,ip,"online ✅",response_ms)
                online+=1
            else:
                print(f"{ip:<15}| offline ❌")
                save_log(file,ip,"offline ❌")
                offline+=1
        total_valid = online + offline + errors
        save_summary(file, online, offline, errors, ignored,total_valid)


    print("\n========== MONITORING SUMMARY ==========")
    print(f"{'Total valid devices':<20}: {total_valid}")
    print(f"{'Online':<20}: {online}")
    print(f"{'Offline':<20}: {offline}")
    print(f"{'Errors':<20}: {errors}")
    print(f"{'Ignored':<20}: {ignored}")
    print("=" * 40)
    
def save_log(file, ip, result,response_ms=None,error=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if response_ms is not None:
        file.write(f"{timestamp} | {ip:<15}| {result} {response_ms} ms\n")
    elif error is not None:
        file.write(f"{timestamp} | {ip:<15}| {result} {error}\n")        
    else:
        file.write(f"{timestamp} | {ip:<15}| {result}\n")
def save_summary(file, online, offline, errors, ignored,total_valid):
    file.write("\n========== MONITORING SUMMARY ==========\n")
    file.write(f"{'Total valid devices':<20}: {total_valid}\n")
    file.write(f"{'Online':<20}: {online}\n")
    file.write(f"{'Offline':<20}: {offline}\n")
    file.write(f"{'Errors':<20}: {errors}\n")
    file.write(f"{'Ignored':<20}: {ignored}\n")
    file.write("=" * 40"\n\n")
devices=[]
devices=extract_file("devices.txt")
check_connection(devices)
