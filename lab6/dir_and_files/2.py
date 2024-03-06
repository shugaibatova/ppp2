
import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"The path exists.")
    else:
        print(f"The path does not exist.")
        return
    
    if os.access(path, os.R_OK):
        print(f"The path is readable.")
    else:
        print(f"The path is not readable.")
        
    if os.access(path, os.W_OK):
        print(f"The path is writable.")
    else:
        print(f"The path is not writable.")

path = ""
check_path_access(path)