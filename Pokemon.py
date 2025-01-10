#Michael Stroup
#Pokemon
#11/19
#Init
import random
pokemon_level = 0
pokemon_name = "Bulbusaur"
#stats record
wins = 0
losses = 0
boss_fights = 0
#Pictures/Ascii art
def venusaur():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠶⠶⠶⢦⣄⠀⠀⠀⠀⢀⣀⣤⠤⠴⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣋⣁⣀⣀⣀⠀⠀⠀⣀⣴⣤⣾⢷⡾⠛⣾⡿⢻⣤⣤⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠖⠚⠋⠉⠉⠉⠉⠉⠉⠉⠉⢉⣛⡳⣿⣿⠿⠙⠷⠟⠷⠋⠻⠾⠻⣿⣷⠶⠖⠒⠒⠒⠒⠒⠻⠿⠦⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⢀⣠⣤⡴⠶⠛⠛⠋⠉⠉⠉⠛⠛⠲⢦⣄⠀⠀⢀⣠⣤⠶⠿⠓⠒⠶⠶⠶⠦⣤⣤⣀⡀⠀⠀⠀⠉⠙⠓⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⠀⣀⣤⣶⠾⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣷⣴⣿⣉⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⢦⣄⡀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⢀⣠⡶⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⣀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⡾⠛⠁⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⢦⣌⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠸⣧⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣽⠆⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠦⣤⣀⣀⣤⠀⠀⠀⢠⣾⡃⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡼⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣉⣻⠶⣤⣤⣿⣿⣿⣿⣿⣿⣏⢀⣤⡈⣡⣙⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣿⡆⠀⣰⣦⣤⣴⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣀⣴⡶⠶⣶⣿⣟⠛⢿⣯⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢻⠷⠓⠲⣶⡤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣠⡿⠷⠄⠈⠉⠛⣀⣠⣽⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣄⣀⠙⠛⠉⠿⠷⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣴⠛⠓⠚⠛⠂⠀⠀⠰⠶⠛⠛⣻⠏⠉⠹⠿⣿⣿⡛⠛⠻⠿⠿⠿⣿⣉⣤⡴⠞⠀⠀⠀⢸⣿⡇⠀⠀⠀⢀⣀⠉⢻⣿⠿⠛⠛⠛⣛⣽⣿⣿⠃⠉⢿⣿⡿⣏⠛⠻⣶⣶⠾⠛⠻⠷⢤⣄⡀⠀⠀⠀⠀
    ⠀⢀⣈⣭⠿⠛⠀⠀⠀⠀⣠⡆⠀⠀⠀⠋⣶⠀⠀⢀⣽⣿⣿⣦⣄⠀⠀⠀⢿⣋⣁⣤⣴⠖⠀⠀⢸⣿⠀⠀⠀⠀⠀⠙⠿⣿⡿⠀⠀⣠⣾⣿⣿⣿⣿⣄⠀⠀⠉⠃⠀⠀⠀⢻⣆⠀⠀⠀⠀⢠⣈⡉⠛⠶⣤⡄
    ⢸⡏⠁⣀⠀⢀⣴⡇⠀⢠⣿⠁⠀⡄⠀⣼⣿⠀⢀⣿⣟⣿⣿⣻⣿⣷⡄⠀⠘⢻⣟⠋⢀⣠⣤⠀⠈⠁⠀⠀⠸⣶⣄⣶⣤⡿⠁⠀⠾⠿⣿⣯⣿⣿⣤⣿⣧⡀⠘⣿⣆⠀⣤⣀⠹⣷⣄⠀⣦⣈⠙⢿⣷⡾⠋⠀
    ⠘⠛⢿⣏⣴⣿⣏⣀⣠⡟⣿⣤⣼⣷⣶⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠻⠾⣿⡿⢁⡄⠀⠀⠀⢤⣀⠘⣿⠿⠟⠀⢀⣀⣀⡀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢷⣬⣿⣷⣤⡼⠷⠀⠀
    ⠀⠀⠀⠀⠁⠀⠉⠉⠉⣴⢏⣿⣿⣿⣿⣿⠟⠛⢻⣿⠟⠀⠀⠀⢴⡛⠉⠁⠀⢀⠀⠀⠻⢶⣿⠃⢀⣿⡄⢈⣿⠟⠋⠀⡀⠀⠀⠀⣉⣽⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠉⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡾⠿⠋⢹⣿⡏⠀⢀⡾⠁⠀⠀⠀⠀⣾⠛⣶⣤⣀⠸⡇⠀⠀⠀⠙⠷⢾⠟⠿⠟⠁⠀⠀⢸⡇⣀⣤⣾⣿⢹⡇⠀⠀⠀⠀⠙⣿⡛⠋⠀⢻⣿⣿⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠁⠀⠀⢸⡿⠀⠀⢾⡁⠀⠀⠀⠀⠀⠹⣄⠙⠛⣹⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠛⠿⣤⣉⣀⠼⠁⠀⣀⠀⠀⣸⡇⠀⠀⠈⣿⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢰⣟⢀⣀⠀⠀⢸⡇⠀⠀⠘⢷⡀⠀⠲⣦⣀⡀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⠾⠋⠀⣰⡟⠀⠀⠀⠀⣿⡏⠀⠀⠀⢀⣸⡏⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣤⣦⣾⡇⠀⠀⠀⠈⠳⢶⣤⣾⣽⣿⣟⣿⣶⡶⠶⢦⣤⣀⠀⢠⡀⠀⠀⠀⣤⠀⣠⣤⡶⠖⠛⢿⣿⣿⣽⠛⣠⣦⣴⠾⠋⠀⠀⠀⠀⠀⣿⠁⠀⢀⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⠛⢿⡄⢹⣿⣿⡀⠀⠀⠀⠉⠛⠳⠶⠶⠶⠶⠶⠛⠋⠀⠀⠀⠀⢸⣿⣿⢃⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⣫⡾⠃⠀⠀⠀⠀⠀⠀⣤⠀⠀⣸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣿⣿⣿⢿⣿⣧⡺⣧⡄⠀⠀⢀⣀⡀⠉⠻⣮⣝⣿⣿⣿⣤⣤⣀⣀⣀⣀⣀⣀⣀⣤⣴⣿⣿⡿⣫⣾⠛⣁⣄⠀⠀⠀⠀⠀⠛⠋⠀⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠈⠉⠙⠒⠋⠙⢷⣄⠀⠀⠀⠘⠛⠁⠀⠀⣠⣿⡿⢿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣽⡾⠋⠀⠀⠿⠷⠀⠀⠀⠀⠀⠀⠀⣠⡿⠳⠞⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⠃⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢉⡟⠀⠀⠀⠀⠀⠀⠀⢰⣤⣶⠆⢀⣴⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⢿⣿⡟⢿⣿⣿⣏⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣹⡆⢢⡾⠻⣧⠀⠀⣴⢶⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠉⠙⠻⣇⣠⡿⠷⠾⣧⣈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
def ivysaur():
    print("""
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟨🟨⬛🟥🟨🟨🟥⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟥🟥🟥⬛⬛⬛🟥🟥🟨🟨🟥⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛⬛🟨🟨🟨⬛⬛⬛⬛🟥🟥⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥⬛⬛🟥🟥⬛⬛🟨🟨⬛🟥🟨⬛⬛⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟨🟨🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛🟩⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛🟨🟨🟥🟥🟥⬛⬜⬜
    ⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬛⬜⬜
    ⬜⬜⬜⬛🟦⬛⬛🟩⬛🟩🟩⬛⬛⬛🟥🟥🟥⬛⬛⬛⬛⬛⬛🟩⬛⬛⬜
    ⬜⬜⬜⬛🟦🟦⬛⬛⬛🟩⬛⬛🟩🟩⬛⬛⬛🟩⬛🟩🟩🟩⬛⬛🟩🟩⬛
    ⬜⬜⬜⬛🟦🟦🟦🟦🟦⬛⬛⬛⬛🟩🟩⬛🟩⬛⬛🟩⬛🟩🟩⬛🟩⬛⬛
    ⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛🟦⬛⬛🟩⬛🟩⬛🟩⬛
    ⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦⬛⬛🟩⬛🟩⬛
    ⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦⬛🟦🟦🟦⬛⬛⬛⬜
    ⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟥🟥⬛🟦🟦🟦⬛🟦🟦🌫️⬛⬜⬜
    ⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛🟦⬛🟦⬛🟦🌫️⬛⬜⬜⬜
    ⬜⬛🟦🟦🟦🟦🟦🟦🟦⬛🟥⬜🟦🟦🟦🟦🟦🟦🟦⬛⬜⬛⬛⬜⬜⬜⬜
    ⬜⬛⬛🟦🟦🟦🟦🟦⬛⬜⬜🟦🟦🟦🟦⬛🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦🟦🟦⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦⬜⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬜🟦⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜""")
def bulbusaur():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀
    ⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀
    ⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀
    ⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀
    ⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈
    ⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰
    ⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀
    ⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀
    ⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀
    ⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀""")
#Function
def battle():
    global pokemon_level
    global pokemon_name
    global wins
    global losses
    print("Battling!")
    #random outcome of battle
    outcome = random.randint(1,2)
    if outcome == 1:
        print("Oh No! " + pokemon_name + " lost the battle.")
        print("They did not level up.")
        losses = losses + 1
    elif outcome == 2:
        print(pokemon_name + " Won!")
        print("They leveled up twice!")
        pokemon_level = pokemon_level + 1
        evolve()
        pokemon_level = pokemon_level + 1
        wins = wins + 1
def train():
    global pokemon_level
    global pokemon_name
    #Level up Message changes based on pokemon evolution
    print("Nice work, " + pokemon_name + ". They did " + str(random.randint(5,20)) + " push ups today!")
    pokemon_level = pokemon_level + 1
    print(pokemon_name + " Leveled Up!")
def rest():
    global pokemon_level
    global pokemon_name
    global losses
    global wins
    global boss_fights
    #Show all stats, vary based on pokemon evolution and level
    print(pokemon_name + " is resting. Here are their stats.")
    print("Name: " + pokemon_name)
    print("Level: " + str(pokemon_level))
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Boss Attempts: " + str(boss_fights))
    #Display Ascii art
    if pokemon_name == "Bulbusaur":
        bulbusaur()
    elif pokemon_name == "Ivysaur":
        ivysaur()
    elif pokemon_name == "Venusaur":
        venusaur()
def evolve():
    global pokemon_level
    global pokemon_name
    #Check if pokemon is ready to evolve
    if pokemon_level == 5:
        print(pokemon_name + " evolved!")
        pokemon_name = "Ivysaur"
        print("Now they are " + pokemon_name + "!")
    if pokemon_level == 15:
        print(pokemon_name + " evolved!")
        pokemon_name = "Venusaur"
        print("Now they are " + pokemon_name + "!")
def boss():#final battle, better chance at higher level, only available after level 20
    while True:
        print("You can now continue training or challenge the Boss!!")
        print("""1.Train
2.Gym Battle
3.Rest(display info)
4.Quit
5. Boss Battle""")
        activity = int(input("Type activity: 1/2/3/4/5"))
        if activity == 1:
            train()
            evolve()
        elif activity == 2:
            battle()
            evolve()
        elif activity == 3:
            rest()
        elif activity == 4:
            print("Thanks for playing!")
            break
        elif activity == 5:#Boss fight code
            print(pokemon_name + " is challenging the boss!")
            global boss_fights
            boss_fights = boss_fights + 1
            boss = random.randint(1,100)
            boss = boss - 15
            boss = boss + pokemon_level
            if boss <= 90:
                print("Oh No! " + pokemon_name + " lost the boss battle.")
                print(pokemon_name + " was this close: "  + str(boss) + "/100")
            elif boss > 90:
                print(pokemon_name + " defeated the boss! it was this close: " + str(boss) + "/100")
                print(pokemon_name + "'s journey is complete. Here are their final stats.")
                print("Name: " + pokemon_name)
                print("Level: " + str(pokemon_level))
                print("Wins: " + str(wins))
                print("Losses: " + str(losses))
                print("Boss Attempts: " + str(boss_fights))
                if pokemon_name == "Bulbusaur":
                    bulbusaur()
                elif pokemon_name == "Ivysaur":
                    ivysaur()
                elif pokemon_name == "Venusaur":
                    venusaur()
                print("Thanks for playing!")
                break
def game():
    print("Welcome to Pokemon Evolution")
    while True:
        print("Choose todays activity")
        if pokemon_level < 20:
            print("""1.Train
2.Gym Battle
3.Rest(display info)
4.Quit""")
            activity = int(input("Type activity: 1/2/3/4"))
            if activity == 1:
                train()
                evolve()
            elif activity == 2:
                battle()
                evolve()
            elif activity == 3:
                rest()
            elif activity == 4:
                print("Thanks for playing!")
                break
        elif pokemon_level >= 20:
            boss()
            break
#Main
game()
