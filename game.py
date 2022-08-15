from datetime import datetime, timedelta
from enum import Enum


class Typ(Enum):
    HOME_GAME = 'Spiel'
    AWAY_GAME = 'Auswärtsspiel'


class game:
    def __init__(self,
                 typ: Typ,
                 opponent,
                 start_date: datetime,
                 end_time: datetime,
                 address):
        self.typ = typ
        self.opponent = opponent
        self.start_date = start_date.date()
        self.end_date = end_time.date()
        self.start_time = start_date.time()
        self.meeting_time = (start_date - timedelta(hours=1)).time()
        self.end_time = end_time.time()
        if typ == Typ.HOME_GAME:
            self.home_game = 'ja'
        else:
            self.home_game = 'nein'
        self.terrain = 'Halle'
        self.address = address
        self.info = ''
        self.participation = 'Spieler müssen zusagen'
        self.nomination = 'Trainer, Spieler'
        self.accept_decline_hours = 24 * 3
        self.accept_decline_hours_reminder = 24 * 4
