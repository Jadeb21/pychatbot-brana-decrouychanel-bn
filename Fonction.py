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
        if i[-5]<chr(90):
            list_nom.append(i[11:-5])
        else:
            list_nom.append(i[11:-4])
    for nom in list_nom :
        if list_nom.count(nom)>1:
            list_nom.remove(nom)
    if nom == "Chirac":
        print("Jacques")
    if nom == "Giscard dEstaing":
        print("Valéry")
    if nom == "Hollande":
        print("François")
    if nom == "Macron":
        print("Emmanuelle")
    if nom == "Mitterrand":
        print("François")
    if nom == "Sarcozy":
        print("Nicolas")
    return list_nom

def minucule(l):
    for line in list_of_files :
        for letter in line:
          letter = ord(letter)
            if letter > chr(97):
                letter = ord(letter) - 32
                print(letter)