
import subprocess
import platform

def ping_host(host):
    current_os = platform.system().lower()

    #Set correct parameters (-n for windows/edge, -c for rest)
    param = "-n" if current_os == "windows" else "-c"
    command = ["ping", param, "4", host]
    print(f"Pinging {host}...")
    response = subprocess.call(command)

    if response == 0:
        print(f"\n{host} is UP.")
    else:
        print(f"\n{host} is DOWN.")

target = input("Enter IP: ")
ping_host(target)