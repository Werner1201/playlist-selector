import os
import sys
import platform
import subprocess
import shlex
import json


def execute_mpv_command(command):
    sys.stdout.flush()
    _ = subprocess.call(
        command, shell=True)

# TODO: Make this function Read the Json Config File and Print the List and
# Execute mpv with the date from json.


def playlist_seletor():
    escolha = 0
    yturl = "https://www.youtube.com/playlist?"
    command = "mpv --no-video " + yturl
    print("Qual dos estilos, quer escutar ?")
    print("\n1-Rock/PopRock")
    print("\n2-Lofi hip-hop lonley music")
    print("\n3-Eletrónica")
    print("\n4-Aleatório, todas juntas")
    print("\n5-RAP NANA")
    print("\n6-ASMR")
    escolha = int(input("\nDigite: "))
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')
    print("Intruções:" +
          "\n9-0 Abaixa e Aumenta o Volume" +
          "\nP- Pausa a música" +
          "\nEnter-Vai pra próxima música" +
          "\nQ = Fecha o programa\n")
    if escolha == 1:
        commando = shlex.split(
            command + "list=PLiZj_IL8ze6Vp8-5ZgKagH-LuPor6BPic")
        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 2:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6XZkvrrxPO6LGVt1jj8TybQ")

        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 3:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6Visa1jD9zWhwO9og6z6uw_")
        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 4:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6U8rETvvf6DvszB83NQQmo1")
        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 5:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6VbQZdY-kFUpHKaB4qA7q2w")
        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 6:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6Um1PLTpHq8KoLltPJ_m043")

        execute_mpv_command(commando)
        if platform.system() == 'Linux':
            os.system('clear')
        else:
            os.system('cls')
        main()

    if escolha == 0 or escolha > 6:
        os.system("pause")


def config_editing(playlist_tuples):
    aux_tuple = 0
    print("\nEDITING PLAYLIST CONFIG MODE: ")
    name_arr = playlist_tuples[0]
    link_arr = playlist_tuples[1]
    end = False
    while not end:
        print(f"\nConfig Has {len(name_arr)} Entries: ")
        index = 0
        for string in name_arr:
            print(f"Playlist #{index+1}: {string},{link_arr[index]}\n")
            index += 1
        choiceEntry = int(
            input("\nWhich Entry do you want to Edit ? Type Number: "))
        choiceType = int(input(f"\nWhich Type of Entry #{choiceEntry}" +
                               " you want" +
                               " to Edit?" +
                               "\n0-Name, \n1-Link, \n2-Both, \n3-Exit Mode" +
                               "\nChoose: "))
        if choiceType == 3:
            return playlist_tuples
        if choiceType == 2:
            print(
                f"\n#{choiceEntry}- {name_arr[choiceEntry-1]}," +
                f"{link_arr[choiceEntry-1]}" +
                " :")
            aux_line = input("\nEditing: ")
            aux_arr = aux_line.split(",")
            name_arr[choiceEntry-1] = aux_arr[0]
            link_arr[choiceEntry-1] = aux_arr[1]
            aux_tuple = (name_arr, link_arr)
            choiceEnd = int(input("\nDo you want to edit anything else ?" +
                                  " 0-No, 1-Yes: "))
            if choiceEnd == 0:
                return aux_tuple
        if choiceType == 1:
            print(
                f"\n#{choiceEntry}- {name_arr[choiceEntry-1]}," +
                "_____________" +
                " :")
            aux_line = input("\nEditing: ")
            link_arr[choiceEntry-1] = aux_line
            aux_tuple = (name_arr, link_arr)
            choiceEnd = int(input("\nDo you want to edit anything else ?" +
                                  " 0-No, 1-Yes: "))
            if choiceEnd == 0:
                return aux_tuple
        if choiceType == 0:
            print(
                f"\n#{choiceEntry}- _______________," +
                f"{link_arr[choiceEntry-1]}" +
                " :")
            aux_line = input("\nEditing: ")
            name_arr[choiceEntry-1] = aux_line
            aux_tuple = (name_arr, link_arr)
            choiceEnd = int(input("\nDo you want to edit anything else ?" +
                                  " 0-No, 1-Yes: "))
            if choiceEnd == 0:
                return aux_tuple
        if choiceType > 3:
            return playlist_tuples


def create_json_config_file(configjson: json):
    filejson = open("config.json", "wt")
    filejson.writelines(configjson)
    filejson.close()
    return 0


def create_json_config(configdict: dict) -> json:
    configjson = json.dumps(configdict)
    return configjson


def config_dict_template(names_arr, links_arr) -> dict:
    configdict = {}
    i = 0
    for name in names_arr:
        configdict[name] = links_arr[i]
        i += 1
    return configdict


def comma_verify(text):
    if "," in text:
        return text
    else:
        return 0


def split_array(string_arr) -> tuple:
    names_arr = []
    links_arr = []
    for string in string_arr:
        aux_arr = string.split(",")
        names_arr.append(aux_arr[0])
        links_arr.append(aux_arr[1])
    return (names_arr, links_arr)


def jsonToTuple() -> tuple:
    name_arr = []
    link_arr = []
    jsonFile = open("config.json", "rt")
    jsonDict = json.load(jsonFile)
    for n in jsonDict:
        name_arr.append(n)
        link_arr.append(jsonDict[n])
    return (name_arr, link_arr)


def choose_playlists():
    print("Choose the playlists names and their links to"
          + "be added to your config!")
    print("\nPlease type the name and separate the link with a comma ',' :")
    string_arr = []
    final = False
    index = 0
    while not final:
        buffer_values = input(f"\nPlaylist #{index}:")
        if comma_verify(buffer_values) == 0:
            print("Error you did not use any comma ',' ! Try Again.")
            continue
        string_arr.append(buffer_values)
        index += 1
        aux_final = int(
            input("Want to Continue ? 0 to stop, 1 to continue: ")
        )
        if aux_final == 0:
            final = True
            aux_tuple = split_array(string_arr)
            aux_last_edit = int(
                input("Do you want to Edit anything ? 1-Yes,0-No: "))
            if aux_last_edit == 1:
                aux_tuple = config_editing(aux_tuple)
            create_json_config_file(create_json_config(
                config_dict_template(aux_tuple[0], aux_tuple[1])))
            print("Configurations Concluded!")

        if aux_final == 1:
            final = False
            print("Configurations Saved!\n")


def new_user_workflow():
    print("Oh a new user! Welcome to Playlist Selector!\n")
    choose_playlists()
    return 0


def old_user_options():
    print("\nSelect What you want to do:")
    print("\n1 - Listen to the Playlists. ")
    print("\n2 - Edit Playlists")
    print("\n0 - Exit Program")
    choice = int(input("\nChoose: "))
    if choice == 0:
        os.system("pause")
    if choice == 1:
        playlist_seletor()
    if choice == 2:
        aux_tuple = config_editing(jsonToTuple())
        create_json_config_file(create_json_config(
            config_dict_template(aux_tuple[0], aux_tuple[1])))


def old_user_workflow():
    print("Welcome Back!")
    old_user_options()
    return 0


def checking_workflow():
    if os.path.exists('config.json') is True:
        old_user_workflow()
    else:
        new_user_workflow()


def main():
    checking_workflow()


main()
