from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.db import connection
from create_acc.models import passenger
import sqlite3

def registration(request):

    return render(request, 'registration.html')

def saveEnquiry(request):
    if request.method == "POST":
        first_name= request.POST.get('frst')
        last_name = request.POST.get('last')
        date_birth = request.POST.get('dob')
        gender =request.POST.get('gender')
        email = request.POST.get('email')
        Nid_No = request.POST.get('nid')
        houseNo = request.POST.get('houseno')
        roadNo = request.POST.get('roadno')
        zipCode = request.POST.get('zip')
        city = request.POST.get('city')
        mobile_No = request.POST.get('contact')
        password =request.POST.get('password')
        confirm_pass = request.POST.get('confirmpass')
        
    #     en=passenger(first_name=first_name,last_name=last_name, date_birth= date_birth, gender= gender,email=email,Nid_No=Nid_No,house_no=houseNo,roadNo=roadNo, zipCode= zipCode,town=city,mobile_No=mobile_No,password=password,confirm_pass=confirm_pass)
        
    #     en.save()
    #     # return render(request, 'registration.html')
    #     return render(request, 'login.html')
    # else:
    #     return render(request,'registration.html')

    
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        # sql1 = "SELECT email FROM create_acc_passenger WHERE email=%s"
        cur.execute("SELECT email FROM create_acc_passenger WHERE email='?'",(email))
        result1 = cur.fetchall()
        cur.close()

        if (result1):
            print('1')
            msg = "This E-mail ID is already registered."
            return render(request, 'registration.html', {"status": msg})
        else:
            print('2')
            cur2 = con.cursor()
            # sql2 = "SELECT Nid_No FROM create_acc_passenger WHERE Nid_No=%s;"
            cur2.execute("SELECT Nid_No FROM create_acc_passenger WHERE Nid_No='Nid_No'")
            result2 = cur2.fetchall()
            cur2.close()

            if (result2):
                print('3')
                msg = "This NID number is already registered."
                return render(request, 'registration.html', {"status": msg})
            else:
                print('4')
                cur3 = con.cursor()
                # sql3 = "SELECT mobile_No FROM create_acc_passenger WHERE mobile_No='+880'||%s;"
                cur3.execute("SELECT mobile_No FROM create_acc_passenger WHERE mobile_No='+880'||'mobile_No'")
                result3 = cur3.fetchall()
                cur3.close()

                if (result3):
                    print('5')
                    msg = "This contact number is already registered."
                    return render(request, 'registration.html', {"status": msg})
                else:
                    print('6')
                    pw_hash = make_password(password)
                    print(pw_hash)

                    f = open("info.txt", "a+")
                    f.write(email + " " + password)
                    f.write("\n")
                    f.close()

                    cur = con.cursor()
                    # sql = "INSERT INTO create_acc_passenger VALUES(NVL((SELECT MAX(passenger_id)+1 FROM create_acc_passenger),1),%s,%s,%s,TO_DATE(%s,'YYYY-MM-DD'),CONCAT('+880',%s),%s,%s,%s,%s,%s,%s,%s);"
                    cur.execute("INSERT INTO create_acc_passenger (first_name,last_name, date_birth, gender,email,Nid_No,house_no,roadNo, zipCode,town,mobile_No,password,confirm_pass) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(first_name,last_name, date_birth, gender,email,Nid_No,houseNo,roadNo, zipCode,city,mobile_No,password,confirm_pass))
                    con.commit()
                    cur.close()
                    # en.save()
                    # fullname = first_name + " " + last_name
                    # return redirect("/login" + "?user=" + fullname)
                    # return render(request, 'login.html')
    return render(request, 'login.html')
    # #     en=passenger(first_name=first_name,last_name=last_name, date_birth= date_birth, gender= gender,email=email,Nid_No=Nid_No,house_no=houseNo,roadNo=roadNo, zipCode= zipCode,town=city,mobile_No=mobile_No,password=password,confirm_pass=confirm_pass)
    # #     en.save()
    # #     return render(request, 'login.html')
    # # else:
    # #     return render(request,'registration.html')