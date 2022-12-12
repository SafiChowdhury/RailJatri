from django.shortcuts import render , redirect
from django.db import connection
from .models import station_name,journey,train_info,ticket_info
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.contrib.auth.models import User
import sqlite3
def render_to_pdf(template_src,context_dist={}):
    template = get_template(template_src)
    html = template.render(context_dist)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None

def booking_ticket(request):
    name = station_name.objects.all()
    current_user = request.user
    user_name = current_user.username
    if request.method == "POST":
        from12= request.POST.get('from')
        to= request.POST.get('to')
        journey_date = request.POST.get('date')
        chair = request.POST.get('class')
        total =request.POST.get('passenger')
        ticket = journey(from12=from12,to=to,journey_date=journey_date,chair=chair,passenger_nm=user_name,total=total)
        ticket.save()

        return redirect('select_seat')


    return render(request, 'search.html', {'station_name': name})

def seat_select(request):
    current_user= request.user
    user_id = current_user.first_name
    user_name = current_user.username
    user_email= current_user.email
    infos = journey.objects.filter(passenger_nm=user_name).last()
    x = str(infos.from12)
    xx = str(infos.to)
    y = str(infos.chair)
    z = int(infos.total)
    train_i = train_info.objects.filter(place=xx).last()
    tick = train_info.objects.filter(place=x).filter(to=xx).filter(chair_class=y).last()
    dep_tym= tick.time_train
    arrv_tym= tick.arraival_time
    t_name= str(tick.name_train)
    t_num= int(tick.train_number)
    cost = int(tick.fare)
    price = cost*z
    ticket = ticket_info(cost=price,passenger_name=user_id,train_name=t_name,dest_from=x,dest_to=xx,train_id=t_num,chair_class=y,total_seat=z,arrv_tym=arrv_tym,dep_tym=dep_tym,passenger_un=user_name)
    ticket.save()
    if request.method == "POST":
        return redirect('pay_select')

    return render(request,'seat_selection.html',{'first_name':user_id,'email':user_email,'info':infos,'name':train_i,'fare':price})



def pay_cat(request):
    current_user = request.user
    user_name = current_user.username
    cash = ticket_info.objects.filter(passenger_un=user_name).last()
    if request.method == "POST":
        return redirect('bkash_pay')

    return render(request,'payment selection.html',{'tk':cash})
def bkash(request):
    current_user = request.user
    user_name = current_user.username
    cash = ticket_info.objects.filter(passenger_un=user_name).last()
    if request.method == "POST":
        return redirect('success')
    return render(request,'bkash_payment.html',{'tk':cash})


def succesful(request):
    current_user = request.user
    user_name = current_user.username
    infos = ticket_info.objects.filter(passenger_un=user_name).last()

    if request.method == "POST":
        return redirect('tick_det')
    return render(request, 'successful.html', {'info': infos})


# class ViewPDF(View):
#     def get(self, request, *args, **kwargs):
#         current_user = request.user
#         user_name = current_user.username
#         infos = ticket_info.objects.filter(passenger_un=user_name).last()
#         j_date = journey.objects.filter(passenger_nm=user_name).last()
#         data={
#             'info': infos,
#             'date': j_date,
#         }
#         pdf = render_to_pdf('ticket.html',data)
#         return HttpResponse(pdf, content_type='application/pdf')

def tick_details(request):
    current_user = request.user
    user_name = current_user.username
    infos = ticket_info.objects.filter(passenger_un=user_name).last()
    j_date = journey.objects.filter(passenger_nm=user_name).last()
    return render(request,'ticket.html',{'info': infos,'date': j_date})