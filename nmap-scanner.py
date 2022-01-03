import nmap
from debug import debug

scanner = nmap.PortScanner()

ip = input()

(scanner.scan(ip, "1-1024", "-v"))
debug(scanner[ip]["tcp"].keys())