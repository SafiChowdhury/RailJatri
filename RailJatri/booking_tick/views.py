from django.shortcuts import render , redirect
from django.db import connection
from .models import station_name,journey,train_info,ticket_info
from django.contrib.auth.models import User
import sqlite3
def booking_ticket(request):
    name = station_name.objects.all()
    current_user = request.user
    user_name = current_user.username
    if request.method == "POST":
        from12= request.POST.get('from')
        to= request.POST.get('to')
        journey_date = request.POST.get('date')
        chair = request.POST.get('class')
        adult =request.POST.get('adult')
        child = request.POST.get('child')
        temp = int(child) + int(adult)

        ticket = journey(from12=from12,to=to,journey_date=journey_date,adult=adult,child=child,chair=chair,passenger_nm=user_name,total=temp)
        ticket.save()

        return redirect('select_seat')


    return render(request, 'search.html', {'station_name': name})

def seat_select(request):
    current_user= request.user
    user_id = current_user.first_name
    user_name = current_user.username
    user_email= current_user.email
    infos = journey.objects.filter(passenger_nm=user_name).last()
    x = str(infos.to)
    y = str(infos.chair)
    z = int(infos.total)
    train_i = train_info.objects.filter(place=x).last()
    tick = train_info.objects.filter(place=x).filter(chair_class=y).last()
    #    return render(request, 'seat_selection.html',context)

    return render(request,'seat_selection.html',{'first_name':user_id,'email':user_email,'info':infos,'name':train_i,'fare':tick})
# def list_trains(request):
#     if request.method == "POST":
#         if request.session.get('is_logged_in')!="1":
#             return redirect("/" + "?not_logged_in=" + str(0))
#
#
#         fro = request.POST["from"]
#         to = request.POST["to"]
#         date = request.POST["date"]
#         adult = request.POST["adult"]
#         child = request.POST["child"]
#         clas=request.POST["class"]
#         temp=int(child)+int(adult)
#         if temp>4:
#             return redirect("/" + "?max_seat_exceeded=1")
#         request.session["adult"] = str(adult)
#         request.session["child"] = str(child)
#         request.session["total_seats"]=str(temp)
#         request.session["doj"]=str(date)
#         request.session["class"] = clas
#         request.session["from"] = fro
#         request.session["to"] = to
#         global details
#         details={'from':fro,'to':to,'date':date,'adult':adult,'child':child,'class':clas}
#         date=str(date)
#         print(str(date))
#
#         cursor0 = connection.cursor()
#         sql0 ="SELECT TO_CHAR(SYSDATE,'YYYY-MM-DD') FROM DUAL;"
#         cursor0.execute(sql0)
#         result0 = cursor0.fetchall()
#         cursor0.close()
#         for re0 in result0:
#             sdate=str(re0[0])
#         if date==sdate:
#             cursor = connection.cursor()
#             sql = "SELECT TT1.TRAIN_ID,(SELECT NAME FROM TRAIN T1 WHERE T1.TRAIN_ID=TT1.TRAIN_ID) NAME1,TT1.DEPARTURE_TIME,TT2.DEPARTURE_TIME,ROW_NUMBER() Over (ORDER BY TO_TIMESTAMP(LPAD(TT1.DEPARTURE_TIME,4,'0'), 'HH24:MI')) As SN " \
#                   "FROM TRAIN_TIMETABLE TT1,TRAIN_TIMETABLE TT2 " \
#                   "WHERE (TT1.DIRECTION='FROM' AND TT1.STATION_ID=(SELECT STATION_ID FROM STATION WHERE NAME=%s)) AND (TT2.DIRECTION='TO' AND TT2.STATION_ID=(SELECT STATION_ID FROM STATION WHERE NAME=%s)) AND (TT1.TRAIN_ID=TT2.TRAIN_ID) AND TO_DATE(CONCAT(CONCAT(CONCAT(TO_CHAR(SYSDATE, 'YYYY-MM-DD'),' '),TT1.DEPARTURE_TIME),':00'),'YYYY-MM-DD HH24:MI:SS')>SYSDATE " \
#                   "ORDER BY TO_TIMESTAMP(LPAD(TT1.DEPARTURE_TIME,4,'0'), 'HH24:MI');"
#             cursor.execute(sql, [fro, to])
#             result = cursor.fetchall()
#             cursor.close()
#         else:
#             cursor = connection.cursor()
#             sql = "SELECT TT1.TRAIN_ID,(SELECT NAME FROM TRAIN T1 WHERE T1.TRAIN_ID=TT1.TRAIN_ID) NAME1,TT1.DEPARTURE_TIME,TT2.DEPARTURE_TIME,ROW_NUMBER() Over (ORDER BY TO_TIMESTAMP(LPAD(TT1.DEPARTURE_TIME,4,'0'), 'HH24:MI')) As SN " \
#                   "FROM TRAIN_TIMETABLE TT1,TRAIN_TIMETABLE TT2 " \
#                   "WHERE (TT1.DIRECTION='FROM' AND TT1.STATION_ID=(SELECT STATION_ID FROM STATION WHERE NAME=%s)) AND (TT2.DIRECTION='TO' AND TT2.STATION_ID=(SELECT STATION_ID FROM STATION WHERE NAME=%s)) AND (TT1.TRAIN_ID=TT2.TRAIN_ID) " \
#                   "ORDER BY TO_TIMESTAMP(LPAD(TT1.DEPARTURE_TIME,4,'0'), 'HH24:MI');"
#             cursor.execute(sql, [fro, to])
#             result = cursor.fetchall()
#             cursor.close()
#
#         cursor1 = connection.cursor()
#         sql1 = "select NVL((TRUNC(COST*%s)+TRUNC(COST*%s*0.5)),0) " \
#                "FROM COST " \
#                "WHERE STATION_ID=(SELECT STATION_ID from STATION where NAME=%s) AND TO_STATION_ID=(SELECT STATION_ID from STATION where NAME=%s)"
#         cursor1.execute(sql1, [adult,child,fro, to])
#         result1 = cursor1.fetchall()
#         cursor1.close()
#         cursor2 = connection.cursor()
#         sql2 = "select NVL(COST,0) " \
#                "FROM COST " \
#                "WHERE STATION_ID=(SELECT STATION_ID from STATION where NAME=%s) AND TO_STATION_ID=(SELECT STATION_ID from STATION where NAME=%s)"
#         cursor2.execute(sql2, [fro,to])
#         result2 = cursor2.fetchall()
#         cursor2.close()
#         st1=""
#         st2=""
#         st3=""
#         st4=""
#         st5=""
#         st6=""
#         for re2 in result2:
#             st1=int(re2[0])
#             st2=int(re2[0]*decimal.Decimal('0.5'))
#             st3=int(re2[0]*decimal.Decimal('0.8'))
#             st4 = int(re2[0]*decimal.Decimal('0.8')*decimal.Decimal('0.5'))
#             st5= int(re2[0]*decimal.Decimal('0.6'))
#             st6 = int(re2[0]*decimal.Decimal('0.6')*decimal.Decimal('0.5'))
#         fare_list=[]
#         fare_list.append(str(st1))
#         fare_list.append(str(st2))
#         fare_list.append(str(st3))
#         fare_list.append(str(st4))
#         fare_list.append(str(st5))
#         fare_list.append(str(st6))
#         st = ""
#         for re in result1:
#
#             if clas=='SNIGDHA':
#                 st = re[0]
#             elif clas=='S_CHAIR':
#                 st=re[0]*0.8
#             else:
#                 st=re[0]*0.6
#         print(st)
#         if st!="":
#             request.session['vat'] = str(int(st * 0.15))
#             st=st+(st*0.15)
#
#         else:
#             st="0"
#         dict_result = []
#         doj = request.session.get('doj')
#         traincnt=0
#         for r in result:
#             traincnt=traincnt+1
#             TRAIN_ID = r[0]
#             NAME = r[1]
#             departure = r[2]
#             arrival = r[3]
#             sn=r[4]
#             leftright=str(sn%2)
#             delay=(sn-1)*200
#             cursor = connection.cursor()
#             sql = "SELECT 78-COUNT(*) FROM BOOKED_SEAT WHERE TRAIN_ID=%s AND CLASS='SNIGDHA' AND TRUNC(DATE_OF_JOURNEY)= TO_DATE(%s,'YYYY-MM-DD');"
#             cursor.execute(sql, [TRAIN_ID, doj])
#             result = cursor.fetchall()
#             for r in result:
#                 snigdha = r[0];
#             print(snigdha)
#             cursor1 = connection.cursor()
#             sql1 = "SELECT 78-COUNT(*) FROM BOOKED_SEAT WHERE TRAIN_ID=%s AND CLASS='S_CHAIR' AND TRUNC(DATE_OF_JOURNEY)= TO_DATE(%s,'YYYY-MM-DD');"
#             cursor1.execute(sql1, [TRAIN_ID, doj])
#             result1 = cursor1.fetchall()
#             for r1 in result1:
#                 s_chair = r1[0];
#             print(s_chair)
#             cursor2 = connection.cursor()
#             sql2 = "SELECT 78-COUNT(*) FROM BOOKED_SEAT WHERE TRAIN_ID=%s AND CLASS='SHOVAN' AND TRUNC(DATE_OF_JOURNEY)= TO_DATE(%s,'YYYY-MM-DD');"
#             cursor2.execute(sql2, [TRAIN_ID, doj])
#             result2 = cursor2.fetchall()
#             for r2 in result2:
#                 shovan = r2[0];
#             row = {'sn':sn,'lr':leftright,'delay':delay, 'TRAIN_ID': TRAIN_ID, 'NAME': NAME, 'DEPARTURE_TIME': departure, 'ARRIVAL_TIME': arrival,'snigdhaad':fare_list[0],
#                    'snigdhach':fare_list[1],'s_chairad':fare_list[2],'s_chairch':fare_list[3],'shovanad':fare_list[4],'shovanch':fare_list[5],
#                    'snigdhaseat':snigdha,'s_chairseat':s_chair,'shovanseat':shovan}
#             dict_result.append(row)
#         request.session['trains']=dict_result
#         request.session['cost']=str(int(st))
#         request.session['snigdha_fare'] = fare_list
#         return render(request, 'list_trains.html', {'tcount':traincnt, 'trains': dict_result, 'cost': str(int(st)) + '' + ' BDT', 'details': details})
#     else:
#         dict_result=request.session.get('trains')
#         st=request.session.get('cost')
#         return render(request, 'list_trains.html',
#                       {'trains': dict_result, 'cost': str(st) + '' + ' BDT', 'details': details})

def succesful(request):
    return render(request,'successful.html')

def tick_details(request):
    return render(request,'ticket.html')