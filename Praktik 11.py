import glob

def scan_files():
    suspicious_keyword = "# VIRUS SAYS HI!"
    python_files = glob.glob('*.py')
    
    for file in python_files:
        with open(file, 'r', errors='ignore') as f:
            content = f.read()
            if suspicious_keyword in content:
                print(f"[WARNING] Suspicious content found in: {file}")
            else:
                print(f"[OK] {file} is clean.")

scan_files()
