from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import BlackcatPackage
from .extra.package_manager import PackageManager

packages_id = set()
pm = PackageManager()

def index(request):
    return render(request, 'index.html')

def query(request):
    sites_name = {
        'blackcat': '黑貓宅急便',
        'chinese': '中華郵政',
    }

    query_id = request.GET['query_id']
    site = request.GET['site']
    print(query_id)
    package = BlackcatPackage.objects.get(query_id=query_id)

    context = {
        'query_id': query_id,
        'site': sites_name[site],
        'state': package.state,
        'login_date': package.login_date,
        'establishment': package.establishment
    }

    return render(request, 'query.html', context)

def package(request):
    if request.method == 'POST':
        query_id = request.POST['query_id']
        site = request.POST['site']
        pm.add(query_id)
        pm.update()
        return render(request, 'package.html', {'new_id': query_id})
    elif request.method == 'GET':
        pm.update()
        return render(request, 'package.html', { 'packages': pm.package_ids })


