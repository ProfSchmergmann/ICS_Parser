# ICS_Parser

This is a simple project to parse .ics files to .xlsx files which suit the needs of adding games to player plus.
The .ics files can be taken from [here](https://www.basketball-bund.net/index.jsp?Action=101&liga_id=37392) where you just can download the ics file.
It is important to first choose from which league you want to have the games and also which team you're playing in.

## Using instructions

You can use this code by just executing it, 
- typing in the name of the ics file which you downloaded before and which is located in the same folder, 
- then you have to input your team name and 
- finally you can choose how the output file should be called.

## Used packages 

I have used the following packages inside this project, which can be installed using pip.

- [datetime](https://pypi.org/project/DateTime/)
- [enum](https://pypi.org/project/enum/)
- [icalendar](https://pypi.org/project/icalendar/)
- [string](https://docs.python.org/3/library/string.html)
- [xlsxwriter](https://pypi.org/project/XlsxWriter/)