from django.shortcuts import render
from django.db import connection
#from booking_tick.models import station_name

import sqlite3
def booking_ticket(request):

    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    sql = "SELECT name FROM booking_tick_station_name"
    cur.execute(sql)
    result = cur.fetchall()


    dict = []
    for r in result:
        NAME = r[0]
        row = {'name': NAME}
        dict.append(row)
    con.commit()
    cur.close()
    return render(request,'search.html')

def seat_select(request):
    return render(request,'seat_selection.html')

def succesful(request):
    return render(request,'successful.html')

def tick_details(request):
    return render(request,'ticket.html')