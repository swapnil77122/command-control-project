

---

# IP Scanner

## Overview

This Python script allows you to scan a specified IP address for open ports using the `nmap` library. It scans the first 1024 ports and outputs the results, including the state of each port.

## Requirements

- Python 3.x
- `nmap` library

## Installation

1. **Install Python:** Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Nmap:** Make sure you have Nmap installed on your machine. You can download it from [nmap.org](https://nmap.org/download.html).

3. **Install the `python-nmap` library:**
   You can install the `nmap` library using pip:
   ```bash
   pip install python-nmap
   ```

## Usage

1. Open the script in your preferred Python editor or IDE.

2. Replace the `target_ip` variable with the IP address you want to scan.

   ```python
   target_ip = '192.168.1.1'  # Change this to your target IP address
   ```

3. Run the script. It will scan the specified IP address for open ports in the range of 1 to 1024.

```bash
python ip_scanner.py
```

## Output

The script will print the scan results to the console, including:

- Protocol used (TCP/UDP)
- Open ports and their states (open/closed)

Example output:
```
Scanning 192.168.1.1...
Scan results for 192.168.1.1:
Protocol : tcp
Port : 22    State : open
Port : 80    State : open
...
```

## Error Handling

The script includes basic error handling to catch exceptions during the scanning process. If the target IP address is unreachable or an error occurs, it will print an appropriate message.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Nmap](https://nmap.org/) - Network exploration tool and security/port scanner
- [python-nmap](https://pypi.org/project/python-nmap/) - A Python library to access Nmap

---

Feel free to modify any sections to better suit your project or preferences!
![image](https://github.com/user-attachments/assets/a6e46fce-146b-406a-95a6-1c33db53c4c5)
