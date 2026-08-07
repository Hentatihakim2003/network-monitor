from ping3 import ping
with open ("devices.txt","r") as file:
    for ip in file:
        ip=ip.strip()
        if not ip : 
            continue 
        response = ping(ip)
        print (ip)
        if response:
            response_ms = round(response * 1000, 2)
            print("✅ Device is online")
            print(f"Response time: {response_ms} ms")
        else:
            print("❌ Device is offline")