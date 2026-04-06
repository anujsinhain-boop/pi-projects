import subprocess

def scan_network():
    result = subprocess.run(
        ["nmap", "-sn", "-PR", "192.168.4.0/24"],
        capture_output=True,
        text=True,
        check=False,
    )
    print(result.stdout)

if __name__ == "__main__":
    scan_network()
