import os
import shutil
import glob

def backup_python_files():
    os.makedirs('backup', exist_ok=True)
    python_files = glob.glob('*.py')
    for file in python_files:
        shutil.copy(file, os.path.join('backup', file))
        print(f"Backed up: {file}")

backup_python_files()
