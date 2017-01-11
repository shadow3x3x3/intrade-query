import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import BlackcatPackage, ChinesePackage, IntradePackage
from .extra.package_manager import PackageManager

SITE_NAMES = {
    'blackcat': '黑貓宅急便',
    'chinese': '中華郵政',
}

packages_id = set()
pm = PackageManager()

def index(request):
    return render(request, 'index.html')

def query(request):
    context = {}
    query_id = request.GET['query_id']
    print(query_id)
    try:
        intrade_package = IntradePackage.objects.get(query_id=query_id)
        context = retrieve_package_info(context, intrade_package)
        return render(request, 'query.html', context)
    except ObjectDoesNotExist:
        context = {
            'query_id': '包裹號碼為{}的資料不存在'.format(query_id),
            'site': '',
            'state': '',
            'login_date': '',
            'establishment': ''
        }
        return render(request, 'query.html', context)

def package(request):
    if request.method == 'POST':
        print(request.POST)
        query_id = request.POST['query_id']
        # site = request.POST['site']
        if pm.add(query_id):
            package_json = json.dumps({ 'packages': query_id })
        else:
            package_json = json.dumps({ 'packages': 'NOEXIST' })
        return HttpResponse(package_json, content_type='application/json')
    elif request.method == 'GET':
        pm.update()
        return render(request, 'package.html', { 'packages': pm.package_ids })

def retrieve_package_info(context, intrade_package):
    print(intrade_package.chinese_id)
    if intrade_package.chinese_id:
        chinese_package = intrade_package.chinese_id
        context['chinese'] = {
            'state': chinese_package.state,
            'login_date': chinese_package.login_date,
            'establishment': chinese_package.location
        }
    if intrade_package.blackcat_id:
        blackcat_package = intrade_package.blackcat_id
        context['blackcat'] = {
            'state': blackcat_package.state,
            'login_date': blackcat_package.login_date,
            'establishment': blackcat_package.establishment
        }
    return context