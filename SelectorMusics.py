import os
import sys
import platform
import subprocess
import shlex
import json
from typing import TypeVar


# Setting to let the function return both types
T = TypeVar('T', int, str)


def execute_mpv_command(command: list) -> None:
    """
    This function let's the user see the MPV terminal "ui" and controll it
    And Refreshes the stdout before showing it.
    """
    sys.stdout.flush()
    _ = subprocess.call(
        command, shell=True)


def clean_prompt() -> None:
    """
    Auxiliary Function
    It's use is to check the user's system os and selects the correct system
    clear command in the cli.
    """
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def playlist_seletor() -> int:
    """
    Core Function
    It's use is where the name comes from
    It allows the user to reproduce their youtube playlists
    Reading the config.json it shows the list and lets the user select
    the playlist they want to play.
    Runs in a loop to let the user select other playlists if they want to.
    """
    playlists = jsonToTuple()
    name_arr = playlists[0]
    link_arr = playlists[1]
    choice = 0
    program = "mpv --no-video "
    end = False
    while not end:
        clean_prompt()
        print("Which of the playlists do you want to listen?")
        for name in name_arr:
            print(f"\n{name_arr.index(name)+1}- {name}")

        choice = int(input("\nChoose: "))
        clean_prompt()
        print("Intructions:" +
              "\n9-0-: Lowers and Inscreases the Volume" +
              "\nP-: Stops the Music" +
              "\nEnter-: Next Music" +
              "\nQ-: Closes Playlist\n")

        command = shlex.split(program + link_arr[choice-1])
        execute_mpv_command(command)
        clean_prompt()
        if int(input("Do you want to listen more ? 1 - Yes, 0 - No: ")) == 0:
            end = True
            return 0
        else:
            end = False


def config_editing(playlist_tuples: tuple) -> tuple:
    """
    Optional Function
    It's use is multiple inside and outside
    It was adapted to work to new config needs
    If the user wants to edit some thing inside their first config
    Without having to save before editing this function allows it
    But it allows to edit already saved files via the auxiliary fucntion
    JsonToTuple since this function only recieves tuples and returns tuples
    """
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


def create_json_config_file(configjson: json) -> int:
    """
    Third Sequence config Function
    Just writes the json to the config.json file.
    """
    filejson = open("config.json", "wt")
    filejson.writelines(configjson)
    filejson.close()
    return 0


def create_json_config(configdict: dict) -> json:
    """Second Sequence config function here it just converts dict to json"""
    configjson = json.dumps(configdict)
    return configjson


def config_dict_template(names_arr: list, links_arr: list) -> dict:
    """
    First of the Sequence config Functions
    it gets the lists from parameters and uses them to create and dict
    So it can be read by create_json_config
    """
    configdict = {}
    i = 0
    for name in names_arr:
        configdict[name] = links_arr[i]
        i += 1
    return configdict


def comma_verify(text: str) -> T:
    """
    Verification Function
    It verifies if inside the text string there's a comma
    text parameter comes from choose_playlists() input of the new playlists
    """
    if "," in text:
        return text
    else:
        return 0


def split_array(string_arr: list) -> tuple:
    """
    Auxiliary function
    It's purpose is to get an list of strings divided by commas
    and separte it into 2 lists, one of names and the other of links
    and return both inside an tuple.
    """
    names_arr = []
    links_arr = []
    for string in string_arr:
        aux_arr = string.split(",")
        names_arr.append(aux_arr[0])
        links_arr.append(aux_arr[1])
    return (names_arr, links_arr)


def jsonToTuple() -> tuple:
    """
    Auxiliary function
    It's function is to read the config file saving it at jsonFile var and
    separate the dict into 2 lists inside an tuple.
    """
    name_arr = []
    link_arr = []
    jsonFile = open("config.json", "rt")
    jsonDict = json.load(jsonFile)
    for n in jsonDict:
        name_arr.append(n)
        link_arr.append(jsonDict[n])
    return (name_arr, link_arr)


def choose_playlists() -> int:
    """
    Here is the workflow to create and config.json for a first time user
    it uses an string array to read the values of the user divided by a comma
    at the end of the editions and after varios checks if the user wants to
    Edit anything it calls the sequence of fucntions to create the config.json
    create_json_config_file() <- create_json_config() <- config_dict_template()
    """

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
            return 0

        if aux_final == 1:
            final = False
            print("Configurations Saved!\n")


def new_user_workflow() -> int:
    """
    Here is the workflow where there's no config.json
    it returns an int to the controller in the checking_workflow()
    """
    print("Oh a new user! Welcome to Playlist Selector!\n")
    if choose_playlists() == 0:
        return 0


def old_user_options() -> bool:
    """
    Here is Where the user can choose what they want the program to do
    this function is inside an pseudo loop of its own
    if statements 1 and 2 call the function it self so only the
    if statement 0 can end the program.
    """
    print("\nSelect What you want to do:")
    print("\n1 - Listen to the Playlists. ")
    print("\n2 - Edit Playlists")
    print("\n0 - Exit Program")
    choice = int(input("\nChoose: "))
    if choice == 0:
        return True
    if choice == 1:
        if playlist_seletor() == 0:
            clean_prompt()
            return old_user_options()
    if choice == 2:
        aux_tuple = config_editing(jsonToTuple())
        create_json_config_file(create_json_config(
            config_dict_template(aux_tuple[0], aux_tuple[1])))
        clean_prompt()
        return old_user_options()


def old_user_workflow():
    """
    The primary loop of the old user workflow
    here is it is controlled by the return of the old_user_options
    """
    print("Welcome Back!")
    retorno = False
    while not retorno:
        retorno = old_user_options()
    return 0


def checking_workflow():
    """
    Here there's the main loop for the workflow of the program
    It checks if there's and config.json
    True = follows to old_user_workflow()
    False = follows to new_user_workflow()
    """
    while True:
        if os.path.exists('config.json') is True:
            return old_user_workflow()
        else:
            new_user_workflow()


def main():
    checking_workflow()


main()
