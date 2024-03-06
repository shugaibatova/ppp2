
import os
path = ""
def isExist(path):
    if os.path.exists(path):
        os.remove(path)
        return "File deleted"
    else:
        return "File is not exists"
    
print(isExist(path))