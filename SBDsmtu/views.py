
from django.contrib.auth import views as auth_views
from .views import *
from django.shortcuts import render,redirect
from .models import Purchase, UserProfile, User, Role
from django.http import JsonResponse,HttpResponseNotAllowed
from .parserV2 import *
from django.http import HttpResponse  
import json
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator, Page,PageNotAnInteger, EmptyPage
from .forms import *
from datetime import datetime
from django.utils.text import slugify
import pandas as pd
from django.db import models
from django.db.models import Count
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required,user_passes_test
import psycopg2
import csv
import datetime
import os


# Create your views here.


def index(request):
    return render(request, 'base.html',{'user': request.user})

# def purchase_list(request):
#     purchases = Purchase.objects.all()
#     return render(request, 'purchase_list.html', {'purchases': purchases})


# def search_purchase(request):
#     keyword = request.GET.get('keyword', '')
#     purchases = Purchase.objects.filter(PurchaseName__icontains=keyword)
#     return render(request, 'search_results.html', {'purchases': purchases, 'keyword': keyword})
# Страница фильтроВВ
# def filter_purchase(request):
#     form = PurchaseForm(request.POST)
#     keyword = request.GET.get('keyword', '')
#     filter_criteria = request.GET.get('filter_criteria', '')
#     min_price = request.GET.get('min_price', '')
#     max_price = request.GET.get('max_price', '')

#     # Начнем с QuerySet, который не возвращает ничего
#     purchases = Purchase.objects.all()

#     if keyword:
#         # Используем Q-объект для фильтрации по ключевому слову
#         purchases = purchases.filter(Q(PurchaseName__icontains=keyword))  # Замените OtherField на поле, по которому хотите выполнить поиск

#     if min_price and max_price:
#         # Используем Q-объект для фильтрации по диапазону цен
#         purchases = purchases.filter(
#             Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
#         )
    

#     if filter_criteria == 'price_asc':
#         # Если выбрана сортировка по цене (по возрастанию), упорядочим результат
#         purchases = purchases.order_by('InitialMaxContractPrice')
#     elif filter_criteria == 'price_desc':
#         # Если выбрана сортировка по цене (по убыванию), упорядочим результат
#         purchases = purchases.order_by('-InitialMaxContractPrice')
#     elif filter_criteria == 'date_asc':
#         # Если выбрана сортировка по дате (по возрастанию), упорядочим результат
#         purchases = purchases.order_by('PlacementDate')
#     elif filter_criteria == 'date_desc':
#         # Если выбрана сортировка по дате (по убыванию), упорядочим результат
#         purchases = purchases.order_by('-PlacementDate')


#         # Создайте объект Paginator с вашим QuerySet и количеством записей на странице
#     paginator = Paginator(purchases, 1)  # Например, по 10 записей на странице

#     # Получите номер страницы из запроса или используйте 1 по умолчанию
#     page_number = request.GET.get('page')
#     if page_number is None:
#         page_number = 1

#     try:
#         # Получите объект страницы с номером page_number
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         # Если номер страницы не является целым числом, покажите первую страницу
#         page = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы находится за пределами диапазона страниц, покажите последнюю страницу
#         page = paginator.page(paginator.num_pages)


#     return render(request, 'filter_results.html', {
#         'purchases': page,
#         'keyword': keyword,
#         'filter_criteria': filter_criteria,
#         'min_price': min_price,
#         'max_price': max_price,
#         'form': form
#     })
# def filter_purchase(request):
#     form = PurchaseForm(request.POST)
#     keyword = request.GET.get('keyword', '')
#     filter_criteria = request.GET.get('filter_criteria', '')
#     min_price = request.GET.get('min_price', '')
#     max_price = request.GET.get('max_price', '')

#     # Начнем с QuerySet, который не возвращает ничего
#     purchases = Purchase.objects.all()

#     if keyword:
#         # Используем Q-объект для фильтрации по ключевому слову
#         purchases = purchases.filter(Q(PurchaseName__icontains=keyword))  # Замените OtherField на поле, по которому хотите выполнить поиск

#     if min_price and max_price:
#         # Используем Q-объект для фильтрации по диапазону цен
#         purchases = purchases.filter(
#             Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
#         )
    

#     if filter_criteria == 'price_asc':
#         # Если выбрана  , упорядочим результат
#         purchases = purchases.order_by('InitialMaxContractPrice')
#     elif filter_criteria == 'price_desc':
#         # Если выбрана сортировка по цене (по убыванию), упорядочим результат
#         purchases = purchases.order_by('-InitialMaxContractPrice')
#     elif filter_criteria == 'date_asc':
#         # Если выбрана сортировка по дате (по возрастанию), упорядочим результат
#         purchases = purchases.order_by('PlacementDate')
#     elif filter_criteria == 'date_desc':
#         # Если выбрана сортировка по дате (по убыванию), упорядочим результат
#         purchases = purchases.order_by('-PlacementDate')


#         # Создайте объект Paginator с вашим QuerySet и количеством записей на странице
#     paginator = Paginator(purchases, 1)  # Например, по 10 записей на странице

#     # Получите номер страницы из запроса или используйте 1 по умолчанию
#     page_number = request.GET.get('page')
#     if page_number is None:
#         page_number = 1

#     try:
#         # Получите объект страницы с номером page_number
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         # Если номер страницы не является целым числом, покажите первую страницу
#         page = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы находится за пределами диапазона страниц, покажите последнюю страницу
#         page = paginator.page(paginator.num_pages)


#     return render(request, 'filter_results.html', {
#         'purchases': page,
#         'keyword': keyword,
#         'filter_criteria': filter_criteria,
#         'min_price': min_price,
#         'max_price': max_price,
#         'form': form
#     })
# def filter_purchase(request):
#     form = PurchaseForm(request.POST)
#     keyword = request.GET.get('keyword', '')
#     filter_criteria = request.GET.get('filter_criteria', '')
#     min_price = request.GET.get('min_price', '')
#     max_price = request.GET.get('max_price', '')
#     start_date = request.GET.get('start_date', '')
#     end_date = request.GET.get('end_date', '')

#     purchases = Purchase.objects.all()

#     if keyword:
#         purchases = purchases.filter(Q(PurchaseName__icontains=keyword))

#     if min_price and max_price:
#         purchases = purchases.filter(
#             Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
#         )

#     if start_date and end_date:
#         purchases = purchases.filter(
#             PlacementDate__gte=start_date, PlacementDate__lte=end_date
#         )

#     if filter_criteria == 'price_asc':
#         purchases = purchases.order_by('InitialMaxContractPrice')
#     elif filter_criteria == 'price_desc':
#         purchases = purchases.order_by('-InitialMaxContractPrice')
#     elif filter_criteria == 'date_asc':
#         purchases = purchases.order_by('PlacementDate')
#     elif filter_criteria == 'date_desc':
#         purchases = purchases.order_by('-PlacementDate')

#     paginator = Paginator(purchases, 10)
#     page_number = request.GET.get('page', 1)

#     try:
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         page = paginator.page(1)
#     except EmptyPage:
#         page = paginator.page(paginator.num_pages)

#     return render(request, 'filter_results.html', {
#         'purchases': page,
#         'keyword': keyword,
#         'filter_criteria': filter_criteria,
#         'min_price': min_price,
#         'max_price': max_price,
#         'start_date': start_date,
#         'end_date': end_date,
#         'form': form
#     })
def is_admin(user):
    return user.is_authenticated and user.userprofile.roles.filter(name='Администратор').exists()
def is_editor(user):
    return user.is_authenticated and user.userprofile.roles.filter(name='Редактор').exists()
def is_admin_or_editor(user):
    return user.is_authenticated and (user.userprofile.roles.filter(name='Администратор').exists() or user.userprofile.roles.filter(name='Редактор').exists())

@login_required
def filter_purchase(request):
    # form = PurchaseForm(request.POST)
    difference = []
    form = CSVUploadForm(request.POST, request.FILES)
    filter_criteria = request.GET.get('filter_criteria', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    start_date = slugify(request.GET.get('start_date', ''))
    end_date = slugify(request.GET.get('end_date', ''))
  
    unique_purchase_orders = Purchase.objects.values_list('PurchaseOrder', flat=True).distinct()
    unique_customer_names = Purchase.objects.values_list('CustomerName', flat=True).distinct()
    unique_purchase_codes = Purchase.objects.values_list('RegistryNumber', flat=True).distinct()
    unique_procurement_orgs = Purchase.objects.values_list('ProcurementOrganization', flat=True).distinct()
    unique_Purchase_Name = Purchase.objects.values_list('PurchaseName', flat=True).distinct()
    customer_name = request.GET.get('customer_name', '')
    procurement_organization = request.GET.get('procurement_organization', '')
    search_input = request.GET.get('search_input', '')
    purchase_order = request.GET.get('purchase_order', '') 

    purchases = Purchase.objects.all()
    current_user_name = request.user.get_username()
    user_is_admin = request.user.is_authenticated and request.user.userprofile.roles.filter(name='Администратор').exists()
    user_is_editor = request.user.is_authenticated and request.user.userprofile.roles.filter(name='Редактор').exists()
    if search_input:
        purchases = purchases.filter(
        Q(ProcurementOrganization__icontains=search_input) |
        Q(CustomerName__icontains=search_input) |
        Q(RegistryNumber__icontains=search_input) |
        Q(PurchaseName__icontains=search_input)
    )


    if min_price and max_price:
        purchases = purchases.filter(
            Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
        )

    if start_date and end_date:
        purchases = purchases.filter(
            PlacementDate__gte=start_date, PlacementDate__lte=end_date
        )
    if purchase_order:
        purchases = purchases.filter(PurchaseOrder__iexact=purchase_order)
 

    if customer_name:
        purchases = purchases.filter(CustomerName=customer_name)

    if procurement_organization:
        purchases = purchases.filter(ProcurementOrganization=procurement_organization)

    if filter_criteria == 'price_asc':
        purchases = purchases.order_by('InitialMaxContractPrice')
    elif filter_criteria == 'price_desc':
        purchases = purchases.order_by('-InitialMaxContractPrice')
    elif filter_criteria == 'date_asc':
        purchases = purchases.order_by('PlacementDate')
    elif filter_criteria == 'date_desc':
        purchases = purchases.order_by('-PlacementDate')

    paginator = Paginator(purchases, 1)
    page_number = request.GET.get('page', 1)

    filters = {
    'search_input': search_input,
    'filter_criteria': filter_criteria,
    'purchase_order': purchase_order,
    'start_date': start_date,
    'end_date': end_date,
    'min_price': min_price,
    'max_price': max_price,
}

    filter_params = {
    'search_input': request.GET.get('search_input', ''),
    'filter_criteria': request.GET.get('filter_criteria', ''),
    'purchase_order': request.GET.get('purchase_order', ''),
    'start_date': request.GET.get('start_date', ''),
    'end_date': request.GET.get('end_date', ''),
    'min_price': request.GET.get('min_price', ''),
    'max_price': request.GET.get('max_price', ''),
    # Добавьте другие параметры фильтрации
}

    if 'export_excel' in request.GET:
        filtered_data = purchases.filter(
            Q(ProcurementOrganization__icontains=search_input) |
            Q(CustomerName__icontains=search_input) |
            Q(RegistryNumber__icontains=search_input) |
            Q(PurchaseName__icontains=search_input)
        )
        
        if min_price and max_price:
            filtered_data = filtered_data.filter(
                Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
            )

        if start_date and end_date:
            filtered_data = filtered_data.filter(
                PlacementDate__gte=start_date, PlacementDate__lte=end_date
            )
        
        if purchase_order:
            filtered_data = filtered_data.filter(PurchaseOrder__iexact=purchase_order)
        
        data = filtered_data.values()  
        output_excel_path = 'путь_к_вашему_файлу.xlsx'  
        export_to_excel(data, output_excel_path, filters)

        with open(output_excel_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'
       
        os.remove(output_excel_path)

        return response

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

        

    # errors = request.GET.getlist('errors')
    # difference = request.GET.getlist('difference')
    return render(request, 'filter_results.html', {
        'purchases': page,
        'filter_criteria': filter_criteria,
        'min_price': min_price,
        'max_price': max_price,
        'start_date': start_date,
        'end_date': end_date,
        'purchase_order': purchase_order, 
        'unique_purchase_orders': unique_purchase_orders,
        'unique_customer_names': unique_customer_names, 
        'unique_procurement_orgs': unique_procurement_orgs,
        'search_input': search_input,
        'unique_purchase_codes': unique_purchase_codes,
        'unique_Purchase_Name' :unique_Purchase_Name,
        'filter_params': filter_params,
        'filters':filters,
        'form': form,
        'current_user_name': current_user_name,
        'user_is_admin':user_is_admin,
        'user_is_editor':user_is_editor,
        

     
    })





# def filter_purchase(request):
#     form = PurchaseForm(request.POST)
    
#     filter_params = { 'keyword': request.POST.get('keyword', ''), 'filter_criteria': request.POST.get('filter_criteria', ''), 'min_price': request.POST.get('min_price', ''), 'max_price': request.POST.get('max_price', ''), 'start_date': request.POST.get('start_date', ''), 'end_date': request.POST.get('end_date', ''), }


#     purchases = Purchase.objects.all()

#     if filter_params['keyword']:
#         purchases = purchases.filter(Q(PurchaseName__icontains=filter_params['keyword']))

#     if filter_params['min_price'] and filter_params['max_price']:
#         purchases = purchases.filter(
#             Q(InitialMaxContractPrice__gte=filter_params['min_price']) &
#             Q(InitialMaxContractPrice__lte=filter_params['max_price'])
#         )

#     if filter_params['start_date'] and filter_params['end_date']:
#         purchases = purchases.filter(
#             PlacementDate__gte=filter_params['start_date'],
#             PlacementDate__lte=filter_params['end_date']
#         )

#     paginator = Paginator(purchases, 10)
#     page_number = request.GET.get('page', 1)

#     try:
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         page = paginator.page(1)
#     except EmptyPage:
#         page = paginator.page(paginator.num_pages)

#     return render(request, 'filter_results.html', {
#         'purchases': page,
#         'form': form,
#         'filter_params': filter_params,
#     })

# def purchase_list(request):
#     keyword = request.GET.get('keyword', '')
#     filter_criteria = request.GET.get('filter_criteria', '')
#     min_price = request.GET.get('min_price', '')
#     max_price = request.GET.get('max_price', '')
#     purchases = Purchase.objects.all()

#     if keyword:

#         purchases = purchases.filter(Q(PurchaseName__icontains=keyword))  # Замените OtherField на поле, по которому хотите выполнить поиск

#     if min_price and max_price:
      
#         purchases = purchases.filter(
#             Q(InitialMaxContractPrice__gte=min_price) & Q(InitialMaxContractPrice__lte=max_price)
#         )

#     if filter_criteria == 'price_asc':

#         purchases = purchases.order_by('InitialMaxContractPrice')
#     elif filter_criteria == 'price_desc':
#         purchases = purchases.order_by('-InitialMaxContractPrice')
#     elif filter_criteria == 'date_asc':

#         purchases = purchases.order_by('PlacementDate')
#     elif filter_criteria == 'date_desc':
#        purchases = purchases.order_by('-PlacementDate') 

#     paginator = Paginator(purchases, 10)  # Например, по 10 записей на странице
#     page_number = request.GET.get('page')
#     if page_number is None:
#         page_number = 1

#     try:
#         # Получите объект страницы с номером page_number
#         page = paginator.page(page_number)
#     except PageNotAnInteger:
#         # Если номер страницы не является целым числом, покажите первую страницу
#         page = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы находится за пределами диапазона страниц, покажите последнюю страницу
#         page = paginator.page(paginator.num_pages)


#     return render(request, 'purchase_list.html', {
#         'purchases': page,
#         'keyword': keyword,
#         'filter_criteria': filter_criteria,
#         'min_price': min_price,
#         'max_price': max_price,
        
#     })

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            for field_name in ['ApplicationStartDate', 'ApplicationEndDate', 'PlacementDate', 'UpdateDate', 'AuctionDate']:
                input_date = form.cleaned_data[field_name]
                if input_date:
                    form.instance.__dict__[field_name] = input_date
            form.save()
            return JsonResponse({'success': True, 'message': 'Закупка успешно добавлена'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = PurchaseForm()

    return render(request, 'add_purchase.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def delete_purchase(request, purchase_id):
    if request.method == "POST":
        # Ваш код для удаления закупки
        try:     
            purchase = Purchase.objects.get(pk=purchase_id)
            purchase.delete()
            return JsonResponse({"message": "Закупка успешно удалена"})
        except Purchase.DoesNotExist:
            return JsonResponse({"error": "Закупка не найдена"}, status=404)
        except Exception as e:
            return JsonResponse({"error": "Произошла ошибка при удалении закупки: " + str(e)}, status=500)
    else:
        return HttpResponseNotAllowed(["POST"])


import statistics
def save_data(request,purchase_id):
    if request.method == "POST":
        purchase_id = request.POST.get('purchaseId')

        try:
          
            purchase = Purchase.objects.get(pk=purchase_id)
            purchase.QueryCount = request.POST.get('queryCount')
            purchase.ResponseCount = request.POST.get('responseCount')
            purchase.FinancingLimit = request.POST.get('FinancingLimit')
            purchase.NMCKMarket = request.POST.get('NMCKMarket')
            tkp_values = json.loads(request.POST.get('tkpValues'))
            for tkp_number, tkp_value in tkp_values.items():
                purchase.set_tkp(int(tkp_number[3:]), tkp_value)

            additional_info = purchase.additional_info  # получаем словарь TKP
            tkp_values_all = [int(value) for value in additional_info.values()]

            if tkp_values_all:
                
                max_tkp = max(tkp_values_all)
                min_tkp = min(tkp_values_all)
                avg_tkp = sum(tkp_values_all) / len(tkp_values_all)
                purchase.AveragePrice = avg_tkp
                purchase.MinPrice = min_tkp
                purchase.MaxPrice = max_tkp
                standard_deviation = statistics.stdev(tkp_values_all)
                cv = (standard_deviation / avg_tkp) * 100
                purchase.StandardDeviation = standard_deviation
                purchase.CoefficientOfVariation = cv
            
            
            # purchase.AveragePrice = request.POST.get('averagePrice')
            # purchase.MinPrice = request.POST.get('minPrice')
            # purchase.MaxPrice = request.POST.get('maxPrice')
            # purchase.StandardDeviation = request.POST.get('standardDeviation')
            # purchase.CoefficientOfVariation = request.POST.get('coefficientOfVariation')
            # purchase.NMCKMarket = request.POST.get('nmckMarket')
            # purchase.FinancingLimit = request.POST.get('financingLimit')

          
            purchase.save()

            
            return JsonResponse({'message': 'Данные успешно обновлены'})
        except Purchase.DoesNotExist:
            return JsonResponse({'message': 'Запись не найдена'}, status=400)
    else:
        return JsonResponse({'message': 'Недопустимый запрос'}, status=400)
    



@login_required
def analis(request):
    purchases = Purchase.objects.all()
    df = pd.DataFrame(list(purchases.values('ProcurementMethod', 'PurchaseOrder')))
    pivot_table = df.pivot_table(index='ProcurementMethod', columns='PurchaseOrder', aggfunc='size', fill_value=0)
    column_sums = pivot_table.sum()
    column_means = pivot_table.mean()
    row_totals = pivot_table.sum(axis=1)
    pivot_table['Общий итог'] = row_totals
    total_purchase_counts = column_sums.sum()
    column_sums['Суммы'] = total_purchase_counts


    df2 = pd.DataFrame(list(purchases.values('PurchaseOrder', 'InitialMaxContractPrice')))
    df2['PriceRange'] = df2.apply(determine_price_range, axis=1)
    pivot_table2 = df2.pivot_table(index='PriceRange', columns='PurchaseOrder', aggfunc='size', fill_value=0)
    column_sums2 = pivot_table2.sum()
    column_means2 = pivot_table2.mean()
    row_totals2 = pivot_table2.sum(axis=1)
    pivot_table2['Общий итог'] = row_totals2
    total_purchase_counts2 = column_sums2.sum()
    column_sums2['Суммы'] = total_purchase_counts2



    context = {
    'pivot_table': pivot_table,
    'column_sums': column_sums,
    'column_means': column_means,

     'pivot_table2': pivot_table2,
    'column_sums2': column_sums2,
    'column_means2': column_means2,

    }

    return render(request, 'analis.html', context)



def determine_price_range(row):
    if row['InitialMaxContractPrice'] > 100000000:
        return 'Цена контракта более 100 000 000 тыс.руб.'
    elif 5000000 <= row['InitialMaxContractPrice'] <= 10000000:
        return 'Цена контракта 5 000 000 - 10 000 000 тыс.руб.'
    
    elif 1000000 <= row['InitialMaxContractPrice'] <= 5000000:
        return 'Цена контракта 1 000 000 - 5 000 000 тыс.руб.'
    elif 500000 <= row['InitialMaxContractPrice'] <= 1000000:
        return 'Цена контракта 500 000-  1 000 000 тыс.руб.'
    elif 200000 <= row['InitialMaxContractPrice'] <= 500000:
        return 'Цена контракта 200 000 - 500 000 тыс.руб.'
    elif 100000 <= row['InitialMaxContractPrice'] <= 200000:
        return 'Цена контракта 100 000 - 200 000 тыс.руб.'
    else:
        return 'Менее 100 тыс.руб'
    

# def handle_upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES.get('file')

#         if uploaded_file:
#             try:
#                 # Обработка CSV-файла, например, сохранение его на сервере
#                 with open(f"{uploaded_file}", 'wb') as destination:
#                     for chunk in uploaded_file.chunks():
#                         destination.write(chunk)

#                 # Далее, вы можете обработать CSV-файл и его данные
#                 errors = insert_in_table(f"{uploaded_file}")
#                 if errors:
#                     return JsonResponse({'error': 'Ошибка в обработке данных', 'details': errors}, status=400)
#                 return JsonResponse({'response': f'Успех! Данные обработаны и загружены: {uploaded_file}'})
#             except Exception as e:
#                 return JsonResponse({'error': f'Ошибка подключения или вставки данных: {str(e)}'}, status=500)
#         else:
#             return JsonResponse({'response': 'No file was uploaded.'})

#     return JsonResponse({'response': 'Invalid request method'})

def simpl(request):
    return render(request, 'simpl.html')

import tempfile
import random
import time
from django.http import HttpResponseRedirect
@user_passes_test(is_admin_or_editor)
def upload_csv(request):
    errors = []
    difference = find_records_with_differences()

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                for chunk in csv_file.chunks():
                    temp_file.write(chunk)
                temp_file.close()
                errors = insert_in_table(temp_file.name)
                difference = find_records_with_differences()
                if not errors:
                    return JsonResponse({'success': True, 'message': 'Запись успешно добавлена'})
                else:
                    return JsonResponse({'success': False, 'errors': errors}, status=400)

            except Exception as e:
                errors.append(str(e))
                return JsonResponse({'success': False, 'errors': errors}, status=500)

    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {
        'errors': errors,
        'form': form,
        'difference': difference,
    })





def delete_selected_records(request):
    if request.method == 'POST':
        record_ids = request.POST.getlist('record_ids')
        if record_ids:
            result = delete_records_by_id(record_ids)
            if result:
                return JsonResponse({'success': True, 'message': 'Записи успешно удалены'})
            else:
                return JsonResponse({'success': False, 'message': 'Ошибка при удалении записей'})
    # В случае, если запрос был не POST, вернуть JSON с сообщением об ошибке
    return JsonResponse({'success': False, 'message': 'Неверный метод запроса'})

# def login(request):
#     return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')




def login_view(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('filter_purchase')  
        else:
            return render(request, 'login.html', {'error_message': 'Неверные учетные данные'})

    return render(request, 'login.html')

def registration(request):
    if request.user.is_authenticated:
       
        logout(request)
    if request.method == 'POST':
        form = RussianUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('filter_purchase')  # Здесь 'dashboard' - это имя URL-маршрута, на который будет перенаправлен пользователь после успешной регистрации
    else:
        form = RussianUserCreationForm()

    return render(request, 'registration.html', {'form': form})

@user_passes_test(is_admin)
def view_users(request):
    users_with_roles = UserProfile.objects.prefetch_related('user', 'roles').all()

    return render(request, 'view_users.html', {'users_with_roles': users_with_roles})


def update_user_role(request, user_id):
    if request.method == 'POST':
        new_role = request.POST.get('role')
        user = User.objects.get(pk=user_id)
        user_profile, _ = UserProfile.objects.get_or_create(user=user)

        # Определите логику обновления роли пользователя в UserProfile
        # Например, если в вашей модели UserProfile есть поле roles, то:
        user_profile.roles.clear()
        user_profile.roles.add(Role.objects.get(name=new_role))

        updated_roles = ', '.join([role.name for role in user_profile.roles.all()])

        return JsonResponse({'updatedRoles': updated_roles})

    return JsonResponse({'error': 'Invalid request'})

def user_logout(request):
    logout(request)
    return redirect('login')