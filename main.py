from input import read_games
from game import game
from output import write_xlsx


if __name__ == '__main__':
    ics_file = input("Name of input.ics file?")
    final_home_team = input("Name of the home team?")
    xlsx_file = input("Name of output.xlsx file?")

    write_xlsx(read_games(ics_file + '.ics', final_home_team), xlsx_file)
    quit()
