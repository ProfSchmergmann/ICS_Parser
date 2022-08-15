from icalendar import Calendar, Event, vCalAddress, vText
from game import game, Typ


def read_games(input_file_name, final_home_team) -> list[game]:
    e = open(input_file_name, encoding="utf-8")
    ecal = Calendar.from_ical(e.read())
    games = []
    for component in ecal.walk():
        if component.name == "VEVENT":

            summary = component.get("summary")
            home_team = summary.split("-")[0].strip()
            away_team = summary.split("-")[1].split(",")[0].strip()
            if home_team == final_home_team:
                typ = Typ.HOME_GAME
            else:
                typ = Typ.AWAY_GAME
                away_team = home_team

            start_date = component.decoded("dtstart")
            end_date = component.decoded("dtend")

            address = component.get("location").replace("\\", "")

            games.append(game(typ, away_team, start_date, end_date, address))

    return games
