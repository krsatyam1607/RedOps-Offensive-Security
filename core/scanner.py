import subprocess
import argparse
import os
from datetime import datetime

# Create a unique folder to store results
def create_output_dir(target):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dirname = f"reports/{target.replace(':', '').replace('/', '')}_{timestamp}"
    os.makedirs(dirname, exist_ok=True)
    return dirname

def run_nmap(target, outdir):
    print("[*] Running Nmap...")
    output_file = f"{outdir}/nmap.txt"
    
    # Extract IP or hostname from URL
    stripped_target = target.replace("http://", "").replace("https://", "").split('/')[0]
    
    command = ["nmap", "-sC", "-sV", "-oN", output_file, stripped_target]
    subprocess.run(command)

def run_nikto(target, outdir):
    print("[*] Running Nikto...")
    output_file = f"{outdir}/nikto.txt"
    command = ["nikto", "-h", target, "-output", output_file]
    subprocess.run(command)

def run_gobuster(target, outdir):
    print("[*] Running Gobuster...")
    output_file = f"{outdir}/gobuster.txt"
    wordlist = "/usr/share/wordlists/dirb/common.txt"  # Ensure this exists
    command = ["gobuster", "dir", "-u", target, "-w", wordlist, "-o", output_file]
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="RedOps Scanner Module")
    parser.add_argument("-t", "--target", required=True, help="Target IP or URL")
    parser.add_argument("-m", "--modules", choices=["nmap", "nikto", "gobuster", "all"], default="all", help="Modules to run")
    args = parser.parse_args()

    outdir = create_output_dir(args.target)

    if args.modules == "nmap" or args.modules == "all":
        run_nmap(args.target, outdir)

    if args.modules == "nikto" or args.modules == "all":
        run_nikto(args.target, outdir)

    if args.modules == "gobuster" or args.modules == "all":
        run_gobuster(args.target, outdir)

    print(f"\n[✔] Scan complete. Reports saved in: {outdir}")

if __name__ == "__main__":
    main()