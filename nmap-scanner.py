import nmap

scanner = nmap.PortScanner()

ip = input()

(scanner.scan(ip, "1-1024", "-v"))
print(scanner[ip]["tcp"].keys())