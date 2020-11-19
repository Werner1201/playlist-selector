import os
import sys
import platform
import subprocess
import shlex
import json


def execute_mpv_command(command):
    _ = subprocess.Popen(
        command, shell=False,
        stdout=sys.stdout, stderr=sys.stderr).communicate()


def seletor():
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
          "\nCtrl+C = Fecha o programa\n")
    if escolha == 1:
        commando = shlex.split(
            command + "list=PLiZj_IL8ze6Vp8-5ZgKagH-LuPor6BPic")
        execute_mpv_command(commando)
        main()

    if escolha == 2:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6XZkvrrxPO6LGVt1jj8TybQ")

        execute_mpv_command(commando)
        main()

    if escolha == 3:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6Visa1jD9zWhwO9og6z6uw_")
        execute_mpv_command(commando)
        main()

    if escolha == 4:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6U8rETvvf6DvszB83NQQmo1")
        execute_mpv_command(commando)
        main()

    if escolha == 5:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6VbQZdY-kFUpHKaB4qA7q2w")
        execute_mpv_command(commando)
        main()

    if escolha == 6:
        commando = shlex.split(
            command +
            "list=PLiZj_IL8ze6Um1PLTpHq8KoLltPJ_m043")
        execute_mpv_command(commando)
        main()

    if escolha == 0 or escolha > 6:
        os.system("pause")


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
            create_json_config_file(create_json_config(
                config_dict_template(aux_tuple[0], aux_tuple[1])))
            print("Configurations Concluded!")

        if aux_final == 1:
            final = False
            print("Configurations Saved!\n")


def new_user_workflow():
    return 0


def main():
    return 0
# seletor()


main()
