import os
from Fonction import *

directory = "./speeches"
extention = "txt"
l=list_of_files(directory, extention)
print_list(l)
list_nom = extraire_nom(l)
print(list_nom)
#convertir_en_minuscules('C:/Users/maely/PycharmProjects/MyFirstChatbot/speeches/Nomination_Chirac1.txt')

convert_file_lower_case(l,directory)
replacementpunctuation(l)