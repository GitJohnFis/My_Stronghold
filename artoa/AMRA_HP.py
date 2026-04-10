
import speedtest
import time

st = speedtest.Speedtest()

print("Testing...") 
down = st.download() / 10 ** 6         #10_000_000  Convert to Mbps
up = st.upload() / 10 ** 6             #10_000_000  Convert to Mbps

print(f"Down Speed: {down:.2f} Mbps")
print(f"Up Speed: {up:.2f} Mbps")

with open("speed_log.txt", "a") as f:
    f.write(f"{time.ctime()}: Downtime = {down:.2f} Mbps\n")
    f.write(f"{time.ctime()}: Uptime = {up:.2f} Mbps\n")