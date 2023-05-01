from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.http import Http404
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


# from .send_m import SendMSG

# Create your views here.
def index(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')
    user_message_model = apps.get_model('pages', 'user_message')


    x = {
        'month_donations':donation_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month).count(),
        'last_month_donations':donation_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = (datetime.today().month-1)).count(),
        'all_donations':donation_model.objects.all().count(),

        'month_beneficiary':beneficiary_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month).count(),
        'last_month_beneficiary':beneficiary_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = (datetime.today().month-1)).count(),
        'all_beneficiary':beneficiary_model.objects.all().count(),

        'delivery_points':delivery_point_model.objects.all().count(),
        'items':item_model.objects.all().count(),

        'unreaded_messages':user_message_model.objects.filter(readed = False).count(),
        'title':'الصفحة الرئيسية',

    }
    return render(request, 'admin_panel/pages/index.html',x)

def beneficiary(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    if request.method == "POST":
        data = request.POST
        registrar = registrar_model.objects.get(id = 1)
        clothes_accept = True if data["clothes_needed_type"] != 0 else False
        study_supplies_accept = True if data["study_supplies_needed_type"] != 0 else False
        clothes_needed_type = None if data["clothes_needed_type"] == 0 else data["clothes_needed_type"]
        study_supplies_needed_type = None if data["study_supplies_needed_type"] == 0 else data["study_supplies_needed_type"]
        long = "%.6f" % float(data['long'])
        lat = "%.6f" % float(data['Lat'])
        beneficiary_model.objects.create(name=data['name'],phone_num=data['phone_num'],id_ps=data['id_ps'],address=data['address'],long=long,Lat=lat,registrar=registrar,need_scale=data['need_scale'],clothes_accept=clothes_accept,study_supplies_accept=study_supplies_accept,study_supplies_needed_type=study_supplies_needed_type,clothes_needed_type=clothes_needed_type)
        # beneficiary_model.objects.create(name=data['name'],phone_num=data['phone_num'],id_ps=data['id_ps'],address=data['address'],long=float(data['long']),Lat=float(data['Lat']),registrar=registrar,need_scale=data['need_scale'],clothes_accept=clothes_accept,study_supplies_accept=study_supplies_accept,study_supplies_needed_type=study_supplies_needed_type,clothes_needed_type=clothes_needed_type)

    day_beneficiary = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_beneficiary = beneficiary_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_beneficiary)
        data_as = data.get('data_as')

    x = {
        'beneficiaries': beneficiary_model.objects.all().order_by('-entry_date','id'),
        'day_beneficiary':day_beneficiary,
        'data_as':data_as,
        'title':'المستفيدين',

    }
    return render(request, 'admin_panel/pages/beneficiary.html',x)


def donation(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')
            
    day_donations = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_donations = receipt_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_donations)
        data_as = data.get('data_as')


    x = {
        'donations': receipt_model.objects.all(),
        'day_donations':day_donations,
        'data_as':data_as,
        'title':'التبرعات',

    }
    return render(request, 'admin_panel/pages/donation.html',x)

def delivery_point(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    if request.method == "POST":
        data = request.POST
        admin = User.objects.get(id = data['user'])
        long = "%.6f" % float(data['long'])
        lat = "%.6f" % float(data['Lat'])
        delivery_point_model.objects.create(name=data['name'],type=data['type'],Lat=lat,long=long,address=data['address'],user=admin)

    day_delivery_points = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_delivery_points = delivery_point_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_delivery_points)
        data_as = data.get('data_as')

    x = {
        'admins_ac':User.objects.all(),
        'delivery_points': delivery_point_model.objects.all().order_by('-entry_date','id'),
        'day_delivery_points':day_delivery_points,
        'data_as':data_as,

        'title':'نقاط التبرع',

    }
    return render(request, 'admin_panel/pages/delivery_point.html',x)

def delivery_point_admin(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    delivery_point_admins = []
    for user in User.objects.all():
        try :
            d = delivery_point_model.objects.get(user = user)
            delivery_point_admins.append((user,d))
        except ObjectDoesNotExist:
            pass
            



    x = {
        'delivery_point_admins': delivery_point_admins,

        'title':'مديري نقاط التبرع',

    }
    return render(request, 'admin_panel/pages/delivery_point_admin.html',x)

def item(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    if request.method == "POST":
        data = request.POST

        item_model.objects.create(name=data['name'],img=data['img'])

    day_item = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_item = item_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_item)
        data_as = data.get('data_as')

    x = {
        'items': item_model.objects.all().order_by('-entry_date','id'),
        'day_item':day_item,
        'data_as':data_as,

        'title':'العناصر',

    }
    return render(request, 'admin_panel/pages/item.html',x)

def item_desire(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    if request.method == "POST":
        data = request.POST

        beneficiary = beneficiary_model.objects.get(id=data["beneficiary"])
        item = item_model.objects.get(id=data["item"])
        item_desire_model.objects.create(item_c=item,beneficiary_c=beneficiary,desire_scale=data['desire_scale'])

    day_items_desire = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_items_desire = item_desire_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_items_desire)
        data_as = data.get('data_as')

    x = {
        'items_desire': item_desire_model.objects.all().order_by('-entry_date','id'),
        'items': item_model.objects.all().order_by('-entry_date','id'),
        'beneficiaries': beneficiary_model.objects.all().order_by('-entry_date','id'),
        'day_items_desire':day_items_desire,
        'data_as':data_as,

        'title':'تمنايات العناصر',

    }
    return render(request, 'admin_panel/pages/item_desire.html',x)


def item_demand(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    if request.method == "POST":
        data = request.POST

        item_demand_model.objects.create(item_c=item,beneficiary_c=beneficiary,desire_scale=data['desire_scale'])

    day_items_demand = None
    data_as = None
    if request.method == "GET" and 'data_as' in request.GET:
        data = request.GET
        day_items_demand = item_demand_model.objects.filter(entry_date__year = data.get('data_as')[:4], entry_date__month = data.get('data_as')[5:7], entry_date__day = data.get('data_as')[8:10]).order_by('-entry_date','-id')
        print(day_items_demand)
        data_as = data.get('data_as')

    x = {
        'item_demands': item_demand_model.objects.all().order_by('-entry_date','id'),
        'items': item_model.objects.all().order_by('-entry_date','id'),
        'beneficiaries': beneficiary_model.objects.all().order_by('-entry_date','id'),
        'day_items_demand':day_items_demand,
        'data_as':data_as,

        'title':'طلبات اضافة العناصر',

    }
    return render(request, 'admin_panel/pages/item_demand.html',x)


def monthly_graphic_report(request):
    delivery_point_model = apps.get_model('pages', 'delivery_point')
    item_model = apps.get_model('pages', 'item')
    item_desire_model = apps.get_model('pages', 'item_desire')
    donation_model = apps.get_model('pages', 'donation')
    message_model = apps.get_model('pages', 'message')
    receipt_model = apps.get_model('pages', 'receipt')
    registrar_model = apps.get_model('pages', 'registrar')
    beneficiary_model = apps.get_model('pages', 'beneficiary')
    item_demand_model = apps.get_model('pages', 'item_demand')

    month_beneficiary = beneficiary_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month)
    month_beneficiary_daily = []
    for i in range(1,32):
        i_day = 0
        for beneficiary in month_beneficiary:
            if beneficiary.entry_date.day == i:
                i_day+=1
        month_beneficiary_daily.append(i_day)
    
    month_items = item_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month)
    month_items_daily = []
    for i in range(1,32):
        i_day = 0
        for item in month_items:
            if item.entry_date.day == i:
                i_day+=1
        month_items_daily.append(i_day)

    month_items_desire = item_desire_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month)
    month_items_desire_daily = []
    for i in range(1,32):
        i_day = 0
        for item in month_items_desire:
            if item.entry_date.day == i:
                i_day+=1
        month_items_desire_daily.append(i_day)


    # delivery_point_list = []
    # chosed_id = []
    # delivery_point_list_names = []
    # for delivery_point in delivery_point_model.objects.all():
    #     i_times = 0
    #     for donation in month_donations:
    #         if donation.delivery_point_c.id == delivery_point.id:
    #             i_times += 1
    #     if i_times:
    #         delivery_point_list_names.append(delivery_point.name)
    #         chosed_id.append(delivery_point.id)
    #         delivery_point_list.append([delivery_point.name,i_times])

    # others_delivery_point_list = donation_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month).exclude(id__in = chosed_id)
    
    # delivery_point_list.append(["اخرى",others_delivery_point_list.count()])
    # delivery_point_list_names.append("اخرى")

    # def takeSecond(elem):
    #     return elem[1]
    
    # delivery_point_list.sort(key=takeSecond)
 
 
    month_donations = donation_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = datetime.today().month)
    month_donation_daily = []
    for i in range(1,32):
        i_day = 0
        for donation in month_donations:
            if donation.entry_date.day == i:
                i_day+=1
        month_donation_daily.append(i_day)

    last_month_donations = donation_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = (datetime.today().month-1))
    last_month_donation_daily = []
    for i in range(1,32):
        i_day = 0
        for donation in last_month_donations:
            if donation.entry_date.day == i:
                i_day+=1
        last_month_donation_daily.append(i_day)
    x = {
        'month_donations':month_donations.count(),
        'month_donation_daily':month_donation_daily,
        'last_month_donation_daily':last_month_donation_daily,
        'last_month_donations':last_month_donations.count(),
        'all_donations':donation_model.objects.all().count(),

        'month_beneficiary':month_beneficiary.count(),
        'month_beneficiary_daily':month_beneficiary_daily,
        'last_month_beneficiary':beneficiary_model.objects.filter(entry_date__year = datetime.today().year,entry_date__month = (datetime.today().month-1)).count(),
        'all_beneficiary':beneficiary_model.objects.all().count(),

        'delivery_points':delivery_point_model.objects.all().count(),
        
        'items':item_model.objects.all().count(),
        'month_items':month_items.count(),
        'month_items_daily':month_items_daily,

        'month_items_desire':month_items_desire.count(),
        'month_items_desire_daily':month_items_desire_daily,


        'title':'البيان الاسبوعي البياني',

    }
    return render(request, 'admin_panel/pages/monthly_graphic_report.html',x)


def message(request):
    user_message_model = apps.get_model('pages', 'user_message')



    if request.method == "GET" and 'read' in request.GET:
        data = request.GET
        message = user_message_model.objects.get(id = data['id'])
        message.readed = True
        message.save()

    x = {

        'messages':user_message_model.objects.all().order_by('readed'),
        'title':'الرسائل',

    }
    return render(request, 'admin_panel/pages/message.html',x)

