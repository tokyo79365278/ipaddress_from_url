import socket

def get_ip_address(url):
  try:
    hostname = url.split("//")[1].split("/")[0]
    ip_address = socket.gethostbyname(hostname)
    return ip_address
  except:
    return ""

urlinput = input("url: ")
url = (urlinput)
ip_address = get_ip_address(url)
print(f"{ip_address}")
