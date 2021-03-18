#! /usr/bin/env python3
# coding: utf-8
from controller import *


if __name__=='__main__':
    
   
    print("\033[32m\n----------------------------------------\n\033[0m")
    print('\033[32mBienvenue dans votre application.\033[0m')
    print("\033[32m\n----------------------------------------\n\033[0m")

    """loop who answer what do you want and answer we need"""
    choix=""  
    while choix != "q":
        choix = input("\033[33m\n(s) Pour créer des groupes.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
        if choix == "s": 
            
            A = ""
            lvl = ""
            while A != "o" and  A != "n":
                A = input("\033[32m Souhaitez-vous faire des groupes par compétence. (o/n) : \033[0m").lower() 

                if A == "n" :
                    create_grp()
                
                
                if A == "o" :
                    comp(lvl,comp)

                
            
        if choix == "q":
            print("A bientôt.")