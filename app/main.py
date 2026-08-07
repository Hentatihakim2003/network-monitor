from ping3 import ping
with open ("devices.txt","r") as file:
    print("Checking devices...\n")
    for ip in file:
        ip=ip.strip()
        if not ip : 
            continue 
        response = ping(ip)
        
        if response:
            response_ms = round(response * 1000, 2)
            print(f"{ip:<15}| online ✅ {response_ms} ms")
        else:
            print(f"{ip:<15}| offline ❌")