import re

ip ="192.168.0.169"

validip = re.match(r"^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})",ip)

print(validip.group())