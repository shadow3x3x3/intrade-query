import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import BlackcatPackage
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
    query_id = request.GET['query_id']
    site = request.GET['site']
    print(query_id)
    try:
        package = BlackcatPackage.objects.get(query_id=query_id)
        context = {
            'query_id': query_id,
            'site': SITE_NAMES[site],
            'state': package.state,
            'login_date': package.login_date,
            'establishment': package.establishment
        }
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
            # pm.update()
            package_json = json.dumps({ 'packages': query_id })
        else:
            package_json = json.dumps({ 'packages': 'NOEXIST' })
        return HttpResponse(package_json, content_type='application/json')
    elif request.method == 'GET':
        pm.update()
        return render(request, 'package.html', { 'packages': pm.package_ids })


