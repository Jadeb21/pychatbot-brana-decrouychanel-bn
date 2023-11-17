import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
def print_list(l):
    print(l)

def extraire_nom(l):
    list_nom=[]
    for i in l:
        list_nom.append(i[11:-4])
    return list_nom