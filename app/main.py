from ping3 import ping

ip = input("Enter an IP address: ")

response = ping(ip)

if response:
    response_ms = round(response * 1000, 2)
    print("✅ Device is online")
    print(f"Response time: {response_ms} ms")
else:
    print("❌ Device is offline")