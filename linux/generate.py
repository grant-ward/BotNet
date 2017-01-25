import os
import ipaddress,time


print("Welcome! this script will configurate the agent with your configurations!")

if os.path.isfile("settings.py"):
    while True:
        delete = input("\nDo you wanna clean your old configuration? for a new configuration?\n [Y/n] ")
        if delete in ("Y","y","Yes","yes","YES"):
            os.system("echo '' > settings.py")
            break
        if delete in ("N","n","no","No","NO"):
            print("closing...")
            exit()
        else:
            print("Invalid answer!")
else:
    print("\n\nCreating a configurantion file..")
    time.sleep(.5)
    os.system("touch settings.py")
    print("File created! going to configuration phase!")
script = open("settings.py","w")

while True:
    ip = input("Wich IP?\n :")
    try:
        validate_ip = ipaddress.ip_network(ip, strict=False)
        script.write("host="+"'"+str(ip)+"'"+"\n")
        break
    except:
        print("INVALID IP!")
while True:
    try:
        port = int(input("Wich port?\n :"))
        script.write("port="+str(port)+"\n")
        break
    except:
        print("INVALID PORT!")

while True:
    while True:
        tkinter = input("Do you wanna a message in execution of agent?\n[Y/N] :")
        if tkinter in ("y","Y","yes","YES","Yes"):
            script.write("tkinter=True\n")
            while True:
                type_message = input("What type?\nALERT[A]   INFO[I]   ERROR[E]\n: ")
                if type_message in ("e","E","A","a","i","I"):
                    if type_message in ("e","E"):
                        script.write("type=ERROR")
                        break
                    if type_message in ("A","a"):
                        script.write("type=ALERT")
                        break
                    if type_message in ("I","i"):
                        script.write("type=INFO")
                        break
                else:
                    print("Invalid type!")
        if tkinter in ("n","N","no","NO","No") or type_message != None:
            break
        else:
            print("Invalid answer!")
    break
print("Configuration fineshed!\nUse Compile.py to make a .exe or compile yourself with Pyinstaller!")

