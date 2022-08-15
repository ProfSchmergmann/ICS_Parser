from datetime import datetime, timedelta
import xlsxwriter
import string

header = ['Spieltyp',
          'Gegner',
          'Start-Datum',
          'End-Datum\n(Optional)',
          'Start-Zeit',
          'Treffen\n(Optional)',
          'End-Zeit\n(Optional)',
          'Heimspiel',
          'Gelände /\nRäumlichkeiten',
          'Adresse (optional)',
          'Infos zum Spiel',
          'Teilname',
          'Nominierung',
          'Zu-/Absagen bis\n(Stunden vor dem Termin)',
          'Erinnerung zum Zu-/Absagen\n(Stunden vor dem Termin)'
          ]


def write_xlsx(games: list, file_name):
    workbook = xlsxwriter.Workbook(file_name + '.xlsx')
    worksheet = workbook.add_worksheet('Spielplan')
    wrap = workbook.add_format({'text_wrap': True})
    worksheet.set_column('A:O', 20)
    worksheet.set_row(0, 30)
    worksheet.write_row('A1', header, wrap)

    date_format = workbook.add_format({'num_format': 'dd.mm.yyyy'})
    time_format = workbook.add_format({'num_format': 'hh:mm:ss'})

    row = 2
    for game in games:
        worksheet.write('A' + str(row), str(game.typ.value))
        worksheet.write('B' + str(row), game.opponent)
        worksheet.write_datetime('C' + str(row), game.start_date, date_format)
        worksheet.write_datetime('D' + str(row), game.end_date, date_format)
        worksheet.write_datetime('E' + str(row), game.start_time, time_format)
        worksheet.write_datetime('F' + str(row), game.meeting_time, time_format)
        worksheet.write_datetime('G' + str(row), game.end_time, time_format)
        worksheet.write('H' + str(row), game.home_game)
        worksheet.write('I' + str(row), game.terrain)
        worksheet.write('J' + str(row), game.address)
        worksheet.write('K' + str(row), game.info)
        worksheet.write('L' + str(row), game.participation)
        worksheet.write('M' + str(row), game.nomination)
        worksheet.write('N' + str(row), game.accept_decline_hours)
        worksheet.write('O' + str(row), game.accept_decline_hours_reminder)

        row += 1

    workbook.close()
