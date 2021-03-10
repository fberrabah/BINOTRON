
import json
from ast import literal_eval
import doctest
import copy
import functools
import random 
import logging as lg



def create_grp():
    participant = ["Farid", "Marie" , "Phichet" , "Arthur" , "Antoine", "Hatice", "Giovanni", "Mickael", 
    "Rachid", "Julien", "Vivien", "Kevin", "Josephine", "Valentin", "Camille","Tanguy" ]
    nb_part = check_nb_part()

                
    nb_grp = calcul(nb_part)
    x = range(int(nb_part))
    y = range(int(nb_grp))
    list_grp = []
    
    for i in y:
       # import pdb; pdb.set_trace()
        groupe = []
        for i in x:
            used = random.choice(participant)
            groupe.append(used)
            participant.remove(used)

        list_grp.append(groupe)

        if len(participant)< int(nb_part):
            groupe = []
            for item in participant:
                groupe = list_grp[-1]
                groupe.append(item)
                participant.remove(item)

            print("\033[31mVoici les groupes {0}\033[0m".format(list_grp))




def autotest(func):
    globs = copy.copy(globals())
    globs.update({func.__name__: func})
    doctest.run_docstring_examples(
        func, globs, verbose=True, name=func.__name__)
    return func




nom_fichier = 'information_u.json'


def calcul(nb_part):


    nb_grp = 16 // int(nb_part)
    
    return nb_grp



def sav_com(item, lvl, comp):
    with open(nom_fichier, 'w') as fichier:
        json.dump(str({'nom': item, 'Niveau': lvl,'compétence': comp}), fichier)


def read_com():
    with open(nom_fichier, 'r') as fichier:
        information_user = json.load(fichier)
        return information_user
        


def comp(lvl,comp):
    participant = ["Farid", "Marie" , "Phichet" , "Arthur" , "Antoine", "Hatice", "Giovanni", "Mickael", 
    "Rachid", "Julien", "Vivien", "Kevin", "Josephine", "Valentin", "Camille","Tanguy" ]
    comp = ""
    lvl = ""
    comp = input("\033[32m La compétence :\033[0m").lower()
    for item in participant :
        lvl = input("\033[32m Quel est le niveau de " + item + ":\033[0m").lower()
        sav_com(item, lvl, comp)
        information_utilisateur = literal_eval(read_com())
        for (key,valeur) in information_utilisateur.items():
            print(f"{key} est sur {valeur}")
        
 
@autotest

def calcul(nb_part):
    
    """NB only INT
    
    >>> calcul(4)
    4
    """
    return 16 // int(nb_part)




def check_nb_part():

    nb = "0"
    while int(nb) > 8 or int(nb) == 0:
    
        try:
            nb = int(input("\033[32mVeuillez entrer le nombre de personne dans un groupe entre 1 et 8 personnes: \033[0m")) 
 
        except ValueError as e:
            lg.error("Vous n'avez pas saisi de nombre entre 1 et 8 {}".format(e))            # print("Vous n'avez pas saisi de nombre entre 1 et 8")

    nb_part = nb
            
    return nb_part