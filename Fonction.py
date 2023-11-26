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
        if i[-5]<=chr(90):
            list_nom.append(i[11:-5])
        else :
            list_nom.append(i[11:-4])

    for nom in list_nom:
        if list_nom.count(nom)>1:
            list_nom.remove(nom)

    list_prenom=[]

    for nom in list_nom:

        if nom == "Chirac":
            list_prenom.append("Jacques Chirac")
        elif nom == "Giscard dEstaing":
            list_prenom.append("Valéry Giscard dEstaing")
        elif nom == "Hollande":
            list_prenom.append("François Hollande")
        elif nom == "Macron":
            list_prenom.append("Emmanuelle Macron")
        elif nom == "Mitterrand":
            list_prenom.append("François Mitterrand")
        elif nom == "Sarkozy":
            list_prenom.append("Nicolas Sarkozy")


    return list_prenom








def convert_file_lower_case(files_names,directory):
    for file_name in files_names :
        # Création chemin d'acces du fichier
        input_file_path = directory + '/' + file_name
        # Ouverture fichier
        with open(input_file_path,'r') as content:
            #Création chemin ou sera rangé le fichier modifier
            output_file_path = "./cleaned" + '/' + file_name + "copie.txt"
            #Ouverture fichie copie
            with open(output_file_path, 'w') as copy:
                # modification des majusucles en miniscule
                line = content.readline()
                while line != '':
                    line_mod =''
                    for car in line :
                        if car >= 'A' and car <= 'Z':
                            car = chr(ord(car)+ 32 )
                        line_mod += car
                    # Ligne transformer en minuscule réecrite dans la copie
                    copy.write(line_mod)
                    line = content.readline()


def replacementpunctuation(files_names):
    for file_name in files_names:
        input_file_path = "./cleaned" + '/' + file_name + "copie.txt"
        with open(input_file_path, 'r') as f1:
            content = f1.read()
            # définition des caractères de ponctuations
            punctuation_character = ',;:.?!""()[]*/'
            text_clean = ''
            # Verification des caractères un par un
            for car in content:
                if car in punctuation_character:
                    text_clean += ' '
                elif car == "'" or car == "-":
                    text_clean += ' '
                else:
                    text_clean += car
        with open(input_file_path, "w") as file_clean:
            file_clean.write(text_clean)  # Réecriture du texte sans ponctuaction dans le même fichier