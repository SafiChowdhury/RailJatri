from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from django.shortcuts import render,redirect
from .models import profile_update
from booking_tick.models import ticket_info,journey


def updateInfo(request):
    current_user = request.user
    user_name = current_user.username
    user_email = current_user.email
    if request.method == "POST":
        frst_nm = request.POST.get('first')
        lst_nm = request.POST.get('last')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        nid_nm = request.POST.get('nid')
        house_nm = request.POST.get('house')
        rd_nm = request.POST.get('road')
        zp_cd = request.POST.get('zip')
        city = request.POST.get('city')
        ph_nmbr = request.POST.get('num1')
        full_name = str(frst_nm)+str(' ')+str(lst_nm)
        u_adrs = str(house_nm)+str(',')+str(rd_nm)+str(',')+str(city)+str(',')+str(zp_cd)
        #old_info = profile_update.objects.filter(us_nm=user_name).delete()
        up_info = profile_update(f_name=frst_nm,l_name=lst_nm,dob=dob,gender=gender,nid_no=nid_nm,h_nm=house_nm,r_nm=rd_nm,zp_cd=zp_cd,city=city,us_nm=user_name,ph_nmbr=ph_nmbr,full_name=full_name,f_add=u_adrs)
        up_info.save()
        return redirect('infoupdate')
    p_det = profile_update.objects.filter(us_nm=user_name).last()

    return render(request,'updateinfo.html',{'det':p_det,'email':user_email})

def changenum(request):
    current_user = request.user
    user_name = current_user.username
    user_email = current_user.email
    if request.method == "POST":
        num1 = request.POST.get('num2')
        num = request.POST.get('num2')
        up_info = profile_update.objects.filter(us_nm=user_name).update(ph_nmbr=num)
        return redirect('changenum')
    p_det = profile_update.objects.filter(us_nm=user_name).last()
    return render(request,'changenum.html',{'det':p_det,'email':user_email})

def journey_details(request):
    current_user = request.user
    user_name = current_user.username
    user_email = current_user.email

    p_det = profile_update.objects.filter(us_nm=user_name).last()
    if request.method == "POST":
        return redirect('tick_det')
    return render(request,'upcoming.html',{'det':p_det,'email':user_email})

def tick_details(request):
    current_user = request.user
    user_name = current_user.username
    infos = ticket_info.objects.filter(passenger_un=user_name).last()
    j_date = journey.objects.filter(passenger_nm=user_name).last()
    return render(request,'ticket.html',{'info': infos,'date': j_date})