""" Used to deal with the different versions of files"""
import os
import re
def get_next_version(work_path : str, asset_name : str):
    files =  os.listdir(work_path)
    v = []
    for f in files :
        x = re.search(r"v[0-9][0-9][0-9]$",f)
        if x :
            v.append(int(x.group(1)))
    if v :
        nxt_vers = max(v) + 1
    else :
        nxt_vers = 1
    
    return (asset_name+ "_v"+str(nxt_vers)+".ma")
    
