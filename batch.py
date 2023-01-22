import os
curr_path = os.path.dirname(__file__)
#print(curr_path)
file_list = os.listdir(curr_path)
#print(file_list)

def get_file_list(path):
    Path = []
    try:
        pathDir = os.listdir(path)
        for allDir in pathDir:
            if os.path.isfile(allDir) and (".wav" in str(allDir)): 
                Path.append(allDir)
    except Exception:
        pass
    return Path;

#print(get_file_list(curr_path));
for file in get_file_list(curr_path):
    os.system('python slicer2.py '+ file + ' --out output')