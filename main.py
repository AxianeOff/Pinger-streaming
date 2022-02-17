import os
import time
from simple_colors import *

list_films = ["grizox.com", "itzor.com", "redzor.com", "badrip.com", "zifub.com", "tivmy.com", "saypap.com", "wavob.com", "okvop.com", "rikmod.com", "dibrav.com", "vadraz.com", "sardip.com", "zawox.com", "davrip.com", "zavrol.com", "bambip.com", "voplav.com", "pijpa.com", "nidroy.com", "vagdi.com", "lakmoa.com", "choupox.com", "abdov.com", "extrabb.com", "ridzov.com", "justdaz.com", "framib.com", "zaniob.com", "bovrom.com", "rigrov.com", "obniv.com", "evdod.com", "ivrom.com",  "ovtok.com", "poblom.com", "tratov.com", "mildip.com", "bovmi.com", "grizox.com", "difiam.com", "flazto.com", "dadroz.com", "netdov.com", "waklov.com", "pilmov.com", "flozor.com", "kempox.com", "kremov.com"]
list_animes = ["animeovf.fr", "vostfree.tv", "toonanime.tv", "toonanime.cc", "otakufr.co", "gum-gum-streaming.com", "french-anime.com", "wakanim.tv", "adkami.com", "jetanimes.com", "mavanimes.co", "voiranime.com", "gogoanime.fi", "neko-sama.fr", "gvostfr.com", "stream-vf.co", "bananimes.com", "manganimes.net"]


def pingfilms(list):
    # parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    print("\nSouhaitez vraiment lancer le processus de ping des sites de films ?")
    input_choix = input("Tapez Y ou N : ")
    if input_choix == "Y":
        print("\n")
        for i in list:
            str_host = str(i)
            command = f'ping -n 1 {str_host}>nul'
            response = os.system(command)
            if response == 0:
                print(green(f'{str_host} ON'))
            else:
                print(red(f'{str_host} OFF'))
    elif input_choix == "N":
        menu()
    else:
        print("<ERREUR> Veuillez entrer 'Y', 'N' ou 'exit()' <ERREUR>")
        pingfilms(list)
    time.sleep(0.75)
    return menu()


def pinganimes(list):
    # parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    print("\nSouhaitez vraiment lancer le processus de ping des sites d'animés ?")
    input_choix = input("Tapez Y ou N : ")
    if input_choix == "Y":
        print("\n")
        for i in list:
            str_host = str(i)
            command = f'ping -n 1 {str_host}>nul'
            response = os.system(command)
            if response == 0:
                print(green(f'{str_host} ON'))
            else:
                print(red(f'{str_host} OFF'))
    elif input_choix == "N":
        menu()
    else:
        print("<ERREUR> Veuillez entrer 'Y', 'N' ou 'exit()' <ERREUR>")
        pingfilms(list)
    time.sleep(0.75)
    return menu()


def ping():
    input_ping = input("Veuillez taper l'adresse que vous souhaitez ping : ")
    command = f'ping -n 1 {input_ping}'
    response = os.system(command)
    if response == 0:
        print("Ping terminé")
        time.sleep(1.5)
        menu()
    else:
        print("\n<ERREUR> Veuillez insérer une adresse correcte <ERREUR>")
        time.sleep(0.75)
        ping()


def menu():
    print("""
        - 1 - Ping
        - 2 - Ping liste sites de streaming de films
        - 3 - Ping liste sites de streaming d'animés
                                                                            by AxianeOff ;)
    """)
    input_choix = input("Veuillez séléctionner un numéro parmis ceux présentés : ")
    if input_choix == "1":
        ping()
    elif input_choix == "2":
        pingfilms(list_films)
    elif input_choix == "3":
        pinganimes(list_animes)


menu()
