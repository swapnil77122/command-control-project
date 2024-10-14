# Importing the required library
import nmap

def scan_ip(ip_address):
    # Create a new Nmap PortScanner object
    nm = nmap.PortScanner()

    # Run a scan on the specified IP address
    print(f"Scanning {ip_address}...")
    try:
        nm.scan(ip_address, '1-1024')  # Scanning the first 1024 ports

        # Check if the target was found in the scan results
        if ip_address in nm.all_hosts():
            print(f"Scan results for {ip_address}:")
            for proto in nm[ip_address].all_protocols():
                print(f"Protocol : {proto}")
                lport = nm[ip_address][proto].keys()
                for port in sorted(lport):
                    print(f"Port : {port}\tState : {nm[ip_address][proto][port]['state']}")
        else:
            print(f"No results found for {ip_address}. It may be unreachable or down.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example IP address (replace with the target IP address you want to scan)
    target_ip = '192.168.1.1'  # Change this to your target IP address
    scan_ip(target_ip)
