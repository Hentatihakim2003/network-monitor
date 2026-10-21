from datetime import datetime
with open("test.log", "a") as file:
    file.write("192.168.1.1\n")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
file.close()