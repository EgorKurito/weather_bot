import sqlite3

from SQLighter import SQLighter

'''con = sqlite3.connect("weather.db")
cur = con.executescript("""
        insert into weather(city)
        values (
            'Kazan,RU'
        );
""")
'''
db = SQLighter('weather.db')
db.add_row('Moscow,RU')

rowsnum  = db.count_rows()
print(rowsnum)
