import os
import sys
import platform
import subprocess
import shlex


def execute_mpv_command(command):

    process = subprocess.Popen(
        command, shell=False,
        stdout=sys.stdout, stderr=sys.stderr).communicate()
# process = subprocess.run(
#     command, stdout=subprocess.PIPE, shell=True, text=True)
# print(process.stdout)
# while True:
#     line = process.stdout
#     if process.returncode == 0:
#         print(process.returncode)
#         break
#     print(line)


# def read_mpv_command(command):
#     for path in execute_mpv_command(command):
#         print(path)


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


def main():
    seletor()


main()
